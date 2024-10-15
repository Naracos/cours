##### ❓ Uniquement avec des commandes, prouvez-que :

vous avez bien configuré les adresses IP demandées :
- Router
```powershell
[taiga@rooter ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:b3:91:1e brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.254/24 brd 10.5.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:feb3:911e/64 scope link
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:48:36:fc brd ff:ff:ff:ff:ff:ff
    inet 10.0.3.15/24 brd 10.0.3.255 scope global dynamic noprefixroute enp0s8
       valid_lft 86097sec preferred_lft 86097sec
    inet6 fe80::6f90:2e31:f7ac:3aca/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

tout le monde peut se ping au sein du réseau `10.5.1.0/24` :
 - Mon poste
```powershell
PS C:\Users\enzob> ping 10.5.1.11

Envoi d’une requête 'Ping'  10.5.1.11 avec 32 octets de données :
Réponse de 10.5.1.11 : octets=32 temps=1 ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.11 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.11:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 1ms, Moyenne = 0ms
PS C:\Users\enzob> ping 10.5.1.12

Envoi d’une requête 'Ping'  10.5.1.12 avec 32 octets de données :
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.12 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.12:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
PS C:\Users\enzob> ping 10.5.1.254

Envoi d’une requête 'Ping'  10.5.1.254 avec 32 octets de données :
Réponse de 10.5.1.254 : octets=32 temps=1 ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64
Réponse de 10.5.1.254 : octets=32 temps<1ms TTL=64

Statistiques Ping pour 10.5.1.254:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 1ms, Moyenne = 0ms
```

##### ❓ ️ Déjà, prouvez que le routeur a un accès internet

```bash
[taiga@localhost ~]$ ping www.ynov.com
PING www.ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=51 time=56.4 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=2 ttl=51 time=42.2 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=3 ttl=51 time=50.9 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=4 ttl=51 time=48.2 ms
^C
--- www.ynov.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 42.196/49.429/56.423/5.122 ms
```

##### ❓ ️ Activez le routage
```bash
[taiga@localhost ~]$ sudo firewall-cmd --add-masquerade --permanent
[sudo] password for taiga:
success
[taiga@localhost ~]$ sudo firewall-cmd --reload
success
[taiga@localhost ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: yes
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```



















































##### ❓ ️ Prouvez que les clients ont un accès internet

- Client 1 :

```powershell
[taiga@client1 ~]$ ping ynov.com
PING ynov.com (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=1 ttl=53 time=13.9 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=2 ttl=53 time=13.4 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=3 ttl=53 time=15.3 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=4 ttl=53 time=13.4 ms
^C
--- ynov.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3008ms
rtt min/avg/max/mdev = 13.366/13.992/15.315/0.793 ms
```

- Client 2 :

```powershell
[taiga@client2 ~]$ ping naracos.fr
PING naracos.fr (82.65.172.238) 56(84) bytes of data.
64 bytes from 82-65-172-238.subs.proxad.net (82.65.172.238): icmp_seq=1 ttl=62 time=3.75 ms
64 bytes from 82-65-172-238.subs.proxad.net (82.65.172.238): icmp_seq=2 ttl=62 time=3.58 ms
64 bytes from 82-65-172-238.subs.proxad.net (82.65.172.238): icmp_seq=3 ttl=62 time=4.14 ms
64 bytes from 82-65-172-238.subs.proxad.net (82.65.172.238): icmp_seq=4 ttl=62 time=2.45 ms
^C
--- naracos.fr ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3008ms
rtt min/avg/max/mdev = 2.446/3.477/4.137/0.629 ms
```


##### ❓ ️ Montrez-moi le contenu final du fichier de configuration de l'interface réseau

- celui de `client2.tp5.b1` me suffira :
```powershell
[taiga@client2 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s3
DEVICE=enp0s3
NAME=lan

ONBOOT=yes
BOOTPROTO=static

IPADDR=10.5.1.12
NETMASK=255.255.255.0
GATEWAY=10.5.1.254
DNS1=1.1.1.1
```
##### ❓ ️ Sur `routeur.tp5.b1`, déterminer sur quel port écoute le serveur SSH

```powershell
[taiga@client1 ~]$ sudo ss -lnpt | grep 22
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*    users:(("sshd",pid=685,fd=3))
LISTEN 0      128             [::]:22           [::]:*    users:(("sshd",pid=685,fd=4))
```

##### ❓ ️ Sur  `routeur.tp5.b1`, vérifier que ce port est bien ouvert
```powershell
[taiga@client1 ~]$ sudo ss -npt | grep 22
ESTAB 0      0          10.5.1.11:22       10.5.1.1:62796 users:(("sshd",pid=1354,fd=4),("sshd",pid=1350,fd=4))
```

##### ❓ ️  Installez et configurez un serveur DHCP sur la machine `routeur.tp5.b1`

```powershell
[taiga@rooter ~]$ sudo dnf install dhcp-server -y
```

```powershell
[taiga@rooter ~]$ sudo cat /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
default-lease-time 900;
max-lease-time 10800;

authoritative;

subnet 10.5.1.0 netmask 255.255.255.0 {
range 10.5.1.137 10.5.1.237;
option routers 10.5.1.254;
option subnet-mask 255.255.255.0;
option domain-name-servers 1.1.1.1;
}
[taiga@rooter ~]$
```

##### ❓ ️ ️Créez une nouvelle machine client `client3.tp5.b1`
```powershell
[taiga@client3 ~]$ ip a
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:18:1f:35 brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.137/24 brd 10.5.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 651sec preferred_lft 651sec
    inet6 fe80::a00:27ff:fe18:1f35/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

- Accès à internet :
```powershell
[taiga@client3 ~]$ ping google.fr
PING google.fr (172.217.20.195) 56(84) bytes of data.
64 bytes from waw02s08-in-f195.1e100.net (172.217.20.195): icmp_seq=1 ttl=115 time=15.1 ms
64 bytes from waw02s08-in-f195.1e100.net (172.217.20.195): icmp_seq=2 ttl=115 time=12.2 ms
64 bytes from waw02s08-in-f3.1e100.net (172.217.20.195): icmp_seq=3 ttl=115 time=14.6 ms
64 bytes from waw02s08-in-f3.1e100.net (172.217.20.195): icmp_seq=4 ttl=115 time=14.1 ms
^C
--- google.fr ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3008ms
rtt min/avg/max/mdev = 12.193/13.993/15.070/1.092 ms
```

##### ❓ ️Consultez le bail DHCP qui a été créé pour notre client
```powershell
[taiga@rooter ~]$ cat /var/lib/dhcpd/dhcpd.leases
# The format of this file is documented in the dhcpd.leases(5) manual page.
# This lease file was written by isc-dhcp-4.4.2b1

# authoring-byte-order entry is generated, DO NOT DELETE
authoring-byte-order little-endian;

server-duid "\000\001\000\001.\2410(\010\000'H6\374";

lease 10.5.1.137 {
  starts 2 2024/10/15 14:12:23;
  ends 2 2024/10/15 14:27:23;
  cltt 2 2024/10/15 14:12:23;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 08:00:27:18:1f:35;
  uid "\001\010\000'\030\0375";
}
```

##### ❓ Confirmez qu'il s'agit bien de la bonne adresse MAC 
```powershell
[taiga@client3 ~]$ ip a
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:18:1f:35 brd ff:ff:ff:ff:ff:ff
    inet 10.5.1.137/24 brd 10.5.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 795sec preferred_lft 795sec
    inet6 fe80::a00:27ff:fe18:1f35/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```