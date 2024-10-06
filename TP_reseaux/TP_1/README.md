# I. Récolte d'informations


##### ❓ Adresses IP de ta machine

- affiche l'adresse IP que ta machine a sur sa carte réseau WiFi

```powershell
Carte réseau sans fil Wi-Fi :
    Adresse IPv4: 10.33.78.125
```

- affiche l'adresse IP que ta machine a sur sa carte réseau ethernet

```powershell
Carte Ethernet Ethernet :
    Adresse IPv4: 10.33.78.XX
```
*câble déconnecter*


##### ❓Si t'as un accès internet normal, d'autres infos sont forcément dispos...


- adresse passerelle : 10.33.79.254
- serveur DNS : 10.33.79.254
- serveur DHCP : 10.33.79.254

##### ❓Envoie un ping vers...

- toi-même !
```powershell
PS C:\Users\enzob> ping 127.0.0.1

Envoi d’une requête 'Ping'  127.0.0.1 avec 32 octets de données :
Réponse de 127.0.0.1 : octets=32 temps<1ms TTL=128
Réponse de 127.0.0.1 : octets=32 temps<1ms TTL=128
Réponse de 127.0.0.1 : octets=32 temps<1ms TTL=128
Réponse de 127.0.0.1 : octets=32 temps<1ms TTL=128

Statistiques Ping pour 127.0.0.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 0ms, Maximum = 0ms, Moyenne = 0ms
```


##### ❓On continue avec ping. Envoie un ping vers...

- ta passerelle
```powershell
PS C:\Users\enzob> ping 10.33.79.254

Envoi d’une requête 'Ping'  10.33.79.254 avec 32 octets de données :
Délai d’attente de la demande dépassé.

Statistiques Ping pour 10.33.79.254:
    Paquets : envoyés = 1, reçus = 0, perdus = 1 (perte 100%),
```
*Ne fonctionne pas à Ynov*

- un(e) pote sur le réseau
```powershell
PS C:\Users\enzob> ping 10.33.78.124

Envoi d’une requête 'Ping'  10.33.78.124 avec 32 octets de données :
Réponse de 10.33.78.124 : octets=32 temps=552 ms TTL=64
Réponse de 10.33.78.124 : octets=32 temps=9 ms TTL=64
Réponse de 10.33.78.124 : octets=32 temps=72 ms TTL=64
Réponse de 10.33.78.124 : octets=32 temps=76 ms TTL=64

Statistiques Ping pour 10.33.78.124:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 9ms, Maximum = 552ms, Moyenne = 177ms
```

- un site internet
```powershell
PS C:\Users\enzob> ping 10.33.79.254

Envoi d’une requête 'Ping'  10.33.79.254 avec 32 octets de données :
Délai d’attente de la demande dépassé.

Statistiques Ping pour 10.33.79.254:
    Paquets : envoyés = 1, reçus = 0, perdus = 1 (perte 100%),
```
*Ne fonctionne pas à Ynov*

\
##### ❓Faire une requête DNS à la main

Ping de www.thinkerview.com
```powershell
ping www.thinkerview.com

Envoi d’une requête 'ping' sur www.thinkerview.com [188.114.97.7] avec 32 octets de données :
Réponse de 188.114.97.7 : octets=32 temps=18 ms TTL=55
Réponse de 188.114.97.7 : octets=32 temps=18 ms TTL=55
Réponse de 188.114.97.7 : octets=32 temps=20 ms TTL=55
Réponse de 188.114.97.7 : octets=32 temps=18 ms TTL=55

Statistiques Ping pour 188.114.97.7:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 18ms, Maximum = 20ms, Moyenne = 18ms
```
Ping de www.wikileaks.org
```powershell
 ping www.wikileaks.org

Envoi d’une requête 'ping' sur wikileaks.org [51.159.197.136] avec 32 octets de données :
Réponse de 51.159.197.136 : octets=32 temps=11 ms TTL=54
Réponse de 51.159.197.136 : octets=32 temps=10 ms TTL=54
Réponse de 51.159.197.136 : octets=32 temps=11 ms TTL=54
Réponse de 51.159.197.136 : octets=32 temps=11 ms TTL=54

Statistiques Ping pour 51.159.197.136:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 10ms, Maximum = 11ms, Moyenne = 10ms
```

