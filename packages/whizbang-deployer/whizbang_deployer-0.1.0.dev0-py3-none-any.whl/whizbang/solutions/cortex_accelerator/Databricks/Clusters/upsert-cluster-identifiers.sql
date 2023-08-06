--==================================================================
-- Upsert databricks cluster ids in [state_config].[DatabricksClusterLookup]
--==================================================================
PRINT '   -> Executing on server [' + @@servername + ']'
PRINT '   -> Upserting databricks cluster ids in [state_config].[DatabricksClusterLookup]...'

CREATE TABLE #StagedClusterIds
(
       [Name] varchar(100) NOT NULL,
       Identifier varchar(100) NOT NULL
)

IF (LEN('#{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#') <> 0)
BEGIN
    PRINT '   -> DataEngineering-Interactive, #{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#'
    INSERT INTO #StagedClusterIds
    VALUES ('DataEngineering-Interactive', '#{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#')
END

IF (LEN('#{CLUSTERLOOKUP_CTXINTERACTIVE}#') <> 0)
BEGIN
    PRINT '   -> CTX-Interactive, #{CLUSTERLOOKUP_CTXINTERACTIVE}#'
    INSERT INTO #StagedClusterIds
    VALUES ('CTX-Interactive', '#{CLUSTERLOOKUP_CTXINTERACTIVE}#')
END


MERGE state_config.DatabricksClusterLookup AS [Target]
USING  #StagedClusterIds AS [Source]
ON [Target].[Name] = [Source].[Name]
WHEN MATCHED THEN
  UPDATE SET [Target].Identifier = [Source].Identifier, [Target].updatedDateUtc = GetUtcDate()
WHEN NOT MATCHED THEN
  INSERT ([Name], Identifier) VALUES ([Source].[Name], [Source].Identifier);

DROP TABLE #StagedClusterIds

SELECT * FROM state_config.DatabricksClusterLookup

PRINT '   -> Complete'
