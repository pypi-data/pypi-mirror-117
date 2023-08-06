/********************************************************************************************************************/
--STEP 1: CREATE A CREDENTIAL

-- A: Create a Database Master Key.
-- Only necessary if one does not already exist.
-- Required to encrypt the credential secret in the next step.

IF NOT EXISTS (SELECT 1 FROM sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##')
	CREATE MASTER KEY ENCRYPTION BY PASSWORD = '{{adwmasterkey}}'; /*** CHANGE ***/
GO


-- B (for service principal authentication): Create a database scoped credential
-- IDENTITY: Pass the client id and OAuth 2.0 Token Endpoint taken from your Azure Active Directory Application
-- SECRET: Provide your AAD Application Service Principal key.

--CREATE DATABASE SCOPED CREDENTIAL ADLSCredential
--WITH
--    -- Always use the OAuth 2.0 authorization endpoint (v1)
--    IDENTITY = '<client_id>@<OAuth_2.0_Token_EndPoint>',
--    SECRET = '<key>'
--;

-- B (for Gen2 storage key authentication): Create a database scoped credential
-- IDENTITY: Provide any string, it is not used for authentication to Azure storage.
-- SECRET: Provide your Azure storage account key.

IF EXISTS (SELECT 1 FROM sys.database_scoped_credentials WHERE [name] = 'AzureStorageCredential')
       DROP DATABASE SCOPED CREDENTIAL AzureStorageCredential
GO

CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredential
WITH IDENTITY = 'Managed Identity'


-- CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredential
-- WITH
--        IDENTITY = 'MyIdentity',
--        SECRET = 'secret'; /*** CHANGE ***/

-- It should look something like this when authenticating using service principal:
--CREATE DATABASE SCOPED CREDENTIAL ADLSCredential
--WITH
--    IDENTITY = '536540b4-4239-45fe-b9a3-629f97591c0c@https://login.microsoftonline.com/42f988bf-85f1-41af-91ab-2d2cd011da47/oauth2/token',
--    SECRET = 'BjdIlmtKp4Fpyh9hIvr8HJlUida/seM5kQ3EpLAmeDI='
--;

/********************************************************************************************************************/
--STEP 2: CREATE DATA FACTORY CREDENTIALS

-- Create data factory sql login credentials
--Currently being set in the 'Create-Master-Credentials-Script...revisit.
--CREATE LOGIN [datafactory] WITH PASSWORD = 'hi_mom1!';   /**** MUST BE DONE IN MASTER ****/

CREATE USER [datafactory] FOR LOGIN datafactory;

EXEC sp_addrolemember N'db_owner', N'datafactory';

/*
Check user roles:
SELECT DP1.name AS DatabaseRoleName,
   isnull (DP2.name, 'No members') AS DatabaseUserName
 FROM sys.database_role_members AS DRM
 RIGHT OUTER JOIN sys.database_principals AS DP1
   ON DRM.role_principal_id = DP1.principal_id
 LEFT OUTER JOIN sys.database_principals AS DP2
   ON DRM.member_principal_id = DP2.principal_id
WHERE DP1.type = 'R'
ORDER BY DP1.name;
*/


/********************************************************************************************************************/
-- STEP 3: CREATE EXTERNAL DATA SOURCE

IF EXISTS (SELECT 1 FROM sys.external_data_sources WHERE NAME = 'AzureDataLakeStore')
       DROP EXTERNAL DATA SOURCE [AzureDataLakeStore]
GO

-- Parameterize LOCATION
/******************** Replace "ncuaapdl" from line below with name of ADL storage account ********************/
CREATE EXTERNAL DATA SOURCE [AzureDataLakeStore] WITH (TYPE = HADOOP, LOCATION = N'abfss://adls@{{ncuaapdl}}.dfs.core.windows.net' , CREDENTIAL = [AzureStorageCredential])
GO

/********************************************************************************************************************/

-- STEP 5: CREATE EXTERNAL FILE FORMATS

IF EXISTS (SELECT 1 FROM sys.external_file_formats where [name] = 'T_07_0E_1_DT27_F_UTF8_NONE_EFF')
       DROP EXTERNAL FILE FORMAT [T_07_0E_1_DT27_F_UTF8_NONE_EFF]
GO

CREATE EXTERNAL FILE FORMAT [T_07_0E_1_DT27_F_UTF8_NONE_EFF] WITH (FORMAT_TYPE = DELIMITEDTEXT, FORMAT_OPTIONS (FIELD_TERMINATOR = N'0x07', STRING_DELIMITER = N'0x0e', DATE_FORMAT = N'yyyy-MM-dd HH:mm:ss.fffffff', USE_TYPE_DEFAULT = False))
GO

IF EXISTS (SELECT 1 FROM sys.external_file_formats where [name] = 'ORC_Default')
       DROP EXTERNAL FILE FORMAT [ORC_Default]
GO

CREATE EXTERNAL FILE FORMAT [ORC_Default] WITH (FORMAT_TYPE = ORC, DATA_COMPRESSION = N'org.apache.hadoop.io.compress.DefaultCodec')
GO

IF EXISTS (SELECT 1 FROM sys.external_file_formats where [name] = 'ORC_Snappy')
       DROP EXTERNAL FILE FORMAT [ORC_Snappy]
GO

CREATE EXTERNAL FILE FORMAT [ORC_Snappy] WITH (FORMAT_TYPE = ORC, DATA_COMPRESSION = N'org.apache.hadoop.io.compress.SnappyCodec')
GO

IF EXISTS (SELECT 1 FROM sys.external_file_formats where [name] = 'ParquetFile_GZip')
       DROP EXTERNAL FILE FORMAT [ParquetFile_GZip]
GO

CREATE EXTERNAL FILE FORMAT [ParquetFile_GZip] WITH (FORMAT_TYPE = PARQUET, DATA_COMPRESSION = N'org.apache.hadoop.io.compress.GzipCodec')
GO

IF EXISTS (SELECT 1 FROM sys.external_file_formats where [name] = 'T_COMMA_DOUBLEQUOTE_2_DT27_F_UTF8_NONE_EFF')
       DROP EXTERNAL FILE FORMAT [T_COMMA_DOUBLEQUOTE_2_DT27_F_UTF8_NONE_EFF]
GO

CREATE EXTERNAL FILE FORMAT [T_COMMA_DOUBLEQUOTE_2_DT27_F_UTF8_NONE_EFF] WITH (FORMAT_TYPE = DELIMITEDTEXT, FORMAT_OPTIONS (FIELD_TERMINATOR = N',', STRING_DELIMITER = N'"', USE_TYPE_DEFAULT = False))
GO