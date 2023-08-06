/****** Object:  StoredProcedure [state].[AddDropboxQueue]    Script Date: 8/13/2021 10:16:31 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[AddDropboxQueue]
	@FolderName NVARCHAR(256)
	,@FileName NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;

	

	IF(@FolderName IS NULL AND @FileName IS NULL)
	BEGIN
		RETURN 0
	END

	DECLARE @ObjectId INT;
	DECLARE @MatchID INT;


	-- Grab the highest ranked match
	SELECT TOP 1 @ObjectId=ObjectId ,@MatchID=fom.FileObjectMatchId
							 FROM [state].[FileObjectMatch] fom 
								INNER JOIN [state].ObjectList ol ON fom.ObjectSchema = ol.ObjectSchema and fom.ObjectName = ol.ObjectName AND fom.DataBaseId = ol.DatabaseId
									AND ol.IncludeInLoad=1 
							 WHERE @FolderName LIKE fom.FolderRegex
								AND @FileName LIKE fom.FileRegex
							 ORDER BY fom.ApplyRank,fom.FileObjectMatchId
							 ;


	INSERT INTO [state].[DropboxQueue](FolderName,FileName,QueueTimeUTC,ObjectId,FileObjectMatchId)
	VALUES (@FolderName,@FileName,GETUTCDATE(),@ObjectId,@MatchID)
	DECLARE @QueueID INT = SCOPE_IDENTITY()

	IF(@MatchID IS NOT NULL)
		SELECT @MatchID AS MatchId, @QueueId AS QueueId
	ELSE
		SELECT -1 AS MatchId, @QueueId AS QueueId

END;


/****** Object:  StoredProcedure [state].[AddUpdateDatabaseExtractStatus]    Script Date: 8/13/2021 10:16:57 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[AddUpdateDatabaseExtractStatus]
	@DatabaseId         INT,
    @loadGroup			INT,
	@databaseLoadId     INT,
    @dataFactoryRunId   CHAR(36),
    @Phase			    VARCHAR(30),
    @startTimeUtc       DATETIME2(7),
    @endTimeUtc         DATETIME2(7),
	@statusId			INT = 1,
	@returnResult		BIT = 1
AS
BEGIN

DECLARE @lv_databaseLoadId INT;
--We will utilize the same table & sproc to generate and track DatabaseLoadId for a non RDBMS sources
--TODO: refactor the name of the table/sproc to make it generic, like DataSource opposed to Database
IF @startTimeUtc IS NOT NULL
	BEGIN
		--Let find out what data source is calling the sproc
		IF EXISTS (SELECT 1 FROM [state_config].[DatabaseList] WHERE DatabaseId = @DatabaseId AND TRIM(SourceType) = 'CSV File' AND TRIM(ServerName) != 'File Drop')
		BEGIN
			SELECT TOP 1 @lv_databaseLoadId = DatabaseLoadId 
			FROM [state].[DatabaseExtract] WHERE DatabaseId = @DatabaseId AND LoadGroup = @loadGroup
			AND CONVERT(char(8), [StartTimeUtc],112) = CONVERT(char(8), @startTimeUtc,112);
			PRINT @lv_databaseLoadId;
			IF @lv_databaseLoadId IS NOT NULL
			BEGIN
				SELECT @lv_databaseLoadId AS DatabaseLoadId;
				RETURN;
			END
		END
	END
ELSE 
	SET @lv_databaseLoadId = 0

IF @lv_databaseLoadId IS NULL
BEGIN
	-- Upsert the row
    MERGE [state].[DatabaseExtract] AS [OE]
	USING ( 
		VALUES (
			@databaseId,
			@DatabaseLoadId,
			@Phase,
			@dataFactoryRunId,
			@startTimeUtc,         
			@endTimeUtc,
			@loadGroup,
			@statusId
		)
	) AS [NEW] (
	   [DatabaseId]
      ,[DatabaseLoadId]
	  ,[Phase]
      ,[DataFactoryRunId]
	  ,[StartTimeUtc]
      ,[EndTimeUtc]
	  ,[LoadGroup]
	  ,[StatusId]
	) 
	ON [OE].[DatabaseId] = [NEW].[DatabaseId] AND [OE].[DatabaseLoadId] = [NEW].[DatabaseLoadId]
	-- AND [OE].[DataFactoryRunId] = [NEW].[DataFactoryRunId]
	WHEN MATCHED THEN
	   UPDATE SET
		  [StatusId] = [NEW].[StatusId],
		  [Phase] = [NEW].[Phase],
		  [EndTimeUtc] = [NEW].[EndTimeUtc]
	WHEN NOT MATCHED 
	-- Add defense again out of band runs causing issues - simply skip logging if the data is not present.
		AND @StartTimeUTC IS NOT NULL AND @loadGroup IS NOT NULL AND @Phase IS NOT NULL and @dataFactoryRunId IS NOT NULL AND @statusId IS NOT NULL 
		THEN  
		INSERT 
		(
		  [DatabaseId]
		  ,[LoadGroup]
		  ,[StatusId]
		  ,[Phase]
		  ,[DataFactoryRunId]
		  ,[StartTimeUtc]
		  ,[EndTimeUtc]
		) VALUES (
		    [NEW].[DatabaseId]
		   ,[NEW].[LoadGroup]
		   ,[NEW].[StatusId]
           ,[NEW].[Phase] 
		   ,[NEW].[DataFactoryRunId]
		   ,[NEW].[StartTimeUtc]
		   ,[NEW].[EndTimeUtc]
		)
	;
IF @returnResult = 1
	SELECT
		DE.[DatabaseLoadId],
		[OperatorName],
		[ServerName],
        [DatabaseName],
		[SourceSystemName],
		[KeyVaultSecretName],
		--[BatchProcess],
		[DNACoreTechSupportEmail]
	FROM 
		(
			SELECT 
				MAX([DatabaseLoadId]) AS DatabaseLoadId, 
				DatabaseId 
			FROM [state].[DatabaseExtract] 
			WHERE [DataFactoryRunId] = @dataFactoryRunId AND DatabaseId = @DatabaseId AND LoadGroup = @loadGroup --modified 7/20/2021 by Will
			GROUP BY DatabaseId
		) DE
		INNER JOIN [state_config].[DatabaseList] DL ON DL.[DatabaseId] = DE.[DatabaseId]
END
	
END;


/****** Object:  StoredProcedure [state].[AddUpdateObjectExtractStatusGeneric]    Script Date: 8/13/2021 10:19:15 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[AddUpdateObjectExtractStatusGeneric]
(
    @DatabaseId         INT,
    @objectId           INT,
    @dataFactoryRunId   CHAR(36),
	@LoadGroup			INT,	--Added 7/20/2021 by Will
    @sourceRowCount     INT,
    @dataRead           BIGINT,
    @dataWritten        BIGINT,
    @rowsRead           BIGINT,
    @rowsCopied         BIGINT,
    @rowsSkipped        BIGINT,
    @copyDuration       INT,
    @throughput         DECIMAL(19, 3),
    @errors             NVARCHAR(4000),
    @usedParallelCopies INT,
    @executionDetails   NVARCHAR(4000),
    @oldWaterMarkDate   DATETIME2(7),
    @oldWaterMarkId     BIGINT,
    @newWaterMarkDate   DATETIME2(7),
    @newWaterMarkId     BIGINT,
    @startTimeUtc       DATETIME2(7),
    @endTimeUtc         DATETIME2(7),
    @extractionSuccess  BIT,
    @fileDrop           VARCHAR(8000),
	@DatabaseLoadId		INT = NULL

)
AS

	BEGIN
		-- Snapshot isolation should be on.
		SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
	
		-- In order to avoid a DF issue, we treat empty as null
		SET @errors = NULLIF(@errors, '');
		SET @executionDetails = NULLIF(@executionDetails, '')

		-- Retrieve DatabaseLoadID from state.DatabaseExtract to facilitate insertion of row into state.ObjectIngest
		SELECT @DatabaseLoadId = MAX(DatabaseLoadId) 
		FROM state.DatabaseExtract
		WHERE DatabaseId = @DatabaseId
		AND LoadGroup = @LoadGroup	--Added 7/20/2021 by Will

		-- Upsert the row
		MERGE [state].[ObjectExtract] AS [OE]
		USING ( 
			VALUES (
				@DatabaseId,
				@DatabaseLoadId,
				@objectId,
				@dataFactoryRunId,
				@sourceRowCount,
				@dataRead,          
				@dataWritten,       
				@rowsRead,          
				@rowsCopied,        
				@rowsSkipped,       
				@copyDuration,      
				@throughput,        
				@errors,            
				@usedParallelCopies,
				@executionDetails,  
				@oldWaterMarkDate,  
				@oldWaterMarkId,    
				@newWaterMarkDate,  
				@newWaterMarkId,    
				@startTimeUtc,         
				@endTimeUtc, 
				@fileDrop,     
				@extractionSuccess
			)
		) AS [NEW] (
			   [DatabaseId]
			  ,[DatabaseLoadId]
			  ,[ObjectId]
			  ,[DataFactoryRunId]
			  ,[SourceRowCount]
			  ,[DataRead]
			  ,[DataWritten]
			  ,[RowsRead]
			  ,[RowsCopied]
			  ,[RowsSkipped]
			  ,[CopyDuration]
			  ,[Throughput]
			  ,[Errors]
			  ,[UsedParallelCopies]
			  ,[ExecutionDetails]
			  ,[OldWaterMarkDate]
			  ,[OldWaterMarkId]
			  ,[WaterMarkDate]
			  ,[WaterMarkId]
			  ,[StartTimeUtc]
			  ,[EndTimeUtc]
			  ,[FileDrop]
			  ,[ExtractionSuccess]
		) 
		ON [OE].[DatabaseId] = [NEW].[DatabaseId] 
			AND [OE].[DatabaseLoadId] = [NEW].[DatabaseLoadId] 
			AND [OE].[ObjectId] = [NEW].[ObjectId] 
			AND [OE].[DataFactoryRunId] = [NEW].[DataFactoryRunId]
		WHEN MATCHED THEN
		   UPDATE SET
			   [DatabaseId] = [NEW].[DatabaseId]
			  ,[DatabaseLoadId] = [NEW].[DatabaseLoadId] 
			  ,[ObjectId] = [NEW].[ObjectId]
			  ,[DataFactoryRunId] = [NEW].[DataFactoryRunId]
			  ,[SourceRowCount] = [NEW].[SourceRowCount]
			  ,[DataRead] = [NEW].[DataRead]
			  ,[DataWritten] = [NEW].[DataWritten]
			  ,[RowsRead] = [NEW].[RowsRead]
			  ,[RowsCopied] = [NEW].[RowsCopied]
			  ,[RowsSkipped] = [NEW].[RowsSkipped]
			  ,[CopyDuration] = [NEW].[CopyDuration]
			  ,[Throughput] = [NEW].[Throughput]
			  ,[Errors] = [NEW].[Errors]
			  ,[UsedParallelCopies] = [NEW].[UsedParallelCopies]
			  ,[ExecutionDetails] = [NEW].[ExecutionDetails]
			  ,[EndTimeUtc] = [NEW].[EndTimeUtc]
			  ,[OldWaterMarkDate] = [NEW].[OldWaterMarkDate]
			  ,[OldWaterMarkId] = [NEW].[OldWaterMarkId]
			  ,[WaterMarkDate] = [NEW].[WaterMarkDate]
			  ,[WaterMarkId] = [NEW].[WaterMarkId]
			  ,[FileDrop] = [NEW].[FileDrop]
			  ,[ExtractionSuccess] = [NEW].[ExtractionSuccess]
		WHEN NOT MATCHED THEN  
			INSERT 
			(
			   [DatabaseId]
			  ,[DatabaseLoadId]
			  ,[ObjectId]
			  ,[DataFactoryRunId]
			  ,[SourceRowCount]
			  ,[DataRead]
			  ,[DataWritten]
			  ,[RowsRead]
			  ,[RowsCopied]
			  ,[RowsSkipped]
			  ,[CopyDuration]
			  ,[Throughput]
			  ,[Errors]
			  ,[UsedParallelCopies]
			  ,[ExecutionDetails]
			  ,[OldWaterMarkDate]
			  ,[OldWaterMarkId]
			  ,[WaterMarkDate]
			  ,[WaterMarkId]
			  ,[StartTimeUtc]
			  ,[EndTimeUtc]
			  ,[FileDrop]
			  ,[ExtractionSuccess]
			) VALUES (
			   [NEW].[DatabaseId]
			  ,[NEW].[DatabaseLoadId]
			  ,[NEW].[ObjectId]
			  ,[NEW].[DataFactoryRunId]
			  ,[NEW].[SourceRowCount]
			  ,[NEW].[DataRead]
			  ,[NEW].[DataWritten]
			  ,[NEW].[RowsRead]
			  ,[NEW].[RowsCopied]
			  ,[NEW].[RowsSkipped]
			  ,[NEW].[CopyDuration]
			  ,[NEW].[Throughput]
			  ,[NEW].[Errors]
			  ,[NEW].[UsedParallelCopies]
			  ,[NEW].[ExecutionDetails]
			  ,[NEW].[OldWaterMarkDate]
			  ,[NEW].[OldWaterMarkId]
			  ,[NEW].[WaterMarkDate]
			  ,[NEW].[WaterMarkId]
			  ,[NEW].[StartTimeUtc]
			  ,[NEW].[EndTimeUtc]
			  ,[NEW].[FileDrop]
			  ,[NEW].[ExtractionSuccess]
			);
	
		-- First we check to see if we need to add to the ingest queue
		-- If @extractionSuccess = 1
		-- If @rowsCopied = 0 skip ingestion phase
		IF @extractionSuccess = 1 AND @rowsCopied > 0
			BEGIN
				DECLARE @deltaIngestionpreProcessingInput VARCHAR(8000);
				DECLARE @deltaIngestionpreProcessingOutput VARCHAR(8000);
				DECLARE @deltaIngestionPreProcessing BIT;
				DECLARE @deltaIngestionEnabled BIT;
				DECLARE @deltaInput VARCHAR(4000);
				DECLARE @synapseIngestionpreProcessingInput VARCHAR(8000);
				DECLARE @synapseIngestionpreProcessingOutput VARCHAR(8000);
				DECLARE @synapseIngestionPreProcessing BIT;				
				DECLARE @synapseIngestionEnabled BIT;
				DECLARE @synapseInput VARCHAR(4000);
				DECLARE @sizeMiB DECIMAL(19,3);
				DECLARE @phase VARCHAR(30);
				DECLARE @phasestatus VARCHAR(30);
				DECLARE @ingestionMode BIT;
				DECLARE @ingestId INT;
				DECLARE @polybaseColumnDefinition NVARCHAR(MAX) = ''
				DECLARE @preProcessingMaxAllocationUnits INT;
				DECLARE @polybaseResourceClass VARCHAR(20) = 'Medium';
				DECLARE @polybaseSProc VARCHAR(128);
				SELECT @synapseInput = @fileDrop;
				DECLARE @preProcessingOutputFileName VARCHAR(8000);
				DECLARE @path VARCHAR(8000);
				

				-- Get some information from the state table
				SELECT @deltaIngestionPreProcessing = [DeltaIngestionPreProcessing]
					  ,@deltaIngestionEnabled = [DeltaIngestion]
					  ,@synapseIngestionPreProcessing = [SynapseIngestionPreProcessing]
					  ,@synapseIngestionEnabled = [SynapseIngestion]					  
				FROM [state].[ObjectList]
				WHERE [ObjectId] = @objectId;

				-- Throw an error if there is a row count mismatch
				IF @sourceRowCount IS NOT NULL AND @sourceRowCount < @rowsCopied 
						
					BEGIN
						DECLARE @errorMsg VARCHAR(8000) = 'The number of copied rows is higher with the row count originally obtained.  This is indicative of an ELT issue.';
			
						UPDATE [state].[ObjectExtract] SET [ExtractionSuccess]=0, [Errors] = @errorMsg 
						WHERE [DatabaseId] = @DatabaseId AND [ObjectId] = @objectId AND [DataFactoryRunId] = @dataFactoryRunId;

						THROW 51005, @errorMsg, 1;  
					END
										 
				-- Check to see if flagged for delta ingestion 
				IF @deltaIngestionEnabled = 1 
					BEGIN
						
						--Insert Delta ingestion row
						SELECT @deltaInput = @fileDrop,
								@phase = 'DELTA',
								@phasestatus = 'QUEUED';

						SET @sizeMiB = (@dataWritten/POWER(1024.0,2));
				
						INSERT INTO [state].[ObjectIngest]
						(
							[ExtractId],
							[DatabaseId],
							[DatabaseLoadId],
							[ObjectId],
							[Phase],
							[PhaseStatus],
							[IngestionPreProcessing],
							[IngestionPreProcessingInput],
							[IngestionPreProcessingOutput],
							[ExpectedNumberOfRows],
							[Input],
							[QueueTimeUtc],
							[OriginalFileSizeInMiB]		    
						)
						VALUES
						(      
							(
								SELECT [ExtractId] FROM [state].[ObjectExtract]
								WHERE [DatabaseId] = @DatabaseId 
								AND [DatabaseLoadId] = @DatabaseLoadId
								AND [ObjectId] = @objectId 
								AND [DataFactoryRunId] = @dataFactoryRunId
							),										-- ExtractId - int	
							@DatabaseId,							-- DatabaseId - int
							@DatabaseLoadId,						-- [LoadGroup] int
							@objectId,								-- ObjectId - int
							@phase,									-- Phase - varchar(30)
							@phasestatus,							-- Phase Status - varchar(30)
							@deltaIngestionPreProcessing,           -- DeltaPreProcessing - bit
							@deltaIngestionpreProcessingInput,      -- PreProcessingInput - nvarchar(4000)
							@deltaIngestionpreProcessingOutput,     -- PreProcessingOutput - nvarchar(4000)
							@rowsCopied,							-- ExpectedNumberOfRows - int
							@deltaInput,							-- Delta Input	
							SYSUTCDATETIME(),						-- QueueTime - datetime2(7)
							@sizeMiB								-- OriginalFileSizeInMiB - decimal(19, 3)
						);

						-- End of Delta Ingestion block
						
						/* Disabling Stage Ingestion */
						/*
						--Insert Stage ingestion row
						SELECT  @phase = 'STAGE',
								@phasestatus = 'QUEUED';

						SET @sizeMiB = (@dataWritten/POWER(1024.0,2));
				
						INSERT INTO [state].[ObjectIngest]
						(
							[ExtractId],
							[DatabaseId],
							[DatabaseLoadId],
							[ObjectId],
							[Phase],
							[PhaseStatus],
							[IngestionPreProcessing],
							[ExpectedNumberOfRows],
							[Input],
							[QueueTimeUtc],
							[OriginalFileSizeInMiB]		    
						)
						VALUES
						(      
							(
								SELECT [ExtractId] FROM [state].[ObjectExtract]
								WHERE [DatabaseId] = @DatabaseId 
								AND [DatabaseLoadId] = @DatabaseLoadId
								AND [ObjectId] = @objectId 
								AND [DataFactoryRunId] = @dataFactoryRunId
							),										-- ExtractId - int	
							@DatabaseId,							-- DatabaseId - int
							@DatabaseLoadId,						-- [LoadGroup] int
							@objectId,								-- ObjectId - int
							@phase,									-- Phase - varchar(30)
							@phasestatus,							-- Phase Status - varchar(30)
							@deltaIngestionPreProcessing,           -- DeltaPreProcessing - bit
							@rowsCopied,							-- ExpectedNumberOfRows - int
							(
								SELECT OL.ObjectSchema + '/' + OL.ObjectName FROM [state].[ObjectExtract] OE
								INNER JOIN [state].[ObjectList] OL ON [OE].[ObjectId] = [OL].[ObjectId]
								WHERE [OE].[DatabaseId] = @DatabaseId 
								AND [OE].[DatabaseLoadId] = @DatabaseLoadId
								AND [OE].[ObjectId] = @objectId 
								AND [OE].[DataFactoryRunId] = @dataFactoryRunId
							),
							SYSUTCDATETIME(),						-- QueueTime - datetime2(7)
							@sizeMiB								-- OriginalFileSizeInMiB - decimal(19, 3)
						);
						
						-- End of Stage Ingestion block
						*/

						-- Insert Synapse ingestion row
						IF @synapseIngestionPreProcessing = 1

							BEGIN
								

								SELECT @preProcessingOutputFileName = REPLACE(RIGHT(@synapseIngestionpreProcessingInput, CHARINDEX('/', REVERSE(@synapseIngestionpreProcessingInput) + '/') - 2), 'dat', 'txt');
								SELECT @path = LEFT(@synapseIngestionpreProcessingInput, LEN(@synapseIngestionpreProcessingInput) - CHARINDEX('/', REVERSE(@synapseIngestionpreProcessingInput))) + '/';
								SELECT @synapseIngestionpreProcessingOutput = (@path + @preProcessingOutputFileName),
										@synapseInput = (@path + @preProcessingOutputFileName),
										@phase = 'SYNAPSE',
										@phasestatus = 'PREPROCESSING';

							END; -- End of Synapse PreProcessing code block

						ELSE 
							BEGIN

								SELECT @synapseInput = @fileDrop,
										@phase = 'SYNAPSE',
										@phasestatus = 'QUEUED';
							END; 

						-- If this object is not to be ingested (for now) we set the phase to skipped. This will be skipped in current SProc but leaving in event needed for future.
						IF @synapseIngestionEnabled = 0 
							BEGIN
								SET @phase = 'SYNAPSE'
								SET @phasestatus = 'SKIPPED';
							END;

						SET @sizeMiB = (@dataWritten/POWER(1024.0,2));
						-- We assign an allocation unit for each 5 GB.
						SET @preProcessingMaxAllocationUnits = CEILING(@sizeMiB/5120.);

						-- We Adjust that value based on constaints
						SELECT @preProcessingMaxAllocationUnits=CASE WHEN @preProcessingMaxAllocationUnits < 1 THEN 1 WHEN @preProcessingMaxAllocationUnits > 32 THEN 32 ELSE @preProcessingMaxAllocationUnits END;
        
						-- We need to determine the appropriate resource class.
						IF @sizeMiB < 100 BEGIN
							SET @polybaseResourceClass = 'Small';
						END;
						ELSE IF @sizeMiB > 10240 BEGIN
							SET @polybaseResourceClass = 'XLarge';
						END;
						ELSE IF @sizeMiB > 5120 BEGIN
							SET @polybaseResourceClass = 'Large';
						END;

						-- We generate the sproc name here.  Note that the length limit on the sproc name is prohibitive.  May need to adjust naming convention.
						SELECT @polybaseSProc = ('[stg].[p_' + [DL].[ServerName] + ISNULL('__' + [DL].[DatabaseName], '') + ISNULL('__' + [OL].[ObjectSchema], '') + '__' + [OL].[ObjectName] + ']')
						FROM [state].[ObjectList] [OL]
						INNER JOIN [state_config].[DatabaseList] [DL]
							ON [DL].[DatabaseId] = [OL].[DatabaseId]
						WHERE
						[OL].[ObjectId] = @objectId
						AND [DL].[DatabaseId] = @DatabaseId;


						SELECT @polybaseColumnDefinition =
									CASE WHEN [FL].SynapseIngestion = 1	
											THEN STRING_AGG((CAST([FL].ColumnName AS NVARCHAR(MAX)) + N' ' + [FL].ColumnType+ N' ' + 
														CASE [FL].[Nullable] WHEN 1 
																				THEN N'NULL' 
																			 WHEN 0 
																				THEN N'NOT NULL' 
														END), ',') 
															WITHIN GROUP (ORDER BY [ColumnOrdinal]) 
											ELSE NULL 
									END 
						FROM [state].[FieldList] [FL] 
						WHERE [FL].[ObjectId] = @objectId 
						AND [FL].[DatabaseId] = @DatabaseId
						GROUP BY [FL].[SynapseIngestion]						


						-- We need to add a row to the ingest table
						INSERT INTO [state].[ObjectIngest]
						(
							[ExtractId],
							[DatabaseId],
							[DatabaseLoadId],
							[ObjectId],
							[Phase],
							[PhaseStatus],
							[IngestionPreProcessing],
							[IngestionPreProcessingInput],
							[IngestionPreProcessingOutput],
							[IngestionPreProcessingMaxAllocationUnits],
							[ExpectedNumberOfRows],
							[Input],
							[PolybaseResourceClass],
							[ColumnDefinition],
							[QueueTimeUtc],
							[OriginalFileSizeInMiB]
						)
						VALUES
						(      
							(
								SELECT [ExtractId] FROM [state].[ObjectExtract]
								WHERE [DatabaseId] = @DatabaseId 
								AND [ObjectId] = @objectId 
								AND [DataFactoryRunId] = @dataFactoryRunId
							),										-- ExtractId - int 
							@DatabaseId,							-- DatabaseId - int
							@DatabaseLoadId,						-- [LoadGroup] int
							@objectId,								-- ObjectId - int
							@phase,									-- Phase - varchar(30)
							@phasestatus,							-- PhaseStatus varchar(30)
							@synapseIngestionPreProcessing,         -- PolybasePreProcessing - bit
							@synapseIngestionpreProcessingInput,    -- PreProcessingInput - nvarchar(4000)
							@synapseIngestionpreProcessingOutput,   -- PreProcessingOutput - nvarchar(4000)
							@preProcessingMaxAllocationUnits,       -- PreProcessingMaxAllocationUnits - int
							@rowsCopied,							-- ExpectedNumberOfRows - int
							@synapseInput,							-- PolybaseInput - nvarchar(4000)
							@polybaseResourceClass,                 -- PolybaseResourceClass - varchar(20)
							@polybaseColumnDefinition,				-- PolybaseColumnDefinition - nvarchar(max)
							SYSDATETIMEOFFSET(),					-- QueueTime - datetimeoffset(7)
							@sizeMiB								-- OriginalFileSizeInMiB - decimal(19, 3)
						);
						
					END; -- End of Synapse code block

				ELSE IF	@synapseIngestionEnabled = 1 

					BEGIN
						
						IF @synapseIngestionPreProcessing = 1

							BEGIN
								

								SELECT @preProcessingOutputFileName = REPLACE(RIGHT(@synapseIngestionpreProcessingInput, CHARINDEX('/', REVERSE(@synapseIngestionpreProcessingInput) + '/') - 2), 'dat', 'txt');
								SELECT @path = LEFT(@synapseIngestionpreProcessingInput, LEN(@synapseIngestionpreProcessingInput) - CHARINDEX('/', REVERSE(@synapseIngestionpreProcessingInput))) + '/';
								SELECT @synapseIngestionpreProcessingOutput = (@path + @preProcessingOutputFileName),
										@synapseInput = (@path + @preProcessingOutputFileName),
										@phase = 'SYNAPSE',
										@phasestatus = 'PREPROCESSING';

							END; -- End of Synapse PreProcessing code block

						ELSE 
							BEGIN

								SELECT @synapseInput = @fileDrop,
										@phase = 'SYNAPSE',
										@phasestatus = 'QUEUED';
							END; 

						-- If this object is not to be ingested (for now) we set the phase to skipped. This will be skipped in current SProc but leaving in event needed for future.
						IF @synapseIngestionEnabled = 0 
							BEGIN
								SET @phase = 'SYNAPSE'
								SET @phasestatus = 'SKIPPED';
							END;

						SET @sizeMiB = (@dataWritten/POWER(1024.0,2));
						-- We assign an allocation unit for each 5 GB.
						SET @preProcessingMaxAllocationUnits = CEILING(@sizeMiB/5120.);

						-- We Adjust that value based on constaints
						SELECT @preProcessingMaxAllocationUnits=CASE WHEN @preProcessingMaxAllocationUnits < 1 THEN 1 WHEN @preProcessingMaxAllocationUnits > 32 THEN 32 ELSE @preProcessingMaxAllocationUnits END;
        
						-- We need to determine the appropriate resource class.
						IF @sizeMiB < 100 BEGIN
							SET @polybaseResourceClass = 'Small';
						END;
						ELSE IF @sizeMiB > 10240 BEGIN
							SET @polybaseResourceClass = 'XLarge';
						END;
						ELSE IF @sizeMiB > 5120 BEGIN
							SET @polybaseResourceClass = 'Large';
						END;

						-- We generate the sproc name here.  Note that the length limit on the sproc name is prohibitive.  May need to adjust naming convention.
						SELECT @polybaseSProc = ('[stg].[p_' + [DL].[ServerName] + ISNULL('__' + [DL].[DatabaseName], '') + ISNULL('__' + [OL].[ObjectSchema], '') + '__' + [OL].[ObjectName] + ']')
						FROM [state].[ObjectList] [OL]
						INNER JOIN [state_config].[DatabaseList] [DL]
							ON [DL].[DatabaseId] = [OL].[DatabaseId]
						WHERE
						[OL].[ObjectId] = @objectId
						AND [DL].[DatabaseId] = @DatabaseId;


						SELECT @polybaseColumnDefinition =
									CASE WHEN [FL].SynapseIngestion = 1	
											THEN STRING_AGG((CAST([FL].ColumnName AS NVARCHAR(MAX)) + N' ' + [FL].ColumnType+ N' ' + 
														CASE [FL].[Nullable] WHEN 1 
																				THEN N'NULL' 
																			 WHEN 0 
																				THEN N'NOT NULL' 
														END), ',') 
															WITHIN GROUP (ORDER BY [ColumnOrdinal]) 
											ELSE NULL 
									END 
						FROM [state].[FieldList] [FL] 
						WHERE [FL].[ObjectId] = @objectId 
						AND [FL].[DatabaseId] = @DatabaseId
						GROUP BY [FL].[SynapseIngestion]						


						-- We need to add a row to the ingest table
						INSERT INTO [state].[ObjectIngest]
						(
							[ExtractId],
							[DatabaseId],
							[DatabaseLoadId],
							[ObjectId],
							[Phase],
							[PhaseStatus],
							[IngestionPreProcessing],
							[IngestionPreProcessingInput],
							[IngestionPreProcessingOutput],
							[IngestionPreProcessingMaxAllocationUnits],
							[ExpectedNumberOfRows],
							[Input],
							[PolybaseResourceClass],
							[ColumnDefinition],				--20210120: PBA TO REVIEW WITH WILL
							[QueueTimeUtc],
							[OriginalFileSizeInMiB]
						)
						VALUES
						(      
							(
								SELECT [ExtractId] FROM [state].[ObjectExtract]
								WHERE [DatabaseId] = @DatabaseId 
								AND [ObjectId] = @objectId 
								AND [DataFactoryRunId] = @dataFactoryRunId
							),										-- ExtractId - int 
							@DatabaseId,							-- DatabaseId - int
							@DatabaseLoadId,						-- [LoadGroup] int
							@objectId,								-- ObjectId - int
							@phase,									-- Phase - varchar(30)
							@phasestatus,							-- PhaseStatus varchar(30)
							@synapseIngestionPreProcessing,         -- PolybasePreProcessing - bit
							@synapseIngestionpreProcessingInput,    -- PreProcessingInput - nvarchar(4000)
							@synapseIngestionpreProcessingOutput,   -- PreProcessingOutput - nvarchar(4000)
							@preProcessingMaxAllocationUnits,       -- PreProcessingMaxAllocationUnits - int
							@rowsCopied,							-- ExpectedNumberOfRows - int
							@synapseInput,							-- PolybaseInput - nvarchar(4000)
							@polybaseResourceClass,                 -- PolybaseResourceClass - varchar(20)
							@polybaseColumnDefinition,				-- PolybaseColumnDefinition - nvarchar(max)
							SYSDATETIMEOFFSET(),					-- QueueTime - datetimeoffset(7)
							@sizeMiB								-- OriginalFileSizeInMiB - decimal(19, 3)
						);


					END; -- End of Synapse code block

				ELSE BEGIN
							 
						SET @phase = 'DELTA'					
						SET @phasestatus = 'SKIPPED'

						SET @sizeMiB = (@dataWritten/POWER(1024.0,2));
				
						INSERT INTO [state].[ObjectIngest]
						(
							[ExtractId],
							[DatabaseId],
							[DatabaseLoadId],
							[ObjectId],
							[Phase],
							[PhaseStatus],
							[IngestionPreProcessing],
							[IngestionPreProcessingInput],
							[IngestionPreProcessingOutput],
							[ExpectedNumberOfRows],
							[Input],
							[QueueTimeUtc],
							[OriginalFileSizeInMiB]		    
						)
						VALUES
						(      
							(
								SELECT [ExtractId] FROM [state].[ObjectExtract]
								WHERE [DatabaseId] = @DatabaseId 
								AND [DatabaseLoadId] = @DatabaseLoadId
								AND [ObjectId] = @objectId 
								AND [DataFactoryRunId] = @dataFactoryRunId
							),										-- ExtractId - int	
							@DatabaseId,							-- DatabaseId - int
							@DatabaseLoadId,						-- [LoadGroup] int
							@objectId,								-- ObjectId - int
							@phase,									-- Phase - varchar(30)
							@phasestatus,							-- Phase Status - varchar(30)
							@deltaIngestionPreProcessing,           -- DeltaPreProcessing - bit
							@deltaIngestionpreProcessingInput,      -- PreProcessingInput - nvarchar(4000)
							@deltaIngestionpreProcessingOutput,     -- PreProcessingOutput - nvarchar(4000)
							@rowsCopied,							-- ExpectedNumberOfRows - int
							@deltaInput,							-- Delta Input	
							SYSUTCDATETIME(),						-- QueueTime - datetime2(7)
							@sizeMiB								-- OriginalFileSizeInMiB - decimal(19, 3)
						);

						END; -- End of Else code block

			END; -- End of Extraction Success code block

		-- If we want to be able to use this in a Lookup, we must return a result, so we return this
		SELECT 1 AS [Success];
