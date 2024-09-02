# Abusing ADCS


Active Directory Certificate Services (ADCS) is a server role in Windows Server that allows organizations to build a public key
infraestructure (PKI) to provide users and computers with secure communication channels using digital certificates. These
certificates can be used for various purposes like secure email, web browsing, virtual private network (VPN) connections, and
more. ADCS provides functionalities for issuing, managing, and revoking digital certificates within an Active Directory
environment.



ADCS stores details regarding certification Authrities (CAs) and Certificate Templates within the Lightweight
Directory Access Protocol (LDAP) directory service, which is part of Microsoft's Active Directory. By using LDAP as the
storage mechanism, ADCS integrates seamslesslyu with ACtive Directory, Allowing administrators to manage certificateservices
using familiar tools and interfaces within the Active Directory environment


The configuration Naming Context (CN) in Active Directory holds configuration information about the entire forest,
including information About ADCS. By opeing ADSI,msc and connection to the Configuration Context, adminsitrators can
navigate through the Active Directory configuration and view objects related to ADCS, such as CA configuration settings,
certificate templates and other relevant information.


The sample:

Win + R => adsiedit.msc => connect to => (Configuration) => CN=Services => CN=Public Key Services => CN=Certificate Template

Notice:

Since the Configuratiohn Naming Context (NC) is replicated across all domain controllers within the forest, we canm alter these objects from a child domain as a SYSTEM user in its local replicañ. With the ability to write to these objects, itis possible to create or own Certificate Template which is vulnerable to ESC12 and then
publish it ot the ADCS CA server.

Simplification ADCS attack:

Add a new vulnerable Certificate Template inside the Certificate Templates contaainer as a pKICertificateTemplate object.

Give The Adminstrator user of the child domain Full Control rights over the created Certificatge Template.

Publish teh created Templat eto the CA server by modigying the KIEnrollmentService object of the CA inside the Enrollment Services container.
After the Configuration NC is replicated back to the parent domain, request the certifiacte for the root/Adminstrator from the child domain.




to make a certificate Template Vulnerable to ESC1:
1: Right click on the suer template
2: Select Duplicate Template. This action will open a prompt with the properties of the new template.
3: Set the Subject Name option to supply in the reuqest. This configuration allows for dynamic specification of the subject name during the certificate request process, protentally introducing the ESC1 vulnerability



Request Created Certificate:


```bash
.\Certify.exe request /ca:inlanefreight.ad\INLANEFREIGHT-DC01-CA /domain:inlanefreight.ad /template:"Copy of User" /altname:INLANEFREIGHT\Administrator
```
