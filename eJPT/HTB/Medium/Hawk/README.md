




```bash

❯ bruteforce-salted-openssl -t q0 -f /usr/share/wordlists/rockyou.txt -c aes-256-cbc -d sha256 .drupal.txt.hack
Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.

Tried passwords: 30
Tried passwords per second: inf
Last tried password: friends

Password candidate: friends




❯ droopescan

    |
 ___| ___  ___  ___  ___  ___  ___  ___  ___  ___
|   )|   )|   )|   )|   )|___)|___ |    |   )|   )
|__/ |    |__/ |__/ |__/ |__   __/ |__  |__/||  /
                    |
                                         v1.33.7

Example invocations: 
  droopescan scan drupal -u URL_HERE
  droopescan scan silverstripe -u URL_HERE

More info: 
  droopescan scan --help
 
Please see the README file for information regarding proxies.

❯ droopescan scan drupal -u http://10.10.10.102
[+] Plugins found:                                                              
    profile http://10.10.10.102/modules/profile/
    php http://10.10.10.102/modules/php/
    image http://10.10.10.102/modules/image/

[+] Themes found:
    seven http://10.10.10.102/themes/seven/
    garland http://10.10.10.102/themes/garland/

[+] Possible version(s):
    7.58

[+] Possible interesting urls found:
    Default changelog file - http://10.10.10.102/CHANGELOG.txt
    Default admin - http://10.10.10.102/user/login

[+] Scan finished (0:03:15.108819 elapsed)


$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupal',
      'password' => 'drupal4hawk',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);

```


