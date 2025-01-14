# TP perso (LINUX)

changer nom utilisateur

sudo `hostnamectl set-hostname Superviseur`

redémarrer le système :
sudo `invoke-rc.d hostname.sh restart`

### Mise en place du serveur DHCP

Mise à jour du PC

`sudo apt-get update`

Installation du packet :

`sudo apt-get install isc-dhcp-server`

On fait un “ip a” pour récupéré le nom de l’interface réseau 

```bash
taiga@Superviseur:~$ ip a
1: lo:  mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3:  mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:4d:22:91 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 86275sec preferred_lft 86275sec
    inet6 fe80::9297:f589:c2f9:d5e8/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: enp0s8:  mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e2:2a:30 brd ff:ff:ff:ff:ff:ff
    inet 10.10.1.1/16 brd 10.10.255.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::e823:9e75:bdf1:c435/64 scope link noprefixroute
       valid_lft forever preferred_lft forever

```

Pour nous c’est “enp0s8”.

On édit la configuration avec 

`sudo nano /etc/default/isc-dhcp-server`

on retire le # de “DHCPDv4_CONF=/etc/dhcp/dhcpd.conf” 

et ajoutons le nom de notre interface à 

`INTERFACESv4=""`

ce qui donne 

`INTERFACESv4="`enp0s8`"`

on enregistre et quitte

on ouvre “`/etc/dhcp/dhcpd.conf`"

`sudo nano /etc/dhcp/dhcpd.conf`

et on déclare une étendue DHCP :

```bash
# Déclaration d'une étendue DHCP
subnet 10.10.0.0 netmask 255.255.0.0 {
        # Plage d'adresses IP à distribuer
        range   10.10.2.1 10.10.2.200;
        # Serveur(s) DNS à distribuer
        option domain-name-servers 1.1.1.1;
        # Passerelle par défaut
        option routers 10.10.1.1;
}
```

On enregistre et restart le service :

`sudo systemctl restart isc-dhcp-server.service`

### mise en place du routeur :

sudo nano /etc/sysctl.conf

ajout de : “net.ipv4.ip_forward = 1”

Installation d’Iptables :
**`taiga@debian**:**~**$ sudo apt-get install iptables` 

Activation du NAT :

iptables -t nat -A POSTROUTING -o <NOM DU RESEAU> -j MASQUERADE

Pour nous :
**`taiga@debian**:**~**$ sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE`

## Installation de MeshCentral (et nodejs)

On installe NodeJS :

`sudo apt install -y nodejs npm`

Maintenant que NodeJS est installer, nous pouvons lancer le programme :

`sudo npm install meshcentral`

Une fois installer, plus qu’à le lancer ! :

`sudo node /usr/local/lib/node_modules/meshcentral`

Maintenant on ce rend sur la page web, en entrant l’adresse ip de notre serveur

![image.png](image.png)

et on crée un utilisateur qui seras automatiquement Admin :

user : admin

mdp : 383838

![image.png](image%201.png)

On vas créer un nouveaux groupe :

![image.png](image%202.png)

Et ajouter un agent avec cette commande :

```bash
sudo wget ("https://10.10.1.1/meshagents?script=1" --no-check-certificate -O ./meshinstall.sh || wget "https://10.10.1.1/meshagents?script=1" --no-proxy --no-check-certificate -O ./meshinstall.sh) && chmod 755 ./meshinstall.sh && sudo -E ./meshinstall.sh https://10.10.1.1 'oFWem6OllUic3z$ui59@fXev8IGzGEZ2iJ5V1uPANPamwswkmwy1ry5Hsgn2x1Xy' || ./meshinstall.sh https://10.10.1.1 'oFWem6OllUic3z$ui59@fXev8IGzGEZ2iJ5V1uPANPamwswkmwy1ry5Hsgn2x1Xy'
```

C’est parfait ! Vos ordinateurs apparait et peuvent être contrôler !

![image.png](image%203.png)

![image.png](image%204.png)