Ping de www.torproject.org
```powershell
 ping www.torproject.org

Envoi d’une requête 'ping' sur www.torproject.org [204.8.99.144] avec 32 octets de données :
Réponse de 204.8.99.144 : octets=32 temps=115 ms TTL=50
Réponse de 204.8.99.144 : octets=32 temps=114 ms TTL=50
Réponse de 204.8.99.144 : octets=32 temps=119 ms TTL=50
Réponse de 204.8.99.144 : octets=32 temps=114 ms TTL=50

Statistiques Ping pour 204.8.99.144:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 114ms, Maximum = 119ms, Moyenne = 115ms
```


##### ❓Effectue un scan du réseau auquel tu es connecté

###### <span style="color:red;">CHANGEMENT DE RESEAU ENTRE LES TEST !</span>
Information du réseau :
    - Adresse réseau : 192.168.1.0
    - Masque du réseau : 255.255.255.0
    - Routeur FAI : 192.168.1.254

```powershell
PS C:\Windows\system32> nmap -sn -PR 192.168.1.0/24

Starting Nmap 7.95 ( https://nmap.org ) at 2024-10-06 16:59 Paris, Madrid (heure dÆÚtÚ)
Nmap scan report for 192.168.1.50
Host is up (0.074s latency).
MAC Address: 10:5A:17:██:A6:0C (██████ ████████)
Nmap scan report for 192.168.1.84
Host is up (0.075s latency).
MAC Address: B0:2A:43:16:2B:BB (Google)
Nmap scan report for 192.168.1.96
Host is up (0.28s latency).
MAC Address: D4:D2:D6:██:0B:2E (███████████████████████)
Nmap scan report for 192.168.1.98
Host is up (0.28s latency).
MAC Address: B4:FB:E3:██:7A:41 (██████████ (China))
Nmap scan report for 192.168.1.132
Host is up (0.44s latency).
MAC Address: E4:F0:42:7A:22:E2 (Google)
Nmap scan report for 192.168.1.154
Host is up (0.73s latency).
MAC Address: 84:0D:8E:██:D6:6D (███████████)
Nmap scan report for 192.168.1.180
Host is up (0.041s latency).
MAC Address: 20:66:CF:██:67:23 (Freebox SAS)
Nmap scan report for 192.168.1.184
Host is up (0.40s latency).
MAC Address: 20:DF:B9:91:ED:6B (Google)
Nmap scan report for 192.168.1.185
Host is up (0.0090s latency).
MAC Address: B8:27:EB:██:D8:60 (███████████)
Nmap scan report for 192.168.1.187
Host is up (0.40s latency).
MAC Address: A4:77:33:AF:C9:03 (Google)
Nmap scan report for 192.168.1.254
Host is up (0.0090s latency).
MAC Address: 20:66:CF:██:24:A3 (Freebox SAS)
Nmap scan report for 192.168.1.88
Host is up.
Nmap done: 256 IP addresses (12 hosts up) scanned in 9.47 seconds
PS C:\Windows\system32>
```


##### ❓Changer d'adresse IP

Je sais que l'adresse ```192.168.222``` est disponlible, je vais donc l'utilisé !

```powershell
PS C:\Windows\system32> ipconfig

Configuration IP de Windows

Carte Ethernet Ethernet 2 :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::37a:5c14:2221:ccab%5
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.56.1
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . :

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6. . . . . . . . . . . . . .: 2a01:e0a:bae:be60:8544:d700:3fa6:7b9c
   Adresse IPv6 temporaire . . . . . . . .: 2a01:e0a:bae:be60:89d2:c8c7:6a44:448f
   Adresse IPv6 de liaison locale. . . . .: fe80::d106:7b93:2d6f:1a4c%14
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.1.222
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . : fe80::2266:cfff:fe66:24a3%14
                                       192.168.1.254
```