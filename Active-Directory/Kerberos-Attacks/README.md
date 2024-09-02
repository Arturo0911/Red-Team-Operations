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

```