END;


/****** Object:  StoredProcedure [state].[AddUpdateObjectModelStatusGeneric]    Script Date: 8/13/2021 10:19:54 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[AddUpdateObjectModelStatusGeneric]
(
    @objectId           INT,
    @loadGroup			INT,
	@dataFactoryRunId   CHAR(36),
    @objectSchema       NVARCHAR(100),
    @objectName         NVARCHAR(100),
    @success			BIT,
    @errors             NVARCHAR(4000),
    @startTimeUtc       DATETIME2(7),
    @endTimeUtc         DATETIME2(7)

)
AS

	BEGIN
		-- Snapshot isolation should be on.
		SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
	
		-- In order to avoid a DF issue, we treat empty as null
		SET @errors = NULLIF(@errors, '');

		-- Upsert the row
		MERGE [state].[ObjectModel] AS [OM]
		USING ( 
			VALUES (
				@objectId,
				@LoadGroup,
				@dataFactoryRunId,
				@objectSchema,
				@objectName,
				@success,
				@errors,
				@startTimeUtc,
				@endTimeUtc
			)
		) AS [NEW] (
			   [ObjectId]			
			  ,[LoadGroup]			
			  ,[DataFactoryRunId]	
			  ,[ObjectSchema]		
			  ,[ObjectName]		
			  ,[Success]			
			  ,[Error]				
			  ,[StartTimeUtc]		
			  ,[EndTimeUtc]
		) 
		ON [OM].[ObjectId] = [NEW].[ObjectId] 
			AND [OM].[LoadGroup] = [NEW].[LoadGroup] 
			AND [OM].[ObjectSchema] = [NEW].[ObjectSchema]
			AND [OM].[ObjectName] = [NEW].[ObjectName]
			AND [OM].[DataFactoryRunId] = [NEW].[DataFactoryRunId]
		WHEN MATCHED THEN
		   UPDATE SET
			   [Success]		= [NEW].[Success]		
			  ,[Error]			= [NEW].[Error]						 
			  ,[EndTimeUtc]		= [NEW].[EndTimeUtc]
		WHEN NOT MATCHED THEN  
			INSERT 
			(
			   [ObjectId]		
			  ,[LoadGroup]		
			  ,[DataFactoryRunId]
			  ,[ObjectSchema]	
			  ,[ObjectName]		
			  ,[Success]		
			  ,[Error]			
			  ,[StartTimeUtc]	
			  ,[EndTimeUtc]
			) VALUES (
			   [NEW].[ObjectId]		
			  ,[NEW].[LoadGroup]		
			  ,[NEW].[DataFactoryRunId]
			  ,[NEW].[ObjectSchema]	
			  ,[NEW].[ObjectName]		
			  ,[NEW].[Success]		
			  ,[NEW].[Error]			
			  ,[NEW].[StartTimeUtc]	
			  ,[NEW].[EndTimeUtc]
			);

		-- If we want to be able to use this in a Lookup, we must return a result, so we return this
		SELECT 1 AS [Success];
END;


/****** Object:  StoredProcedure [state].[AddUpdateObjectTransformationEngineStatusGeneric]    Script Date: 8/13/2021 10:20:15 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[AddUpdateObjectTransformationEngineStatusGeneric]
(
    @objectId           INT = 0,
    @loadGroup			INT = -1,
	@dataFactoryRunId   CHAR(36),
    @objectSchema       NVARCHAR(100) = NULL,
    @objectName         NVARCHAR(100) = NULL,
    @success			BIT,
    @errors             NVARCHAR(4000),
    @startTimeUtc       DATETIME2(7),
    @endTimeUtc         DATETIME2(7),
	@filePath			NVARCHAR(4000) = NULL

)
AS

	BEGIN
		-- Snapshot isolation should be on.
		SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
	
		-- In order to avoid a DF issue, we treat empty as null
		SET @errors = NULLIF(@errors, '');

		-- Upsert the row
		MERGE [state].[ObjectModel] AS [OM]
		USING ( 
			SELECT DISTINCT 
							OML.[ObjectId]			AS [ObjectId]		
						   ,OML.[LoadGroup]			AS [LoadGroup]		
						   ,@dataFactoryRunId 		AS [DataFactoryRunId]
						   ,OML.[ObjectSchema]		AS [ObjectSchema]	
						   ,OML.[ObjectName]		AS [ObjectName]		
						   ,@success		  		AS [Success]		
						   ,@errors			  		AS [Error]			
						   ,@startTimeUtc	  		AS [StartTimeUtc]	
						   ,@endTimeUtc		  		AS [EndTimeUtc]
						   ,@filePath				AS [FilePath]
			FROM [state].[ObjectModelList] OML
			WHERE [LoadGroup] = -1
			AND OML.[ObjectSchema] = ISNULL(@objectSchema,OML.[ObjectSchema])
			AND OML.[ObjectName]   = ISNULL(@objectName,OML.[ObjectName])
			
		) AS [NEW]
		ON [OM].[ObjectId] = [NEW].[ObjectId] 
			AND [OM].[LoadGroup] = [NEW].[LoadGroup] 
			AND [OM].[ObjectSchema] = [NEW].[ObjectSchema]
			AND [OM].[ObjectName] = [NEW].[ObjectName]
			AND [OM].[DataFactoryRunId] = [NEW].[DataFactoryRunId]
		WHEN MATCHED THEN
		   UPDATE SET
			   [Success]		= [NEW].[Success]		
			  ,[Error]			= [NEW].[Error]						 
			  ,[EndTimeUtc]		= [NEW].[EndTimeUtc]
			  ,[FilePath]		= [NEW].[FilePath]
		WHEN NOT MATCHED THEN  
			INSERT 
			(
			   [ObjectId]		
			  ,[LoadGroup]		
			  ,[DataFactoryRunId]
			  ,[ObjectSchema]	
			  ,[ObjectName]		
			  ,[Success]		
			  ,[Error]			
			  ,[StartTimeUtc]	
			  ,[EndTimeUtc]
			) VALUES (
			   [NEW].[ObjectId]		
			  ,[NEW].[LoadGroup]		
			  ,[NEW].[DataFactoryRunId]
			  ,[NEW].[ObjectSchema]	
			  ,[NEW].[ObjectName]		
			  ,[NEW].[Success]		
			  ,[NEW].[Error]			
			  ,[NEW].[StartTimeUtc]	
			  ,[NEW].[EndTimeUtc]
			);

		-- If we want to be able to use this in a Lookup, we must return a result, so we return this
		SELECT 1 AS [Success];
END;


/****** Object:  StoredProcedure [state].[GetDataModelList]    Script Date: 8/13/2021 10:20:36 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetDataModelList] 
( 
	@loadGroup INT
	,@databaseId INT 
	,@phase		   nvarchar(30)
	,@ModelName	   nvarchar(100) = NULL
	,@TargetSchema nvarchar(255) = NULL
	,@TargetObject nvarchar(255) = NULL
	,@TableType    nvarchar(15)
)
AS
	BEGIN
		
		SELECT  DISTINCT DL.OperatorName AS Operator
			,@databaseId AS databaseId
			,DMC.TargetSchemaName
			,DMC.TargetTableName
			,DL.ClusterId	 AS DatabricksClusterId
			,DSC.CommandText AS DatabricksNotebookPath
		FROM [state_config].[DataModelConfig] DMC
		INNER JOIN [state_config].[DatabaseList] DL ON  @databaseId = DL.DatabaseId
													AND DMC.Active     = DL.Active
		INNER JOIN [state_config].[DatabaseToStepCommand] DSC ON DL.DatabaseId = DSC.DatabaseId
															  AND ISNULL(@loadGroup,-1) = DSC.LoadGroup
															  AND DL.Active = DSC.Active

		--INNER JOIN [state].[ObjectModelList] OML ON  DMC.TargetSchemaName = OML.ObjectSchema 
		--										 AND DMC.TargetTableName  = OML.ObjectName
		--										 AND DMC.Active = OML.IncludeInLoad
		WHERE DSC.LoadGroup = ISNULL(@loadGroup,-1)		
		AND DMC.Active = 1		
		AND DSC.Phase = @phase
		AND DL.[DatabaseId] = ISNULL(@databaseId,DL.[DatabaseId])
		AND DMC.ModelName = ISNULL(@ModelName, DMC.ModelName)
		AND DMC.TargetSchemaName = ISNULL(@TargetSchema,DMC.TargetSchemaName)
		AND DMC.TargetTableName = ISNULL(@TargetObject,DMC.TargetTableName)
		AND UPPER(LTRIM(RTRIM(DMC.TableType))) = UPPER(LTRIM(RTRIM(@TableType)))

END;


/****** Object:  StoredProcedure [state].[GetFileObjectToCopy]    Script Date: 8/13/2021 10:20:51 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetFileObjectToCopy]
	@QueueId INT 
AS
BEGIN
	SET NOCOUNT ON
	
	SELECT  
		dl.[DatabaseId],
		ol.[ObjectSchema],
		ol.[ObjectName],
		ol.[DeltaIngestionPreProcessing],
		ol.[LoadGroup],
		CAST(CASE WHEN fom.ConversionType= 'None' THEN 1 ELSE 0 End AS bit) AS NoConversion,
		CAST(CASE WHEN fom.ConversionType= 'CSVToORC' THEN 1 ELSE 0 End AS bit) AS CSVToORCConversion,
		CAST(CASE WHEN fom.ConversionType= 'CSVToPARQUET' THEN 1 ELSE 0 End AS bit) AS CSVToParquetConversion

	FROM [state_config].[DatabaseList] dl 
		INNER JOIN [state].[ObjectList] ol on dl.DatabaseId = ol.DatabaseId 
		INNER JOIN [state].[DropboxQueue] dq ON ol.ObjectId = dq.ObjectId
		INNER JOIN [state].[FileObjectMatch] fom ON dq.FileObjectMatchId = fom.FileObjectMatchId
	WHERE dq.QueueId  = @QueueId
END;


/****** Object:  StoredProcedure [state].[GetJobList]    Script Date: 8/13/2021 10:21:07 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetJobList] 
( 
	@LoadGroup INT 
)
AS
	BEGIN
		
		SELECT [CommandId]
			  ,[DatabaseId]
			  ,[LoadGroup]
			  ,[ExecutionOrder]
			  ,[Phase]
			  ,[CommandType]
			  ,[CommandText]
			  ,[ExecutionProcedure]
			  ,[SourceSchemaSuffix]
			  ,[TargetSchemaSuffix]
			  ,[ItemNameToExecute]
			  ,[GenericTargetFileFormat]
			  ,[SynapseTargetFileFormat]
		FROM [state_config].[DatabaseToStepCommand] DSC
		WHERE [LoadGroup] = @LoadGroup
		AND [Active] = 1
		ORDER BY LoadGroup, ExecutionOrder ASC

	END;


/****** Object:  StoredProcedure [state].[GetObjectIngestListGeneric]    Script Date: 8/13/2021 10:21:21 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetObjectIngestListGeneric] 
(
	 @databaseId INT
	,@phase VARCHAR(30)
	,@phasestatus VARCHAR(30)
	,@limit INT
	,@databaseloadid INT
	,@loadGroup INT
)
AS
	BEGIN
		
		-- Get list of objects to ingest into Delta layer
		IF @phasestatus = 'QUEUED'
			BEGIN
				-- Check to see if any Delta layer ingestions currently processing
				DECLARE @CurrentCount INT;

				SELECT @CurrentCount = COUNT(*) 
				FROM [state].[ObjectIngest] 
				WHERE [PhaseStatus] = 'PROCESSING';
		
				-- We want to block if we are currently processing.
				IF @CurrentCount > 0 
					BEGIN
						DECLARE @errorMsg VARCHAR(8000) = 'One or more ingestions are marked as in progress. If they actually are running, then ingestion is illegal at this time. Canceled pipelines may result in ingests being stuck as in-progess.  Contact Capax.';
						THROW 51000, @errorMsg, 1
					END

				-- Return a list of ingestion, filtered to avoid objects in error.
				SELECT TOP(@limit) * FROM
				(
					SELECT
							[DL].[ServerName],
							[DL].[DatabaseName],
							[DL].[DatabaseId],
							[OL].[ObjectSchema],
							[OL].[DeltaIngestion],
							[OL].[SynapseIngestion],
							[OL].[ObjectName],
							[OI].[DatabaseLoadId],
							[OI].[IngestId],
							[OI].[Phase],
							[DL].[SinkFileFormat],
							[DSC].[CommandId],
							[DSC].[CommandType],
							[DSC].[CommandText],
							[DSC].[ExecutionProcedure],
							MIN([OI].[QueueTimeUtc]) AS FirstQueueTime,
							COUNT(*) AS NumberOfFiles
					FROM [state].[ObjectIngest] AS OI INNER JOIN [state].[ObjectList] AS OL
					ON OL.[ObjectId] = OI.[ObjectId]
					INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
					INNER JOIN [state_config].[DatabaseToStepCommand] AS DSC ON [DSC].[DatabaseId] = [OI].[DatabaseId] AND [DSC].[Phase] = [OI].[Phase]
					WHERE [OI].[PhaseStatus] = @phasestatus
					AND [OI].[Phase] = @phase
					AND [OI].[DatabaseLoadId] = @databaseloadid
					AND [DSC].[LoadGroup] = @loadGroup -- Added 7/20/2021 by Will
					AND [DSC].[Active] = 1
					GROUP BY [DL].[ServerName],
								[DL].[DatabaseName],
								[DL].[DatabaseId],
								[OL].[ObjectSchema],
								[OL].[DeltaIngestion],
								[OL].[SynapseIngestion],
								[OL].[ObjectName],
								[OI].[DatabaseLoadId],
								[OI].[IngestId],
								[OI].[Phase],
								[DL].SinkFileFormat,
								[DSC].[CommandId],
								[DSC].[CommandType],
								[DSC].[CommandText],
								[DSC].[ExecutionProcedure]
				) AS Result
				WHERE NOT EXISTS (
					-- We check for failures on this object... If we get any, that object is not a canidate for ingestion.
					-- Note:  We also exclude any object not fully ingested already.
					SELECT TOP(1) [OI2].[Success] FROM [state].[ObjectIngest] [OI2]
					INNER JOIN [state].[ObjectList] AS [OL2] ON [OL2].[ObjectId] = [OI2].[ObjectId]
					INNER JOIN [state_config].[DatabaseList] AS [DL2] ON [DL2].[DatabaseId] = [OI2].[DatabaseId]
					WHERE [OL2].[ObjectName] = [Result].[ObjectName] AND [OL2].[ObjectSchema] = [Result].[ObjectSchema] 
					AND [DL2].[ServerName] = [Result].[ServerName] AND [DL2].[DatabaseName] = [Result].[DatabaseName]
					AND 
					(
						[OI2].[PhaseStatus] NOT IN ('QUEUED', 'PREPROCESSING', 'SKIPPED')
						AND ([OI2].[Success] = 0 OR [OI2].[Success] IS NULL)
					)
				)
				ORDER BY FirstQueueTime ASC;

			END;
	END;

/****** Object:  StoredProcedure [state].[GetObjectListById]    Script Date: 8/13/2021 10:21:35 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetObjectListById] 
	@databaseId INT
	,@loadGroup INT
AS
BEGIN

	SELECT 
		[state_config].[DatabaseList].[ServerName],
		[state_config].[DatabaseList].[DatabaseName],
		[state].[ObjectList].[DatabaseId],
		[state].[ObjectList].[ObjectId],
		[state].[ObjectList].[ObjectSchema],
		[state].[ObjectList].[ObjectName],		
		[state].[ObjectList].[IncludeInLoad],
		[state].[ObjectList].[LoadIncremental],
		[state].[ObjectList].[DeltaIngestionPreProcessing],
		[state].[ObjectList].[WhereQueryPart],
		[state].[ObjectList].[WaterMarkType],
		ISNULL([LH].[WaterMarkDate], '1900-01-01') AS WaterMarkDate, 
		ISNULL([LH].[WaterMarkId], 0) AS WaterMarkId,
		[state].[ObjectList].[ClientPublished],
		[state].[ObjectList].[LoadGroup],
		[state_config].[DatabaseList].[SinkFileFormat],
		[state_config].[DatabaseList].[SourceType],
		[state_config].[DatabaseList].[AutoRefreshSchema]
		FROM [state].[ObjectList]
		JOIN [state_config].[DatabaseList] 
		ON [state_config].[DatabaseList].[DatabaseId] = [state].[ObjectList].[DatabaseId]
		LEFT OUTER JOIN (SELECT [ObjectId], MAX([WaterMarkDate]) AS WaterMarkDate, MAX([WaterMarkId]) AS WaterMarkId FROM [state].[ObjectExtract] WHERE [ExtractionSuccess] = 1 GROUP BY [ObjectId]) AS [LH]
		ON [state].[ObjectList].[ObjectId] = [LH].[ObjectId]
		WHERE [state_config].[DatabaseList].[DatabaseId] = @databaseId
		AND [state].[ObjectList].[LoadGroup] = @loadGroup
		AND [state].[ObjectList].[IncludeInLoad] = 1
		ORDER BY [ObjectSchema], [ObjectName];
END;


/****** Object:  StoredProcedure [state].[GetObjectLoadGroupIngestListGeneric]    Script Date: 8/13/2021 10:32:15 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE OR ALTER PROCEDURE [state].[GetObjectLoadGroupIngestListGeneric] 
(
	 @databaseId INT
	,@phase VARCHAR(30)
	,@phasestatus VARCHAR(30)
	,@limit INT
	,@loadGroup INT
)
AS
	BEGIN
		
		-- Get list of objects to ingest into Delta layer
		IF @phasestatus = 'QUEUED'
			BEGIN
				-- Check to see if any Delta layer ingestions currently processing
				DECLARE @CurrentCount INT;

				SELECT @CurrentCount = COUNT(*) 
				FROM [state].[ObjectIngest] OI
				JOIN [state].[DatabaseExtract] DE ON [OI].[DatabaseId] = [DE].[DatabaseId] AND [OI].[DatabaseLoadId] = [DE].[DatabaseLoadId] -- Added 7/21/2021 by Will
				WHERE [PhaseStatus] = 'PROCESSING'
				AND [OI].[DatabaseId] = @databaseId -- Added 7/21/2021 by Will
				AND [DE].[LoadGroup] = @loadGroup -- Added 7/21/2021 by Will
		
				-- We want to block if we are currently processing.
				IF @CurrentCount > 0 
					BEGIN
						DECLARE @errorMsg VARCHAR(8000) = 'One or more ingestions are marked as in progress. If they actually are running, then ingestion is illegal at this time. Canceled pipelines may result in ingests being stuck as in-progess.  Contact Capax.';
						THROW 51000, @errorMsg, 1
					END

				-- Return a list of ingestion, filtered to avoid objects in error.
				SELECT TOP(@limit) * FROM
				(
					SELECT DISTINCT
							[OI].[DatabaseLoadId]
						   ,[OI].[Phase]
						   ,[OI].[DatabaseId]
						   ,[DSC].[LoadGroup]
						   ,[DSC].[CommandType] -- Added 7/21/2021 by Will
					FROM [state].[ObjectIngest] AS OI 
					INNER JOIN [state].[ObjectList] AS OL
					ON [OL].[ObjectId] = OI.[ObjectId] AND [OL].[DatabaseId] = [OI].[DatabaseId]
					INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
					INNER JOIN [state_config].[DatabaseToStepCommand] AS DSC ON [DSC].[DatabaseId] = [OI].[DatabaseId] AND [DSC].[Phase] = [OI].[Phase]
					WHERE [OI].[PhaseStatus] = @phasestatus 
					AND [OI].[Phase] = @phase
					AND [OI].[DatabaseId] = @databaseId
					AND [DSC].[LoadGroup] = @loadGroup -- Added 7/20/2021 by Will
					AND [DSC].[Active] = 1 -- Added 7/21/2021 by Will
					GROUP BY [OI].[DatabaseLoadId]
							,[OI].[Phase]
						    ,[OI].[DatabaseId]
							,[DSC].[LoadGroup]
							,[DSC].[CommandType]
				) AS Result

			END;
	END;


/****** Object:  StoredProcedure [state].[GetObjectToCopy]    Script Date: 8/13/2021 10:32:33 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetObjectToCopy]
(
    @databaseId NVARCHAR(255),
    @objectSchema NVARCHAR(255),
    @objectName   NVARCHAR(255)
)
AS
BEGIN
    SET NOCOUNT ON; 
    DECLARE @lv_objectName NVARCHAR(255);  
	DECLARE @lv_objectSchema NVARCHAR(255);  
	DECLARE @lv_databaseId INT;
    DECLARE @lv_startPosition INT;
    DECLARE @lv_expressionToSearch NVARCHAR(255);

    -- In order to avoid a DF issue, we treat empty as null
    SET @objectSchema = NULLIF(@objectSchema, '');
    SET @objectName = NULLIF(@objectName, '');

	SET @lv_databaseId = @databaseId;
    SET @lv_objectName = @objectName;
	
	SET @lv_objectSchema = @objectSchema;
	SET @lv_expressionToSearch = 'maindl/DROPBOX/';
	SELECT @lv_objectSchema = REPLACE(@lv_objectSchema,@lv_expressionToSearch,'');
	
--TO DO: Need rules for error and re-processing handling
--First we check for a fault.  If any rows are returned we error
	DECLARE @faultCount INT;

	SELECT 
		@faultCount = COUNT(1)
	FROM [state].[ObjectExtract] AS OE
		INNER JOIN [state].[ObjectList] AS OL ON OL.[ObjectId] = OE.[ObjectId]
		INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
	WHERE [OL].[DatabaseId] = @databaseId
		 AND [ObjectSchema] = @objectSchema
		 AND [ObjectName] = @objectName
		 AND [ExtractionSuccess] = 0;

	IF @faultCount > 0 
	BEGIN
		THROW 51000, 'One or more failed extractions are in the history for this object.  Since ordering is important, you must investigate and clear them to resume extraction.', 1;  
	END

    SELECT 
		   C.CompanyName AS CompanyName,
		   [ServerName],
           [DatabaseName],
		   [SourceSystemName],
           [OL].[DatabaseId],
           [OL].[ObjectId],
           [ObjectSchema],
           [ObjectName],
           [IncludeInLoad],
           [LoadIncremental],
		   [CandidateKey],
           [DeltaIngestionPreProcessing],
           (SELECT STRING_AGG(CAST([FL].[SourceQueryPart] AS NVARCHAR(MAX)), ',') WITHIN GROUP (ORDER BY [ColumnOrdinal]) FROM [state].[FieldList] [FL] WHERE [FL].[ObjectId] = [OL].[ObjectId] AND [FL].[Active] = 1) AS [FieldsQueryPart],
		   ISNULL([WhereQueryPart],'') AS [WhereQueryPart],
           [WaterMarkColumn],
           [WaterMarkColumnDataType],
           [WaterMarkType],
           CASE WHEN [LH].[WaterMarkDate] IS NULL THEN 1 ELSE 0 END AS [FirstIncrementalLoad],
           ISNULL([LH].[WaterMarkDate], '1900-01-01') AS [WaterMarkDate],
           ISNULL([LH].[WaterMarkId], 0) AS [WaterMarkId],
           [ClientPublished],
           OL.[LoadGroup],
		   [KeyVaultSecretName],
		   [DNACoreTechSupportEmail],
           [SinkFileFormat],
           [FileColDelimiter],
           [FileHeader]
    FROM [state].[ObjectList] [OL]
    JOIN [state_config].[DatabaseList]
      ON [DatabaseList].[DatabaseId] = @lv_databaseId
	INNER JOIN state_config.Company C	ON [state_config].[DatabaseList].CompanyId = C.CompanyId
    LEFT OUTER JOIN
    (
        SELECT [ObjectId],
               MAX([WaterMarkDate]) AS [WaterMarkDate],
               MAX([WaterMarkId]) AS [WaterMarkId]
        FROM [state].[ObjectExtract]
        WHERE [ExtractionSuccess] = 1
        GROUP BY [ObjectId]
    ) AS [LH]
      ON [OL].[ObjectId] = [LH].[ObjectId]
    WHERE
       [OL].[DatabaseId] = @lv_databaseId
	   AND [ObjectSchema] = @lv_objectSchema
	   AND [ObjectName] = @lv_objectName
	   AND [IncludeInLoad] = 1
END;


/****** Object:  StoredProcedure [state].[GetTransformationEngineRulesMapList]    Script Date: 8/13/2021 10:32:50 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[GetTransformationEngineRulesMapList] 
( 
	@loadGroup INT
	,@databaseId INT = NULL
	,@phase        nvarchar(30)
	,@TargetSchema nvarchar(255) = NULL
	,@TargetObject nvarchar(255) = NULL
)
AS
	BEGIN
		
		SELECT  DISTINCT DL.OperatorName AS Operator
			,TERM.[DatabaseId]
			,TERM.[TargetSchema]
			,TERM.[TargetObject] 
			,DL.ClusterId	 AS DatabricksClusterId
			,DSC.CommandText AS DatabricksNotebookPath
		FROM [state].[ObjectModelList] OML
		INNER JOIN [state_config].[TransformationEngineRulesMap] TERM ON  OML.ObjectName   = TERM.TargetObject
																	  AND OML.ObjectSchema = TERM.TargetSchema
		INNER JOIN [state_config].[DatabaseList] DL ON  ISNULL(@databaseId,TERM.[DatabaseId]) = DL.DatabaseId
													AND TERM.Active     = DL.Active
		INNER JOIN [state_config].[DatabaseToStepCommand] DSC ON DL.DatabaseId = DSC.DatabaseId
															  AND ISNULL(@loadGroup,-1) = DSC.LoadGroup
															  AND DL.Active = DSC.Active
		WHERE OML.LoadGroup = ISNULL(@loadGroup,-1)
		AND OML.IncludeInLoad = 1
		AND TERM.Active = 1
		AND DSC.Phase = @phase
		AND TERM.[DatabaseId] = ISNULL(@databaseId,TERM.[DatabaseId])
		AND TERM.[TargetSchema] = ISNULL(@TargetSchema,TERM.[TargetSchema])
		AND TERM.[TargetObject] = ISNULL(@TargetObject,TERM.[TargetObject])

	END;


/****** Object:  StoredProcedure [state].[TryGetGetDataModelList]    Script Date: 8/13/2021 10:33:04 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[TryGetGetDataModelList] 
(
    @databaseId	   int = NULL
	,@ModelName	   nvarchar(100) = NULL
	,@TargetSchema nvarchar(255) = NULL
	,@TargetObject nvarchar(255) = NULL
	,@TableType    nvarchar(15)
)
AS
	BEGIN
		
		SELECT DMC.[ModelName]
			  ,DMC.[SourceType]
			  ,DMC.[SourceSchemaName]
			  ,DMC.[SourceTableName]
			  ,DMC.[TargetSchemaName]
			  ,DMC.[TargetTableName]
			  ,DMC.[TargetColumnName]
			  ,DMC.[TargetColumnType]
			  ,DMC.[ColumnOrdinal]
			  ,DMC.[TableType]
			  ,DMC.[IncrementalLoad]
		FROM [state_config].[DataModelConfig] DMC
		WHERE DMC.[Active] = 1
		--AND [DatabaseId] = ISNULL(@DatabaseId,[DatabaseId])
		AND DMC.ModelName = ISNULL(@ModelName,DMC.ModelName)
		AND DMC.TargetSchemaName = ISNULL(@TargetSchema,DMC.TargetSchemaName)
		AND DMC.TargetTableName = ISNULL(@TargetObject,DMC.TargetTableName)
		AND UPPER(LTRIM(RTRIM(DMC.TableType))) = UPPER(LTRIM(RTRIM(@TableType)))
		ORDER BY DMC.[ModelName],DMC.[TargetSchemaName],DMC.[TargetTableName],DMC.[ColumnOrdinal]


	END;


/****** Object:  StoredProcedure [state].[TryGetObjectIngestDelta]    Script Date: 8/13/2021 10:33:17 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[TryGetObjectIngestDelta] 
(
	@phase VARCHAR(30)
   ,@fileIngestID INT
   ,@loadGroup INT
)
AS
	BEGIN
		-- In order to avoid a DF issue, we treat empty as null
		SET @phase = NULLIF(@phase, '');
		SET @fileIngestID = NULLIF(@fileIngestID, '');

		-- If ingestion phase is Delta, run Delta ingestion query
		IF UPPER(@phase) = 'DELTA'
			BEGIN
				-- First we check for a fault.  If any rows are returned we error
				DECLARE @FaultCount INT;

				SELECT @FaultCount = COUNT(*)
				FROM [state].[ObjectIngest] AS OI 
				INNER JOIN [state].[ObjectList] AS OL ON OL.[ObjectId] = OI.[ObjectId]
				INNER JOIN (SELECT DISTINCT ObjectId FROM [state].[ObjectIngest] where IngestId = @fileIngestID) OI2 ON OI.ObjectId = OI2.ObjectId
				INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
				WHERE OI.Phase = @phase
				AND [Success] = 0;

				-- We want to block if any faults
				IF @FaultCount > 0 
					BEGIN
						DECLARE @deltaErrorMsg VARCHAR(4000) = 'One or more failed ingestions are in the history for this object.  Since ordering is important, you must investigate and clear them to resume ingestion.';
						THROW 51000, @deltaErrorMsg, 1
					END

				-- Begin execution of delta ingestion
				SELECT 
					   REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_') AS SchemaName
					  ,[SC].CommandText AS NotebookPath
					  ,LOWER([TableName]) AS ObjectName
					  ,ISNULL([CandidateKey],' ') AS CandidateKey
					  ,[OI].[Input] AS FilePath
					  ,CASE [OL].[LoadIncremental] WHEN 0 THEN 'FULL' ELSE 'INCREMENTAL' END AS FileType
					  ,CASE [OL].[FileHeader] WHEN 0 THEN 'FALSE' ELSE 'TRUE' END AS FileHeader
					  ,CASE WHEN LEN([OL].[FileColDelimiter]) > 1 THEN ' ' ELSE [OL].[FileColDelimiter] END AS FileColDelimiter
					  ,CASE WHEN LEN([OL].[FileQuoteCharacter]) > 1 THEN ' ' ELSE [FileQuoteCharacter] END  AS FileQuoteCharacter
					  ,[DateFormat]
					  ,(
							SELECT ISNULL(STRING_AGG(cast([FL].[ColumnName] + ' ' + [FL].[ColumnType] as varchar(max)), ';') WITHIN GROUP (ORDER BY [FL].[ColumnOrdinal]) ,'')
							FROM [state].[ObjectIngest] [OI] 
							INNER JOIN [state].[ObjectList] [OL] ON [OI].[ObjectId] = [OL].[ObjectId]
							INNER JOIN [state].[FieldList] [FL] ON [FL].[ObjectId] = [OL].[ObjectId]
							WHERE [OI].[IngestId] = @fileIngestId AND [FL].[Active] = 1
					   ) AS FileSchema
					  ,[OL].LoadGroup
					  ,[DCL].Identifier AS ClusterId
					  ,[OL].ClientPublished
					  ,ISNULL((SELECT STRING_AGG(ColumnName,',') 
					    FROM [state].FieldList dfl WHERE dfl.ObjectId = OI.ObjectID and dfl.Active = 0),'') AS ExcludedColumns
				FROM [state].[ObjectIngest] [OI]
				INNER JOIN [state_config].[DatabaseList] [DL] ON [OI].DatabaseId = [DL].DatabaseId
				INNER JOIN [state].[ObjectList] [OL] ON [OI].[ObjectId] = [OL].[ObjectId]
				INNER JOIN [state_config].[Company] [C] ON [C].CompanyId = [DL].[CompanyId]
				INNER JOIN [state_config].[DatabaseToStepCommand] [SC] ON [OI].[DatabaseId] = [SC].[DatabaseId] AND [OI].[Phase] = [SC].[Phase]
				LEFT JOIN [state_config].DatabricksClusterLookup [DCL] ON [DCL].[Identifier] = [DL].[ClusterId]
				WHERE [OI].[IngestId] = @fileIngestId 
				AND (Success IS NULL OR Success = 0)
				AND [OI].Phase = @phase
				AND [SC].[LoadGroup] = @loadGroup -- Added 7/20/2021 by Will
				AND [SC].[Active] = 1
				ORDER BY OI.QueueTimeUtc ASC; 
		
			END
	END;


/****** Object:  StoredProcedure [state].[TryGetObjectIngestDeltaSynapse]    Script Date: 8/13/2021 10:33:30 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[TryGetObjectIngestDeltaSynapse]
(
	@phase VARCHAR(30)
   ,@fileIngestID INT
   ,@loadGroup INT
)
AS
	BEGIN
		-- In order to avoid a DF issue, we treat empty as null
		SET @phase = NULLIF(@phase, '');
		SET @fileIngestID = NULLIF(@fileIngestID, '');

		-- If ingestion phase is Stage, run Stage ingestion query
		IF UPPER(@phase) = 'SYNAPSE'		
			BEGIN

				-- First we check for a fault.  If any rows are returned we error
				DECLARE @FaultCount INT;

				SELECT @FaultCount = COUNT(*)
				FROM [state].[ObjectIngest] AS OI 
				INNER JOIN [state].[ObjectList] AS OL ON OL.[ObjectId] = OI.[ObjectId]
				INNER JOIN (SELECT DISTINCT ObjectId FROM [state].[ObjectIngest] where IngestId = @fileIngestID) OI2 ON OI.ObjectId = OI2.ObjectId
				INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
				WHERE OI.Phase = @phase
				AND [Success] = 0;

				-- We want to block if any faults
				IF @FaultCount > 0 
					BEGIN
						DECLARE @stageErrorMsg VARCHAR(4000) = 'One or more failed ingestions are in the history for this object.  Since ordering is important, you must investigate and clear them to resume ingestion.';
						THROW 51000, @stageErrorMsg, 1
					END

				--Declare variable
				DECLARE @result varchar(max);

				SELECT @result =  ISNULL(STRING_AGG(cast([FL].[ColumnName] + ' ' + [FL].[ColumnType] as varchar(max)), ',') WITHIN GROUP (ORDER BY [FL].[ColumnOrdinal]) ,'')
							FROM [state].[ObjectIngest] [OI] 
							INNER JOIN [state].[ObjectList] [OL] ON [OI].[ObjectId] = [OL].[ObjectId]
							INNER JOIN [state].[FieldList] [FL] ON [FL].[ObjectId] = [OL].[ObjectId]
							WHERE [OI].[IngestId] = @fileIngestId AND [FL].SynapseIngestion = 1 AND [FL].[Active] = 1

				-- Begin execution of Stage ingestion

				SELECT SC.CommandText		AS NotebookPath
					  ,REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_') AS DeltaSchemaName
					  ,REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_') AS TargetSchemaName
					  ,LOWER([TableName])	AS SourceObject
					  ,LOWER([TableName])	AS TargetObject
					  ,'STAGE/adb_temp' AS TempDirPath
					  ,OI.DatabaseLoadId
					  ,CASE WHEN @result = '' THEN ''
							WHEN @result <> '' THEN @result +  ' , dl_rowhash nvarchar(500) ,dl_partitionkey nvarchar(500) ,dl_iscurrent bit ,dl_recordstartdateutc nvarchar(500),dl_recordenddateutc datetime2(7),dl_sourcefilename nvarchar(500),dl_mergekey nvarchar(500)'  END AS FileSchema
					  ,[DCL].Identifier AS ClusterId
					  ,CASE [OL].[LoadIncremental] WHEN 0 THEN 'FULL' ELSE 'INCREMENTAL' END AS FileType
					  ,[LH].[OldWaterMarkDate]	AS LastRefreshDate
				FROM [state].[ObjectIngest] [OI]
				INNER JOIN [state_config].[DatabaseList] [DL] ON [OI].DatabaseId = [DL].DatabaseId
				INNER JOIN [state].[ObjectList] [OL] ON [OI].[ObjectId] = [OL].[ObjectId]
				INNER JOIN [state_config].[Company] [C] ON [C].CompanyId = [DL].[CompanyId]
				INNER JOIN [state_config].[DatabaseToStepCommand] [SC] ON [OI].[DatabaseId] = [SC].[DatabaseId] AND [OI].[Phase] = [SC].[Phase]
				LEFT JOIN [state_config].DatabricksClusterLookup [DCL] ON [DCL].[Identifier] = [DL].[ClusterId]
				LEFT OUTER JOIN
					(
						SELECT [ObjectId],
							   MAX([OldWaterMarkDate]) AS [OldWaterMarkDate]
						FROM [state].[ObjectExtract]
						WHERE [ExtractionSuccess] = 1
						GROUP BY [ObjectId]
					) AS [LH]
					  ON [OL].[ObjectId] = [LH].[ObjectId]
				WHERE OI.IngestId = @fileIngestID
				AND ([OI].Success IS NULL OR [OI].Success = 0)
				AND [OI].Phase = @phase
				AND [SC].[LoadGroup] = @loadGroup
				AND [SC].[Active] = 1
				ORDER BY OI.QueueTimeUtc ASC; 

			END -- End Stage ingestion block

	END;


/****** Object:  StoredProcedure [state].[TryGetObjectIngestStage]    Script Date: 8/13/2021 10:33:46 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[TryGetObjectIngestStage] 
(
	@phase VARCHAR(30)
   ,@fileIngestID INT
   ,@loadGroup INT
)
AS
	BEGIN
		-- In order to avoid a DF issue, we treat empty as null
		SET @phase = NULLIF(@phase, '');
		SET @fileIngestID = NULLIF(@fileIngestID, '');

		-- If ingestion phase is Stage, run Stage ingestion query
		IF UPPER(@phase) = 'STAGE'		
			BEGIN

				-- First we check for a fault.  If any rows are returned we error
				DECLARE @FaultCount INT;

				SELECT @FaultCount = COUNT(*)
				FROM [state].[ObjectIngest] AS OI 
				INNER JOIN [state].[ObjectList] AS OL ON OL.[ObjectId] = OI.[ObjectId]
				INNER JOIN (SELECT DISTINCT ObjectId FROM [state].[ObjectIngest] where IngestId = @fileIngestID) OI2 ON OI.ObjectId = OI2.ObjectId
				INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
				WHERE OI.Phase = @phase
				AND [Success] = 0;

				-- We want to block if any faults
				IF @FaultCount > 0 
					BEGIN
						DECLARE @stageErrorMsg VARCHAR(4000) = 'One or more failed ingestions are in the history for this object.  Since ordering is important, you must investigate and clear them to resume ingestion.';
						THROW 51000, @stageErrorMsg, 1
					END

				-- Begin execution of Stage ingestion

				SELECT SC.CommandText		AS NotebookPath
					  ,REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_') AS SchemaName
					  ,LOWER([TableName])	AS ObjectName
					  ,''					AS CandidateKey
					  ,REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_')	
						+ '/' + LOWER([TableName])
						+ '/' + CAST(YEAR(GETUTCDATE()) AS VARCHAR(4))
						+ '/' + CAST(MONTH(GETUTCDATE()) AS VARCHAR(2))
						+ '/' + CAST(DAY(GETUTCDATE()) AS VARCHAR(2))
						+ '/' + CAST(DATEPART(HOUR,GETUTCDATE()) AS VARCHAR(2))
						+ '_' + CAST(DATEPART(MINUTE,GETUTCDATE()) AS VARCHAR(2)) 			AS FilePath
					  ,''					AS FileType
					  ,''					AS FileHeader
					  ,''					AS FileColDelimiter
					  ,''					AS FileQuoteCharacter
					  ,''					AS [DateFormat]
					  ,''					AS FileSchema
					  ,''					AS LoadGroup
					  ,''					AS ClientPublished
					  ,[DCL].Identifier		AS ClusterId
					  ,OI.DatabaseLoadId
				FROM [state].[ObjectIngest] [OI]
				INNER JOIN [state_config].[DatabaseList] [DL] ON [OI].DatabaseId = [DL].DatabaseId
				INNER JOIN [state].[ObjectList] [OL] ON [OI].[ObjectId] = [OL].[ObjectId]
				INNER JOIN [state_config].[Company] [C] ON [C].CompanyId = [DL].[CompanyId]
				INNER JOIN [state_config].[DatabaseToStepCommand] [SC] ON [OI].[DatabaseId] = [SC].[DatabaseId] AND [OI].[Phase] = [SC].[Phase]
				LEFT JOIN [state_config].DatabricksClusterLookup [DCL] ON [DCL].[Identifier] = [DL].[ClusterId]
				WHERE [OI].[IngestId] = @fileIngestId 
				AND (Success IS NULL OR Success = 0)
				AND [OI].Phase = @phase
				AND [SC].[LoadGroup] = @loadGroup -- Added 7/20/2021 by Will
				AND [SC].[Active] = 1
				ORDER BY OI.QueueTimeUtc ASC;

			END -- End Stage ingestion block

	END;


/****** Object:  StoredProcedure [state].[TryGetObjectIngestSynapse]    Script Date: 8/13/2021 10:33:59 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


--exec [state].[TryGetObjectIngestSynapse] @phase = 'SYNAPSE', @fileIngestID = 31

CREATE OR ALTER PROCEDURE [state].[TryGetObjectIngestSynapse] 
(
	@phase VARCHAR(30)
   ,@fileIngestID INT
   ,@loadGroup INT
)
AS
	BEGIN
		-- In order to avoid a DF issue, we treat empty as null
		SET @phase = NULLIF(@phase, '');
		SET @fileIngestID = NULLIF(@fileIngestID, '');

		-- If ingestion phase is Synapse, run Synapse ingestion query
		IF UPPER(@phase) = 'SYNAPSE' 
			BEGIN

				-- First we check for a fault.  If any rows are returned we error
				DECLARE @FaultCount INT;

				SELECT @FaultCount = COUNT(*)
				FROM [state].[ObjectIngest] AS OI 
				INNER JOIN [state].[ObjectList] AS OL ON OL.[ObjectId] = OI.[ObjectId]
				INNER JOIN (SELECT DISTINCT ObjectId FROM [state].[ObjectIngest] where IngestId = @fileIngestID) OI2 ON OI.ObjectId = OI2.ObjectId
				INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
				WHERE OI.Phase = @phase
				AND [Success] = 0;
				;

				-- We want to block if any faults
				IF @FaultCount > 0 
					BEGIN
						DECLARE @synapseErrorMsg VARCHAR(4000) = 'One or more failed ingestions are in the history for this object.  Since ordering is important, you must investigate and clear them to resume ingestion.';
						THROW 51000, @synapseErrorMsg, 1
					END

				-- Begin execution of Synapse ingestion
				SELECT TOP(1) OI.[DatabaseId],  -- CURRENTLY BLOCKING to 1 for DF limitation
						0																AS [StepID],
						0																AS [StepbatchID],
						SC.CommandText													AS [CommandText],
						''																AS [ClusterID],
						OI.IngestId														AS [IngestId],
						[OI].[Input]													AS [Input],				   				   
						[OL].[LoadIncremental]											AS [LoadIncremental],
						[OI].[ExtractId]												AS [ExtractId],
						[OL].[Partition]												AS [Partition],
						REPLACE(REPLACE(REPLACE(SC.TargetSchemaSuffix,'@Operator',LOWER([DL].[OperatorName])),'@SourceSystemName',LOWER([DL].[SourceSystemName])),' ','_') + '_' + OL.ObjectSchema AS [StageSchemaName],
						[OL].[TableName]												AS [StageTableName],
						'ROUND_ROBIN'													AS [StageDistribution],
						'HEAP'															AS [StageTableType],
						0																AS [IsStageTableType2],
						[SC].[SynapseTargetFileFormat]									AS [FileFormat],
						(
							SELECT STRING_AGG(CAST((CASE WHEN [FL].SynapseIngestion = 1 AND [FL].[Active] = 1 THEN [FL].ColumnName ELSE ('''[PII]'' AS '+[FL].ColumnName) END) AS NVARCHAR(MAX)), ',') WITHIN GROUP (ORDER BY [ColumnOrdinal]) 
							FROM [state].[FieldList] [FL] 
							WHERE [FL].[ObjectId] = [OL].[ObjectId]
						)																AS [Columns],
					   
						[OI].ColumnDefinition											AS ColumnDefinition,
						[OL].[CandidateKey]												AS CandidateKey,
						( 
							SELECT STRING_AGG('[source].['+[value]+'] = [target].['+[value]+']',' AND ') 
							FROM STRING_SPLIT([OL].[CandidateKey],',') WHERE RTRIM([value]) <> ''
						)																AS IncrementalLoadQueryWhereExistsPart,
						[OI].[Phase],
						[OI].[PhaseStatus],
						[OI].[IngestionPreProcessing],
						[OI].[IngestionPreProcessingInput],
						[OI].[IngestionPreProcessingOutput],
						[OI].[IngestionPreProcessingExecutionDuration],
						[OI].[IngestionPreProcessingComputeInformation],
						[OI].[IngestionPreProcessingSuccess],
						[OI].[IngestionPreProcessingStartTimeUtc],
						[OI].[IngestionPreProcessingEndTimeUtc],
						[OI].[ExpectedNumberOfRows],
						[OI].[Success],
						[OI].[StartTimeUtc],
						[OI].[EndTimeUtc],
						[OI].[QueueTimeUtc]
				FROM [state].[ObjectIngest] AS OI INNER JOIN [state].[ObjectList] AS OL
				ON OL.[ObjectId] = OI.[ObjectId]
				INNER JOIN [state_config].[DatabaseList] AS DL ON DL.[DatabaseId] = [OL].[DatabaseId]
				INNER JOIN [state_config].[DatabaseToStepCommand] AS SC ON [SC].[DatabaseId] = [OL].[DatabaseId] AND [SC].[Phase] = [OI].[Phase]
				WHERE OI.IngestId = @fileIngestID
				AND ([OI].Success IS NULL OR [OI].Success = 0)
				AND [OI].Phase = @phase
				AND [SC].[LoadGroup] = @loadGroup -- Added 7/20/2021 by Will
				AND [SC].[Active] = 1
				ORDER BY OI.QueueTimeUtc ASC; 

			END -- End Synapse ingestion block

	END;


/****** Object:  StoredProcedure [state].[TryGetObjectModelList]    Script Date: 8/13/2021 10:34:13 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [state].[TryGetObjectModelList] 
(
    @LoadGroup int 
)
AS
	BEGIN
		
		SELECT ObjectId
			  ,LoadGroup
			  ,ObjectSchema
			  ,ObjectName			  
		FROM [state].[ObjectModelList]
		WHERE LoadGroup = @LoadGroup
		AND IncludeInLoad = 1

	END;


/****** Object:  StoredProcedure [state].[TryGetTransformationEngineRulesMapList]    Script Date: 8/13/2021 10:34:27 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[TryGetTransformationEngineRulesMapList] 
(
    @databaseId int = NULL
	,@TargetSchema nvarchar(255) = NULL
	,@TargetObject nvarchar(255) = NULL
)
AS
	BEGIN
		
		SELECT [TransformRulesMapId] AS ROW_ID
			,[DatabaseId]
			,[OperationType]
			,[Operator]
			,[TargetSchema]
			,[TargetObject]
			,[TargetAttribute]
			,[SourceSchema]
			,[SourceObject]
			,[SourceAttribute]
			,[UnionGroup]
			,[JoinGroup]
			,[Stage]
			,[TransformationType]
			,[Transformation]
			,[CodeMapped]
			,[Active]
		FROM [state_config].[TransformationEngineRulesMap]
		WHERE [Active] = 1
		AND [DatabaseId] = ISNULL(@DatabaseId,[DatabaseId])
		AND [TargetSchema] = ISNULL(@TargetSchema,[TargetSchema])
		AND [TargetObject] = ISNULL(@TargetObject,[TargetObject])
		ORDER BY [TransformRulesMapId]


	END;


/****** Object:  StoredProcedure [state].[UpdateDropboxQueue]    Script Date: 8/13/2021 10:34:45 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state].[UpdateDropboxQueue]
	@QueueId INT
		,@ProcessedTimeUTC DATETIME2
  AS 
  BEGIN
		UPDATE [state].[DropboxQueue] 
		SET ProcessedTimeUTC = @ProcessedTimeUTC 
		WHERE QueueId = @QueueId
  END;


/****** Object:  StoredProcedure [state].[UpdateObjectIngestStatusGeneric]    Script Date: 8/13/2021 10:37:38 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [state].[UpdateObjectIngestStatusGeneric] 
(
	@ingestionId INT, 
	@phase varchar(30), 
	@phasestatus varchar(30),
	@Success BIT = NULL,
	@StartTimeUtc DATETIME2(7) = NULL,
	@EndTimeUtc DATETIME2(7) = NULL,
	@Error NVARCHAR(4000) = NULL,
	@databaseLoadId INT = NULL,
	@columnDefinition NVARCHAR(MAX) = NULL,
	@filePath NVARCHAR(MAX) = NULL
)
AS
	BEGIN
		
		-- Snapshot isolation should be on.
		SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
	
		-- Update the row
		UPDATE [state].[ObjectIngest]
		SET
			[Phase]				= @phase,
			[PhaseStatus]		= @phasestatus,	--New
			[Success]			= @Success,
			[StartTimeUtc]		= ISNULL(@StartTimeUtc,[StartTimeUtc]),
			[EndTimeUtc]		= @EndTimeUtc,
			[Error]				= @Error,
			[ColumnDefinition]	= ISNULL(@columnDefinition,ColumnDefinition),
			[Input]				= ISNULL(@filePath,Input)
		WHERE [IngestId]		= @ingestionId;

		-- Return something so we can use this as a lookup activity in DF.
		SELECT 1 AS Success;
	END;


/****** Object:  StoredProcedure [state_stage].[DeleteStagedMetadata]    Script Date: 8/13/2021 10:37:53 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [state_stage].[DeleteStagedMetadata]
@DatabaseId INT
AS
BEGIN

DELETE FROM [state_stage].[ObjectList] WHERE DatabaseId = @DatabaseId

DELETE FROM [state_stage].[FieldList] WHERE DatabaseId = @DatabaseId

SELECT 'Metadata cleared'
END;


/****** Object:  StoredProcedure [state_stage].[InsertCompany]    Script Date: 8/13/2021 10:38:23 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertCompany]
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

	-- Merge new records and perform updates to state_config.Company

	MERGE state_config.Company AS tgt
	USING state_stage.Company AS src
	ON tgt.CompanyCode = src.CompanyCode

	WHEN MATCHED AND 
		(
			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),tgt.Description), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.CompanyName), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.Active), ''))))
													   AS bigint)
			
			<>

			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),src.Description), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.CompanyName), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.Active), ''))))
													   AS bigint)
		)
			THEN UPDATE SET 
		tgt.CompanyName = src.CompanyName
	   ,tgt.Description = src.Description
	   ,tgt.Active = src.Active

	WHEN NOT MATCHED THEN 
		INSERT 
			(
			 [CompanyCode]
			,[CompanyName]
			,[Description]
			,[Active]
			)
		VALUES
		  (
		   src.[CompanyCode]
		  ,src.[CompanyName]
		  ,src.[Description]
		  ,src.[Active]
		  );
END;


/****** Object:  StoredProcedure [state_stage].[InsertDatabaseList]    Script Date: 8/13/2021 10:38:39 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertDatabaseList]
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

	-- Merge new records and perform updates to state_config.DatabaseList

	MERGE state_config.DatabaseList AS tgt
	USING state_stage.DatabaseList AS src
	ON tgt.CompanyId = src.CompanyId
	AND tgt.ServerName = src.ServerName
	AND tgt.DatabaseName = src.DatabaseName
	AND tgt.ClusterId = src.ClusterId

	WHEN MATCHED AND 
		(
			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),tgt.[OperatorName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[SourceSystemName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[SourceType]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[SinkFileFormat]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[IRName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[MainDataContact]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[DNACoreTechSupportEmail]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[NumLoadGroups]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[Notes]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[KeyVaultSecretName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[AutoRefreshSchema]), ''))))
													   AS bigint)
			
			<>

			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),src.[OperatorName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[SourceSystemName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[SourceType]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[SinkFileFormat]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[IRName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[MainDataContact]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[DNACoreTechSupportEmail]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[NumLoadGroups]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[Notes]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[KeyVaultSecretName]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[AutoRefreshSchema]), ''))))
													   AS bigint)
		)
			THEN UPDATE SET 
		tgt.[OperatorName] = src.[OperatorName]
       ,tgt.[SourceSystemName] = src.[SourceSystemName]
       ,tgt.[SourceType] = src.[SourceType]
       ,tgt.[SinkFileFormat] = src.[SinkFileFormat]
       ,tgt.[IRName] = src.[IRName]
       ,tgt.[MainDataContact] = src.[MainDataContact]
       ,tgt.[DNACoreTechSupportEmail] = src.[DNACoreTechSupportEmail]
       ,tgt.[NumLoadGroups] = src.[NumLoadGroups]
       ,tgt.[Notes] = src.[Notes]
       ,tgt.[KeyVaultSecretName] = src.[KeyVaultSecretName]
       ,tgt.[DateModifiedUtc] = GETUTCDATE()
       ,tgt.[AutoRefreshSchema] = src.[AutoRefreshSchema]

	WHEN NOT MATCHED THEN 
		INSERT 
			(
			 [CompanyId]
		    ,[OperatorName]
		    ,[ServerName]
		    ,[DatabaseName]
		    ,[SourceSystemName]
		    ,[SourceType]
		    ,[SinkFileFormat]
		    ,[ClusterId]
		    ,[IRName]
		    ,[MainDataContact]
		    ,[DNACoreTechSupportEmail]
		    ,[NumLoadGroups]
		    ,[Notes]
		    ,[KeyVaultSecretName]
		    ,[Active]
		    ,[DateModifiedUtc]
		    ,[AutoRefreshSchema]
			)
		VALUES
		  (
		    src.[CompanyId]
		   ,src.[OperatorName]
		   ,src.[ServerName]
		   ,src.[DatabaseName]
		   ,src.[SourceSystemName]
		   ,src.[SourceType]
		   ,src.[SinkFileFormat]
		   ,src.[ClusterId]
		   ,src.[IRName]
		   ,src.[MainDataContact]
		   ,src.[DNACoreTechSupportEmail]
		   ,src.[NumLoadGroups]
		   ,src.[Notes]
		   ,src.[KeyVaultSecretName]
		   ,src.[Active]
		   ,GETUTCDATE()
		   ,src.[AutoRefreshSchema]
		  );
END;


/****** Object:  StoredProcedure [state_stage].[InsertDatabricksClusterLookup]    Script Date: 8/13/2021 10:38:52 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertDatabricksClusterLookup]
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

	-- Merge new records and perform updates to state_config.DatabricksClusterLookup

	MERGE state_config.DatabricksClusterLookup AS tgt
	USING state_stage.DatabricksClusterLookup AS src
	ON tgt.Identifier = src.Identifier

	WHEN MATCHED AND 
		(
			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),tgt.Name), ''))))
													   AS bigint)
			
			<>

			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),src.Name), ''))))
													   AS bigint)
		)
			THEN UPDATE SET 
		tgt.Name = src.Name
	   ,tgt.UpdatedDateUtc = GETUTCDATE()

	WHEN NOT MATCHED THEN 
		INSERT 
			(
			 [Name]
			,[Identifier]
			,[UpdatedDateUtc]
			)
		VALUES
		  (
		   src.[Name]
		  ,src.[Identifier]
		  ,GETUTCDATE()
		  );
END;


/****** Object:  StoredProcedure [state_stage].[InsertFieldList]    Script Date: 8/13/2021 10:39:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE OR ALTER PROCEDURE [state_stage].[InsertFieldList]
	@databaseId INT
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

BEGIN TRY

	BEGIN TRAN

	IF EXISTS(SELECT 1 FROM state_stage.FieldList WHERE DatabaseId = @databaseId)
	BEGIN
		-- Set fields no longer in source to Active=0
		UPDATE fl  SET Active=0
		FROM  state.FieldList fl WHERE NOT EXISTS
								( SELECT 1 from state_stage.FieldList flor
									INNER JOIN state.ObjectList ol ON flor.ObjectSchema = ol.ObjectSchema AND flor.ObjectName = ol.ObjectName AND flor.DatabaseId = ol.DatabaseId
								  WHERE fl.ObjectId = ol.ObjectId 	
									AND fl.ColumnOrdinal = flor.ColumnOrdinal	
									AND fl.DatabaseId = ol.DatabaseId
								)
				AND fl.DatabaseId = @DatabaseId
				AND fl.Active=1
	END

		;WITH src AS (
			SELECT *
			FROM (
				 SELECT 
							ol.[DatabaseId]
							,ol.[ObjectId]
							,stg.[ColumnOrdinal]
							,'[' + stg.[FieldName] + ']' AS SourceQueryPart
							,stg.[Nullable]
							,LOWER(REPLACE(REPLACE(stg.[FieldName], ' ', ''),'.','')) AS [ColumnName]
							,stg.[FieldType] AS [ColumnType]
							,ROW_NUMBER() OVER (PARTITION BY ol.DatabaseId,ol.ObjectId,stg.ColumnOrdinal ORDER BY Nullable,FieldName) as RowNum
					FROM [state_stage].[FieldList] stg
						INNER JOIN [state].[ObjectList] ol ON ol.[ObjectSchema] = stg.[ObjectSchema] 
							AND ol.ObjectName = stg.ObjectName 
							AND ol.DatabaseId = stg.DatabaseId
					WHERE  ol.DatabaseId = @databaseId
					) as x
			WHERE RowNum = 1 -- Duplication error protection
		)
		MERGE [state].[FieldList] AS tgt
		USING src ON    tgt.DatabaseId = src.DatabaseId
					AND tgt.ObjectId = src.ObjectId 
					AND tgt.ColumnOrdinal = src.ColumnOrdinal
					
		WHEN MATCHED AND (
				 tgt.Nullable != src.Nullable
				OR ISNULL(tgt.SourceQueryPart,'') != ISNULL(src.SourceQueryPart,'')
				OR ISNULL(tgt.[ColumnName],'') != ISNULL(src.[ColumnName],'')
				OR ISNULL(tgt.[ColumnType],'') != ISNULL(src.[ColumnType],'')
			)
		THEN UPDATE
			SET  SourceQueryPart = src.SourceQueryPart
				,Nullable = src.Nullable
				,[ColumnName] = src.[ColumnName]
				,[ColumnType] = src.[ColumnType]
				,Active=1
		WHEN NOT MATCHED THEN INSERT
				   ([DatabaseId]
				   ,[ObjectId]
				   ,[ColumnOrdinal]
				   ,[SourceQueryPart]
				   ,[Nullable]
				   ,[ColumnName]
				   ,[ColumnType])
			VALUES( src.[DatabaseId]
					,src.[ObjectId]
					,src.[ColumnOrdinal]
					,src.[SourceQueryPart]
					,src.[Nullable]
					,src.[ColumnName]
					,src.[ColumnType]
					);

		COMMIT TRAN

END TRY
BEGIN CATCH
	ROLLBACK TRAN
	RAISERROR('Error updating FieldList for DatabaseId:%d',16,1,@DatabaseId);
END CATCH

SELECT 'Success' AS Msg

END;


/****** Object:  StoredProcedure [state_stage].[InsertObjectList]    Script Date: 8/13/2021 10:39:24 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertObjectList]
	@databaseId INT
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

	--Insert metadata for all database objects
	INSERT INTO [state].[ObjectList]
           ([DatabaseId]
           ,[ObjectSchema]
           ,[ObjectName]
		   ,[EstimatedRowCount]
		   ,[CandidateKey]
		   ,[TableName])
	SELECT 
       stg.[DatabaseId]
      ,stg.[ObjectSchema]
      ,stg.[ObjectName]
	  ,stg.[EstimatedRowCount] AS [EstimatedRowCount]
	  ,LOWER(REPLACE(REPLACE(stg.[CandidateKey], '.', ''),' ','')) AS [CandidateKey]
	  ,stg.[ObjectName] AS [TableName]
	FROM  [state_stage].[ObjectList] stg
	WHERE DatabaseId = @databaseId
		AND NOT EXISTS(
				SELECT 1 FROM [state].[ObjectList] tgt 
				WHERE tgt.DatabaseId = stg.DatabaseId 
					AND tgt.[ObjectSchema] = stg.[ObjectSchema] 
					AND tgt.[ObjectName] = stg.[ObjectName]
			   )


	--Set objects for extraction/ingestion based on the records in ObjectExtractList table
IF EXISTS (SELECT 1 FROM [state_config].[ObjectExtractList] WHERE [DatabaseId] = @databaseId AND Active=1)
BEGIN
	UPDATE [state].[ObjectList]
	SET [IncludeInLoad] = OE.Active, [DeltaIngestion] = OE.Active, [ClientPublished] = OE.ClientPublished
	FROM [state].[ObjectList] OL
		INNER JOIN [state_config].[ObjectExtractList] OE	ON OL.[DatabaseId] = OE.[DatabaseId] AND OL.[ObjectSchema] = OE.[ObjectExtarctSchema]	AND  OL.[ObjectName] = OE.[ObjectExtractName] 
	WHERE OL.[DatabaseId] = @databaseId
		AND (OL.IncludeInLoad != OE.Active OR OL.DeltaIngestion != OE.Active OR OL.ClientPublished != OE.ClientPublished)

END ELSE BEGIN
	--Set all objects for extraction (no record(s) in the ObjectExtractList table for active record in 
	-- the DatabaseList table
	UPDATE [state].[ObjectList]
	SET [IncludeInLoad] = 1, [DeltaIngestion] = 1
	WHERE [DatabaseId] = @databaseId
		AND (IncludeInLoad=0 OR DeltaIngestion = 0)
END
	
	RETURN;
END;


/****** Object:  StoredProcedure [state_stage].[InsertObjectModelList]    Script Date: 8/13/2021 10:39:35 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertObjectModelList]
	@loadGroup INT
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

		--Insert metadata for all database objects
	INSERT INTO [state].[ObjectModelList]
           (
		    [LoadGroup]
		   ,[ObjectSchema]
           ,[ObjectName]
		   ,[IncludeInLoad]
		   )
	SELECT 
       @loadGroup AS LoadGroup
	  ,stg.[ObjectSchema]
      ,stg.[ObjectName]
	  ,1
	FROM  [state_stage].[ObjectModelList] stg
	LEFT JOIN [state].[ObjectModelList] tgt ON 
	(tgt.[LoadGroup] = @loadGroup AND tgt.[ObjectSchema] = stg.[ObjectSchema] AND tgt.[ObjectName] = stg.[ObjectName] )
	WHERE tgt.[LoadGroup] IS NULL;	

END;

	/****** Object:  StoredProcedure [state_stage].[InsertStepCommand]    Script Date: 8/13/2021 10:40:45 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [state_stage].[InsertStepCommand]
AS
BEGIN
	SET NOCOUNT ON;
    SET XACT_ABORT ON;

	-- Merge new records and perform updates to state_config.DatabaseToStepCommand
	
	MERGE state_config.DatabaseToStepCommand AS tgt
	USING state_stage.DatabaseToStepCommand AS src
	ON tgt.[DatabaseId]	= src.[DatabaseId]
		AND tgt.[LoadGroup] = src.[LoadGroup]
		AND tgt.[ExecutionOrder]	= src.[ExecutionOrder]
		AND tgt.[Phase] = src.[Phase]
		AND tgt.[CommandType] = src.[CommandType]
		AND tgt.[CommandText] = src.[CommandText]
		AND tgt.[ExecutionProcedure] = src.[ExecutionProcedure]
		AND tgt.[Active] = src.[Active]	
	
	WHEN MATCHED AND 
		(
			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),tgt.[DatabaseId]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[LoadGroup]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[ExecutionOrder]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[Phase]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[CommandType]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[CommandText]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.[ExecutionProcedure]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),tgt.Active), ''))))
													   AS bigint)
			
			<>

			CAST(Convert(BINARY(32),HashBytes('SHA2_256' , (ISNULL(Convert(NVARCHAR(4000),src.[DatabaseId]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[LoadGroup]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[ExecutionOrder]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[Phase]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[CommandType]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[CommandText]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.[ExecutionProcedure]), ''))
												   + '~' + (ISNULL(Convert(NVARCHAR(4000),src.Active), ''))))
													   AS bigint)
		)
			THEN UPDATE SET 
		 tgt.[DatabaseId]	= src.[DatabaseId]
		,tgt.[LoadGroup] = src.[LoadGroup]
		,tgt.[ExecutionOrder]	= src.[ExecutionOrder]
		,tgt.[Phase] = src.[Phase]
		,tgt.[CommandType] = src.[CommandType]
		,tgt.[CommandText] = src.[CommandText]
		,tgt.[ExecutionProcedure] = src.[ExecutionProcedure]
		,tgt.[Active] = src.[Active]	

	WHEN NOT MATCHED THEN 
		INSERT 
			(
				[DatabaseId]
			   ,[LoadGroup]
			   ,[ExecutionOrder]
			   ,[Phase]
			   ,[CommandType]
			   ,[CommandText]
			   ,[ExecutionProcedure]
			   ,[SourceSchemaSuffix]
			   ,[TargetSchemaSuffix]
			   ,[ItemNameToExecute]
			   ,[GenericTargetFileFormat]
			   ,[SynapseTargetFileFormat]
			   ,[Active]
			)
		VALUES
		  (
		    src.[DatabaseId]
           ,src.[LoadGroup]
           ,src.[ExecutionOrder]
           ,src.[Phase]
           ,src.[CommandType]
           ,src.[CommandText]
           ,src.[ExecutionProcedure]
           ,src.[SourceSchemaSuffix]
           ,src.[TargetSchemaSuffix]
           ,src.[ItemNameToExecute]
           ,src.[GenericTargetFileFormat]
           ,src.[SynapseTargetFileFormat]
           ,src.[Active]
		  );
END;