## Usage HTB

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-21 01:43 -05

❯ rm nmap/Allports
rm: remove write-protected regular empty file 'nmap/Allports'? y
❯ tree
.
├── content
├── exploit
├── nmap
└── README.md

4 directories, 1 file
❯ sudo nmap -p- --open --min-rate=10000 -T4 -sS -n -Pn -vvv 10.10.11.18 -oG nmap/Allports
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-21 01:44 -05
Initiating SYN Stealth Scan at 01:44
Scanning 10.10.11.18 [65535 ports]
Discovered open port 80/tcp on 10.10.11.18
Discovered open port 22/tcp on 10.10.11.18
Completed SYN Stealth Scan at 01:44, 7.19s elapsed (65535 total ports)
Nmap scan report for 10.10.11.18
Host is up, received user-set (0.19s latency).
Scanned at 2024-11-21 01:44:06 -05 for 8s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 7.29 seconds
           Raw packets sent: 68198 (3.001MB) | Rcvd: 67216 (2.689MB)