# Rendu installation server

Pour commencer on ce connecte au serveur

## Connexion au server :

Connection au serveur :
**`ssh** root@wilfart.fr -p 6251`

Le mot de passe est “ root “

## Mise à jour :

Avec “sudo apt update” et “sudo apt upgrade”, je vérifie que tout est à jour.

```
root@debian:~# sudo apt update
Hit:1 http://security.debian.org/debian-security bookworm-security InRelease
Hit:2 http://deb.debian.org/debian bookworm InRelease
Hit:3 http://deb.debian.org/debian bookworm-updates InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
root@debian:~# sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

```

## Installation d’un Firewall :

Pour commencer on vérrifie les ports utilisé :

```
root@debian:~# sudo ss -tulpn
Netid  State   Recv-Q  Send-Q    Local Address:Port     Peer Address:Port  Process
udp    UNCONN  0       0               0.0.0.0:68            0.0.0.0:*      users:(("dhclient",pid=451,fd=7))
tcp    LISTEN  0       128             0.0.0.0:22            0.0.0.0:*      users:(("sshd",pid=473,fd=3))
tcp    LISTEN  0       128                [::]:22               [::]:*      users:(("sshd",pid=473,fd=4))

```

Ici, le port 22, c’est notre ‘ssh’, il faut donc le retenir, et on install le firewall :

```bash
sudo apt update
sudo apt install ufw
```

une fois installer j’autorise le port ssh qui est ‘22’ :

```
root@debian:~# sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)

```

on ajoute des règles globales pour refusé toutes les entrée entrant et autorisé toutes les sortant par défaut:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Je lance mon Firewall

```
root@debian:~# sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup

```

Avec “sudo ufw status verbose”, je vérifie l’état et les autorisations de mon firewall

```
root@debian:~# sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)

```

```
root@debian:~# sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)

```

```
root@debian:~# sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)

```

## Gestion des utilisateurs :

On install les packets !

`root@debian:~# sudo apt-get install libpam-pwquality libpwquality-tools` 

Création d’un utilisateur :

`sudo useradd Utilisateur`

On lui ajoute des règles pour le mdp, en ouvrant :

```

root@debian:~# sudo nano /etc/pam.d/common-password

```

On vas y coller :

```
# here are the per-package modules (the "Primary" block)
# Trois tentatives, 12 caractères minimum
password        requisite                       pam_pwquality.so retry=3 minlen=12
```

L’utilisateur doit utilisé un mdp d’au moins 12 caractères 

On peux maintenant tester :

```
root@debian:/etc/pam.d# passwd Utilisateur
New password:
BAD PASSWORD: The password is shorter than 12 characters
Retype new password:

```

ça marche !

Je lui ajoute :

retry=3 : Donne le droit à 3 essaye 

minlen=12 : Demande une taille de caractères minimum de 12

minclass=3 : Demande au moins 3 caractères spéciaux 

dictdeck=1 : Vérifie dans une liste de mots de passe courant si il n’est pas utilisé 

```
root@debian:/etc/pam.d# grep 'pwquality' *
common-password:password        requisite                       pam_pwquality.so retry=3 minlen=12 minclass=3 d
ictdeck=1

```

Et je teste :

```
root@debian:/etc/pam.d# passwd Utilisateur
New password:
BAD PASSWORD: The password contains less than 3 character classes

```

Je vais utilisé “ 55bEbB!nGxcGErSSk6&dm#gg “ comme mot de passe pour mes testes 

```
root@debian:/etc/pam.d# passwd Utilisateur
New password:
Retype new password:
passwd: password updated successfully

```

Je lui crée tout les paramètres par défault :

```
sudo mkdir -p /home/Utilisateur
sudo chown Utilisateur:Utilisateur /home/Utilisateur
sudo cp -r /etc/skel/. /home/Utilisateur/
sudo usermod -s /bin/bash Utilisateur

```

Je teste de passer sur mon utilisateur en lançant un autre ssh :

```
C:\Users\enzob>ssh Utilisateur@wilfart.fr -p 6251
Utilisateur@wilfart.fr's password: 
Linux debian 6.1.0-28-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.119-1 (2024-11-22) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Dec 16 15:11:34 2024 from 195.7.117.146
Utilisateur@debian:~$
```

ici ça fonctionne

Je crée mon Admin :
`root@debian:~# sudo adduser admin`

Je lui donne un mdp :

```
root@debian:~# passwd admin
New password:
Retype new password:
passwd: password updated successfully

```

