
# Linux Privilege Escalation

```bash

ps aux | grep root

find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null


hackthurpc@ubuntu:/$ find . -type f -exec grep  -H -i "^htb" {} \;
./usr/lib/python3/dist-packages/certifi/cacert.pem:HTBsROopN4WSaGa8gzj+ezku01DwH/teYLappvonQfGbGHLy9YR0SslnxFSuSGTf
./usr/lib/int-check.sh:HTB{Th15_tH3_fL4G}
Binary file ./usr/lib/modules/5.4.0-148-generic/kernel/net/sched/sch_htb.ko matches
Binary file ./usr/lib/modules/5.4.0-148-generic/kernel/drivers/net/ethernet/cisco/enic/enic.ko matches
Binary file ./usr/lib/modules/5.4.0-148-generic/kernel/drivers/scsi/qla2xxx/qla2xxx.ko matches
<snip>
hackthurpc@ubuntu:/$ 

hackthurpc@ubuntu:/$ lastlog
Username         Port     From             Latest
root                                       Thu Jan  1 00:00:10 +0000 1970
daemon                                     **Never logged in**
bin                                        **Never logged in**
sys                                        **Never logged in**
sync                                       **Never logged in**
games                                      **Never logged in**
man                                        **Never logged in**
lp                                         **Never logged in**
mail                                       **Never logged in**
news                                       **Never logged in**
uucp                                       **Never logged in**
proxy                                      **Never logged in**
www-data                                   **Never logged in**
backup                                     **Never logged in**
list                                       **Never logged in**
irc                                        **Never logged in**
gnats                                      **Never logged in**
nobody                                     **Never logged in**
systemd-network                            **Never logged in**
systemd-resolve                            **Never logged in**
systemd-timesync                           **Never logged in**
messagebus                                 **Never logged in**
syslog                                     **Never logged in**
_apt                                       **Never logged in**
tss                                        **Never logged in**
uuidd                                      **Never logged in**
tcpdump                                    **Never logged in**
landscape                                  **Never logged in**
pollinate                                  **Never logged in**
usbmux                                     **Never logged in**
sshd                                       **Never logged in**
systemd-coredump                           **Never logged in**
lab_adm                                    **Never logged in**
lxd                                        **Never logged in**
hackthurpc      pts/0    10.10.15.235     Sun Mar 16 05:56:00 +0000 2025


```