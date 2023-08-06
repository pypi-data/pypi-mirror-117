CREATE USER [datafactory] FOR LOGIN datafactory;
EXEC sp_addrolemember N'db_datareader', N'datafactory'
EXEC sp_addrolemember N'db_datawriter', N'datafactory'
GRANT CREATE TABLE TO datafactory
GRANT EXECUTE TO datafactory
