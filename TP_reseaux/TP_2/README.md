

##### ❓ Prouvez que votre configuration est effective
```powershell
PS C:\Windows\system32> Get-NetIPAddress -InterfaceAlias "Ethernet"


IPAddress         : fe80::88d:e69e:5cc7:10db%8
InterfaceIndex    : 8
InterfaceAlias    : Ethernet
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Preferred
ValidLifetime     :
PreferredLifetime :
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 10.255.255.100
InterfaceIndex    : 8
InterfaceAlias    : Ethernet
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 24
PrefixOrigin      : Manual
SuffixOrigin      : Manual
AddressState      : Preferred
ValidLifetime     :
PreferredLifetime :
SkipAsSource      : False
PolicyStore       : ActiveStore
```



##### ❓ Tester que votre LAN + votre adressage IP est fonctionnel
```powershell
PS C:\Windows\system32> ping 10.255.255.200

Envoi d’une requête 'Ping'  10.255.255.200 avec 32 octets de données :
Réponse de 10.255.255.200 : octets=32 temps=3 ms TTL=128
Réponse de 10.255.255.200 : octets=32 temps=3 ms TTL=128
Réponse de 10.255.255.200 : octets=32 temps=2 ms TTL=128
Réponse de 10.255.255.200 : octets=32 temps=3 ms TTL=128

Statistiques Ping pour 10.255.255.200:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 2ms, Maximum = 3ms, Moyenne = 2ms
```
##### ❓ Capture de ping

[ping.pcap](ping.pcap)

##### ❓ Sur le PC serveur
```powershell
PS C:\Users\enzob\Desktop\entcat> .\nc.exe -l -p 12345
```

##### ❓ Sur le PC serveur toujours
```powershell
PS C:\Windows\system32> netstat -a -b -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    0.0.0.0:12345          0.0.0.0:0              LISTENING
 [nc.exe]
```


##### ❓ Sur le PC client

```powershell
PS C:\Windows\system32> netstat -a -b -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    10.255.255.100:62276   10.255.255.200:9999    ESTABLISHED
 [nc.exe]
```

##### ❓ Echangez-vous des messages


```powershell
PS C:\Users\enzob\Desktop\entcat> .\nc.exe -l -p 12345

hello
oui
comment va ?
trkl et toi ?
super nickel
```


##### ❓ Utilisez une commande qui permet de voir la connexion en cours

```powershell
PS C:\Windows\system32> netstat -a -b -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    0.0.0.0:12345          0.0.0.0:0              LISTENING
 [nc.exe]
 
  TCP    10.255.255.100:12345   10.255.255.200:7620    ESTABLISHED
 [nc.exe]
```

[netcat1.pcap](netcat1.pcap)


##### ❓  Inversez les rôles

- Fait juste avant dans le TP le TP !

[netcat2.pcap](netcat2.pcap)


##### ❓  Utilisez Wireshark pour capturer du trafic HTTP

[http.pcap](http.pcap)


##### ❓  Pour les 5 applications


[Satisfactory - Service 1](service1-Satisfactory.pcap)

```powershell
PS C:\Windows\system32> netstat -a -b -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    10.33.78.125:62781     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62782     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62783     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62784     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62785     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62786     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62787     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62788     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62789     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62790     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62791     188.114.96.7:80        ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  TCP    10.33.78.125:62792     54.159.219.218:443     ESTABLISHED
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50503          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50504          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50505          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50506          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50507          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50508          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50509          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50510          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50511          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50512          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50513          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50514          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50515          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50516          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50517          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50518          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50519          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50520          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50522          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50523          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50524          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50525          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50526          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
  UDP    0.0.0.0:50527          *:*
 [FactoryGameSteam-Win64-Shipping.exe]
 
```

[Discord - Service 3](service3-Discord.pcap)

```powershell
PS C:\Windows\system32> netstat -a -b -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    10.33.78.125:62513     35.186.224.45:443      ESTABLISHED
 [Discord.exe]
  TCP    10.33.78.125:62514     162.159.135.234:443    ESTABLISHED
 [Discord.exe]
 
```


[Factorio - Service 3](service4-Factorio.pcap)

Port local dans ce cas là.

```powershell
PS C:\Windows\system32> netstat -a -b -n | Select-String factorio -Context 1,0

    TCP    127.0.0.1:63608        127.0.0.1:63609        ESTABLISHED
>  [factorio.exe]
    TCP    127.0.0.1:63609        127.0.0.1:63608        ESTABLISHED
>  [factorio.exe]
    TCP    127.0.0.1:63610        127.0.0.1:63611        ESTABLISHED
>  [factorio.exe]
    TCP    127.0.0.1:63611        127.0.0.1:63610        ESTABLISHED
>  [factorio.exe]
```

[Chrome - Service 4](service4-Chrome.pcap)

```powershell
PS C:\Windows\system32> netstat -a -b -n | Select-String chrome -Context 1,0

    TCP    10.33.78.125:64127     140.82.112.26:443      ESTABLISHED
>  [chrome.exe]
    TCP    10.33.78.125:64160     108.177.15.188:5228    ESTABLISHED
>  [chrome.exe]
    UDP    0.0.0.0:5353           *:*
>  [chrome.exe]
    UDP    0.0.0.0:5353           *:*
>  [chrome.exe]
    UDP    0.0.0.0:5353           *:*
>  [chrome.exe]
    UDP    0.0.0.0:5353           *:*
>  [chrome.exe]
    UDP    [::]:5353              *:*
>  [chrome.exe]
    UDP    [::]:5353              *:*
>  [chrome.exe]
```


[Steam - Service 5](service5-Steam.pcap)

```powershell
PS C:\Windows\system32> netstat -a -b -n | Select-String steam -Context 1,0

    TCP    0.0.0.0:27036          0.0.0.0:0              LISTENING
>  [steam.exe]
    TCP    10.33.78.125:62582     155.133.248.42:443     ESTABLISHED
>  [steam.exe]
    TCP    127.0.0.1:27060        0.0.0.0:0              LISTENING
>  [steam.exe]
    TCP    127.0.0.1:58662        0.0.0.0:0              LISTENING
>  [steam.exe]
    TCP    127.0.0.1:58662        127.0.0.1:60241        ESTABLISHED
>  [steam.exe]
    TCP    127.0.0.1:58667        0.0.0.0:0              LISTENING
>  [steam.exe]
    TCP    127.0.0.1:58667        127.0.0.1:60240        ESTABLISHED
>  [steam.exe]
    TCP    127.0.0.1:60240        127.0.0.1:58667        ESTABLISHED
>  [steamwebhelper.exe]
    TCP    127.0.0.1:60241        127.0.0.1:58662        ESTABLISHED
>  [steamwebhelper.exe]
    UDP    0.0.0.0:27036          *:*
>  [steam.exe]
```