(ici “ 55bEbB!nGxcGErSSk6&dm#gg “ comme l’utilisateur, juste pour le teste)

Je lui donne la possibilité d’utilisé sudo :
`root@debian:~# sudo usermod -aG sudo admin`

Je vérifie qu’il est dedans :

```
root@debian:~# groups admin
admin : admin sudo users
```

Je me connecte et essaye une commande pour vérifier sont fonctionnement

```
root@debian:~# su - admin
admin@debian:~$ sudo apt update
[sudo] password for admin:
Hit:1 http://security.debian.org/debian-security bookworm-security InRelease
Hit:2 http://deb.debian.org/debian bookworm InRelease
Hit:3 http://deb.debian.org/debian bookworm-updates InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.

```

Parfait !

## Sécurisation du SSH :

Nous pouvons commencer par changer le port, mais nous allons pas le faire ici, car notre VM ne serais plus contactable.

Pour commencer on ouvre :

`sudo nano /etc/ssh/sshd_config`

Ici on passe une valeur sur " no “ pour refusé la connexion au SSH par le “ root “ impossible :
`PermitRootLogin no`

et je relance le ssh :

`sudo systemctl restart ssh`

je test :

```
C:\Users\enzob>ssh root@wilfart.fr -p 6251

root@wilfart.fr's password:
Permission denied, please try again.

C:\Users\enzob>ssh admin@wilfart.fr -p 6251

admin@wilfart.fr's password: 
Linux debian 6.1.0-28-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.119-1 (2024-11-22) x86_64

admin@debian:~$
```

Ici ça ne marche pas avec le root, mais cela marche avec l’admin, donc parfait !

Je peux toujours le connecter au root si besoin :

```
admin@debian:~$ su - root
Password:
root@debian:~#
```

## Fail2Ban et notifications :

### `fail2ban` : Protection contre les attaques brute-force

1. Installez `fail2ban` :
    
    `root@debian:~# sudo apt install fail2ban -y` 
    
2. Configurez `fail2ban` pour SSH :
    - Éditez `/etc/fail2ban/jail.local` et ajoutez :
        
        ```bash
        [sshd]
        enabled = true
        port = ssh
        logpath = /var/log/secure
        maxretry = 5
        
        # durée du ban ( 1minute )
        bantime  = 1m
        ```
        
3. Démarrez et activez le service :
    
    `sudo systemctl enable fail2ban
    sudo systemctl start fail2ban`
    
    ```
    root@debian:~# sudo systemctl enable fail2ban
    Synchronizing state of fail2ban.service with SysV service script with /lib/systemd/systemd-sysv-install.
    
    root@debian:~# sudo systemctl start fail2ban
    
    Executing: /lib/systemd/systemd-sysv-install enable fail2ban
    
    ```
    
4. Vérifiez les IP bannies :
    
    `sudo fail2ban-client status sshd`
    

## Logs :

<Fait mais pas encore décrit ici>

## Bonnes pratiques de sécurité :

1. Mises à jour régulières :
    - Mettez à jour le système :
        
        `sudo apt update -y`
        
        `sudo apt upgrade -y`
        
2. Limiter les sudoers :
    - Configurez `/etc/sudoers` pour restreindre les utilisateurs.
3. Désactiver les services inutilisés :
    - Listez les services actifs :
        
        `sudo systemctl list-units --type=service`
        
    - Désactivez un service :
        
        `sudo systemctl disable <service>`
        

## Installation de Nginx :

Nous pouvons pour l’instant lancer un premier service,

installation de Nginx :
`root@debian:~# sudo apt install nginx` 

## Bonus : Connexion Stylé (juste car c’est stylé)

Ici on vas modifié le message de bienvenue SSH, car j’ai envie.

J’ouvre 

`root@debian:~# sudo nano /etc/ssh/bienvenue.msg`

et j’écrit ce que je veux :

```
$$\   $$\
$$$\  $$ |
$$$$\ $$ | $$$$$$\   $$$$$$\  $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$$\
$$ $$\$$ | \____$$\ $$  __$$\ \____$$\ $$  _____|$$  __$$\ $$  _____|
$$ \$$$$ | $$$$$$$ |$$ |  \__|$$$$$$$ |$$ /      $$ /  $$ |\$$$$$$\
$$ |\$$$ |$$  __$$ |$$ |     $$  __$$ |$$ |      $$ |  $$ | \____$$\
$$ | \$$ |\$$$$$$$ |$$ |     \$$$$$$$ |\$$$$$$$\ \$$$$$$  |$$$$$$$  |
\__|  \__| \_______|\__|      \_______| \_______| \______/ \_______/
```

On ouvre : 
`sudo nano /etc/ssh/sshd_config`

Ajoute la ligne :
`Banner /etc/ssh/bienvenue.msg`

et on relance le SSH :
`sudo service ssh reload`

Ont test, ettttttttttt :

```
C:\Users\enzob>ssh root@wilfart.fr -p 6251
$$\   $$\
$$$\  $$ |
$$$$\ $$ | $$$$$$\   $$$$$$\  $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$$\
$$ $$\$$ | \____$$\ $$  __$$\ \____$$\ $$  _____|$$  __$$\ $$  _____|
$$ \$$$$ | $$$$$$$ |$$ |  \__|$$$$$$$ |$$ /      $$ /  $$ |\$$$$$$\
$$ |\$$$ |$$  __$$ |$$ |     $$  __$$ |$$ |      $$ |  $$ | \____$$\
$$ | \$$ |\$$$$$$$ |$$ |     \$$$$$$$ |\$$$$$$$\ \$$$$$$  |$$$$$$$  |
\__|  \__| \_______|\__|      \_______| \_______| \______/ \_______/

                                     $$$$$$$\  $$$$$$\   $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\
                                    $$  _____|$$  __$$\ $$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\
                                    \$$$$$$\  $$$$$$$$ |$$ |  \__|\$$\$$  / $$$$$$$$ |$$ |  \__|
                                     \____$$\ $$   ____|$$ |       \$$$  /  $$   ____|$$ |
                                    $$$$$$$  |\$$$$$$$\ $$ |        \$  /   \$$$$$$$\ $$ |
                                    \_______/  \_______|\__|         \_/     \_______|\__|

root@wilfart.fr's password:

```

TADA !!!