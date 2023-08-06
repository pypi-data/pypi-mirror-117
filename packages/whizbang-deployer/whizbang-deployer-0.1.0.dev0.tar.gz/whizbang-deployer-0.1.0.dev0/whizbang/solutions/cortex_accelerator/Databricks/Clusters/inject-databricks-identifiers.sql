--==================================================================
-- Inject databrick identifiers (cluster & pool ids) in a sql table
--==================================================================

PRINT '   -> Injecting databricks identifiers (cluster & pool ids)...'

CREATE TABLE #StagedDatabricksIdentifiers
(
       [Type] int NOT NULL,
       [Name] varchar(100) NOT NULL,
       Identifier varchar(100) NOT NULL
)

IF (LEN('#{POOLLOOKUP_H16STANDARDPOOL}#') <> 0)
BEGIN 
    PRINT '   -> H16StandardPool, #{POOLLOOKUP_H16STANDARDPOOL}#'
    INSERT INTO #StagedDatabricksIdentifiers
    VALUES (2, 'H16StandardPool', '#{POOLLOOKUP_H16STANDARDPOOL}#')
END

IF (LEN('#{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#') <> 0)
BEGIN 
    PRINT '   -> DataEngineering-Interactive, #{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#'
    INSERT INTO #StagedDatabricksIdentifiers
    VALUES (1, 'DataEngineering-Interactive', '#{CLUSTERLOOKUP_DATAENGINEERINGINTERACTIVE}#')
END

IF (LEN('#{CLUSTERLOOKUP_CTXINTERACTIVE}#') <> 0)
BEGIN 
    PRINT '   -> CTX-Interactive, #{CLUSTERLOOKUP_CTXINTERACTIVE}#'
    INSERT INTO #StagedDatabricksIdentifiers
    VALUES (1, 'CTX-Interactive', '#{CLUSTERLOOKUP_CTXINTERACTIVE}#')
END


MERGE state_config.DatabricksIdentifiers AS [Target]
USING  #StagedDatabricksIdentifiers AS [Source] 
ON [Target].[Type] = [Source].[Type]
       AND [Target].[Name] = [Source].[Name]
WHEN MATCHED THEN
  UPDATE SET [Target].Identifier = [Source].Identifier, [Target].updatedDateUtc = GetUtcDate()
WHEN NOT MATCHED THEN
  INSERT ([Type], [Name], Identifier) VALUES ([Source].[Type], [Source].[Name],[Source].Identifier);

DROP TABLE #StagedDatabricksIdentifiers

SELECT * FROM state_config.DatabricksIdentifiers