### Serveur Web

##### ❓ Lister les ports en écoute sur la machine

```powershell
[taiga@web ~]$ sudo ss -lnpt | grep nginx
LISTEN 0      511          0.0.0.0:80        0.0.0.0:*    users:(("nginx",pid=1447,fd=6),("nginx",pid=1446,fd=6))
LISTEN 0      511             [::]:80           [::]:*    users:(("nginx",pid=1447,fd=7),("nginx",pid=1446,fd=7))
```


##### ❓ Ouvrir le port dans le firewall de la machine

```powershell
[taiga@web ~]$ sudo firewall-cmd --permanent --add-port=80/tcp
[sudo] password for taiga: 
Warning: ALREADY_ENABLED: 80:tcp
success
[taiga@web ~]$ sudo firewall-cmd --reload
success
```

##### ❓ Vérifier que ça a pris effet

```powershell
[taiga@client1 ~]$ ping sitedefou.tp7.b1
PING sitedefou.tp7.b1 (10.7.1.11) 56(84) bytes of data.
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=1 ttl=64 time=1.52 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=2 ttl=64 time=1.49 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=3 ttl=64 time=1.17 ms
64 bytes from sitedefou.tp7.b1 (10.7.1.11): icmp_seq=4 ttl=64 time=1.41 ms
^C
--- sitedefou.tp7.b1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 1.165/1.394/1.515/0.137 ms
```

```powershell
[taiga@client1 ~]$ curl sitedefou.tp7.b1
meow !
```

##### ❓ Capture tcp_http.pcap

[tcp_http.pcap](tcp_http.pcap)

##### ❓ Voir la connexion établie

```powershell
[taiga@client1 ~]$ ss  -tpn | grep 10.7.1.11
ESTAB 0      0         10.7.1.101:50206    10.7.1.11:80    users:(("curl",pid=6814,fd=5))
```


##### ❓ 

```powershell
[taiga@web ~]$ sudo ss -lnpt | grep 443
LISTEN 0      511        10.7.1.11:443       0.0.0.0:*    users:(("nginx",pid=1649,fd=6),("nginx",pid=1648,fd=6))
```

##### ❓ Lister les ports en écoute sur la machine

```powershell

```


##### ❓ Gérer le firewall

```powershell
[taiga@web ~]$ sudo firewall-cmd --permanent --remove-port=80/tcp
success
[taiga@web ~]$ sudo firewall-cmd --permanent --remove-port=80/udp
success
[taiga@web ~]$ sudo firewall-cmd --permanent --add-port=433/tcp
success
[taiga@web ~]$ sudo firewall-cmd --permanent --add-port=433/udp
success
[taiga@web ~]$ sudo firewall-cmd --reload
success
```


##### ❓ Capture tcp_https.pcap

[tcp_https.pcap](tcp_https.pcap)

### Serveur VPN

##### ❓ Prouvez que vous avez bien une nouvelle carte réseau wg0

```powershell
[taiga@vpn ~]$ ip a
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e0:05:e4 brd ff:ff:ff:ff:ff:ff
    inet 10.7.1.111/24 brd 10.7.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee0:5e4/64 scope link
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:48:36:fc brd ff:ff:ff:ff:ff:ff
    inet 10.7.2.111/24 brd 10.7.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe48:36fc/64 scope link
       valid_lft forever preferred_lft forever
4: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none
    inet 10.7.200.1/24 scope global wg0
       valid_lft forever preferred_lft forever
```
##### ❓ Déterminer sur quel port écoute Wireguard

```powershell
[taiga@vpn ~]$ sudo ss -lnpu | grep 51820
UNCONN 0      0            0.0.0.0:51820      0.0.0.0:*
UNCONN 0      0               [::]:51820         [::]:*
```
##### ❓ Ouvrez ce port dans le firewall

```powershell
[taiga@vpn ~]$ sudo sysctl -w net.ipv4.ip_forward=1
net.ipv4.ip_forward = 1
[taiga@vpn ~]$ sudo sysctl -w net.ipv6.conf.all.forwarding=1
net.ipv6.conf.all.forwarding = 1
[taiga@vpn ~]$ sudo firewall-cmd --add-interface=wg0 --zone=public --permanent
success
[taiga@vpn ~]$ sudo firewall-cmd --add-masquerade --permanent
Warning: ALREADY_ENABLED: masquerade
success
[taiga@vpn ~]$ sudo firewall-cmd --permanent --add-port=51820/udp
success
[taiga@vpn ~]$ sudo firewall-cmd --reload
success
```
##### ❓  Ping ping ping !

```powershell
[taiga@client1 ~]$ ping 10.7.200.1
PING 10.7.200.1 (10.7.200.1) 56(84) bytes of data.
64 bytes from 10.7.200.1: icmp_seq=1 ttl=64 time=2.51 ms
64 bytes from 10.7.200.1: icmp_seq=2 ttl=64 time=2.78 ms
64 bytes from 10.7.200.1: icmp_seq=3 ttl=64 time=3.05 ms
^C
--- 10.7.200.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 2.511/2.779/3.046/0.218 ms
```
##### ❓ Capture ping1_vpn.pcap

[ping1_vpn.pcap](ping1_vpn.pcap)

##### ❓ Capture ping2_vpn.pcap

[ping2_vpn.pcap](ping2_vpn.pcap)

##### ❓ Prouvez que vous avez toujours un accès internet

```powershell
[taiga@client1 ~]$ traceroute 1.1.1.1
traceroute to 1.1.1.1 (1.1.1.1), 30 hops max, 60 byte packets
 1  _gateway (10.7.200.1)  3.395 ms  5.221 ms  4.019 ms
 2  * * *
 3  10.0.3.2 (10.0.3.2)  27.036 ms  27.032 ms  34.647 ms
 4  10.0.3.2 (10.0.3.2)  47.454 ms  44.293 ms  51.323 ms
```

##### ❓ Visitez le service Web à travers le VPN

```powershell
[taiga@client1 ~]$ curl -k https://sitedefou.tp7.b1
meow !
[taiga@client1 ~]$ traceroute 10.7.200.37
traceroute to 10.7.200.37 (10.7.200.37), 30 hops max, 60 byte packets
 1  _gateway (10.7.200.1)  7.956 ms  7.219 ms  6.095 ms
 2  sitedefou.tp7.b1 (10.7.200.37)  16.473 ms !X  22.704 ms !X  25.458 ms !X
```
