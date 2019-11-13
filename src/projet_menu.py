import collections

fichier_connexion = "/home//hashe/python/projet/connexion.log"
fichier_utilisateurs = "/home/hashe/python/projet/utilisateurs.txt"
fichier_warning = "/home/hashe/python/projet/warning.txt"
fichier_suspect = "/home/hashe/python/projet/suspect.txt"
fichier_inter = "/home/hashe/python/projet/inter.txt"

list_user = [] # liste contenant les donnée a traité

list_heure = [] # la liste des heures

list_suspect = {}
list_ip = []



consigne ="""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%//&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.......,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&..........,,*************************,,,,,,,,,,,,,****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............*%%%%%%%%%%%%%%%%%%%%%%%%%%,,,,,,,,,,*****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/..............,,,,,,%%%%%%%%%%%%%%%%%%%%%,,,,,,,,,,******(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...............,,,,,,,,,,,,,,,,,*****///(((####%%%%%%#*****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...............,,,,,,,,,,%%%%%%%%%%%%%%%%%%%%%%%%*,,********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............,,,,,,,,,%%%%%%%%%%%%%%%%#,,,,,,,,,,,********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............,,,,,,/%%%%%%%%%%%/,,,,/%%,,,,,,,,,,,********(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@............,,,,%%%%%%%%/,,,,(%%%%%%%%/,,,,,,,,,,,********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..........,%%%%%/,,,,#%%%%%%%%%%%%%%(,,,,,,,,,,,,********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.......%(.,,,#%%%%%%%%%####((///*,,,,,,,,,,,,,,,********@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.......,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,******@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,,,,,,,,,,,,,,,,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




Bonjour, bienvenue sur notre utilitaire du parfait cyber analyste.
Avec cette utilitaire vous pourrais :

1 : créez un fichier utilisateurs.txt ou se trouverons la liste de tout les utilisateurs connecter
2 : Afficher tout les utilisateurs connecter en dehors des horaires de fonctionnement de notre service.
3 : Créez un fichier ou se trouverons la liste des utilisateurs suspect identifier par nos services.
0 : pour quitter


Que choissez vous? """
choix = int(input(consigne))

while choix != 0 :
    if choix == 1 :

        with open(fichier_connexion, "r") as u :
            with open(fichier_utilisateurs, 'w') as i :
                for uuser in u :
                    list_user = uuser.split(";") # création de la liste (tableau) et séparation des donnée IP Login et Date/heure 
                    i.write(list_user[1] + '\n') # Ecriture de la liste de login extrait dans le fichier utilisateurs.txt
        print("""
        
        
Votre fichier utilisateurs.txt a était créer.
        
Merci d'avoir choisis nos service.""")
        choix = 4

    elif choix == 2 :
        with open(fichier_connexion, 'r') as t :
            print('\n\n\nVoici tout les utilisateurs connecter hors des horraires de fonctionnement de nos services :\n')
            for tlog in t :
                list_heure = tlog.split(" ") # Création d'une nouvelle liste séparant l'heure du reste
                if list_heure[1] <= str('08:00') or list_heure[1] >= str('19:00') : # Création de la condition définissant la plage horaire de travail
                    print(list_heure)
        choix = 4

    elif choix == 3 :
        print("""Votre fichier suspect.txt contenant la liste des utilisateurs connecter avec
des adresse ip reconnue compromise, ainsi que le nombre de leur connection.
        
        
Merci d'avoir utiliser nos services.""")

        with open(fichier_warning, "r") as w :
            for wuser in w :
                list_ip.append(wuser.strip()) # création de ma liste d'ip suspect

            with open(fichier_connexion, "r") as susp :
                with open(fichier_inter, "w") as inter :
                    for muser in susp :
                        list_user = muser.split(";") # Création du tableau des log
                        if list_user[0] in list_ip : # Je compare les IP du tableau log a la liste des ip suspect
                            inter.write(list_user[1] + '\n') # Je crée un fichier intermediaire.

        with open(fichier_inter, "r") as suspect :
            for suser in suspect :
                suser = suser.strip() # création de la liste des utilisateur suspect netoyez de tout caractere d'expace superflux
                list_suspect[suser] = list_suspect.get(suser, 0) +1 # création de la bibliotheque list_suspect avec atribuetion d'une valeur 0 par defaut et +1 a chaque nouvelle occurence d'une clef

        list_suspect = collections.OrderedDict(sorted(list_suspect.items())) # Ici on ordonne la bibliothéque comme un dictionnaire et on crée les paire de donnée clef + valeur

        with open(fichier_suspect, "w") as p :
            for key, value in list_suspect.items() : #créatoin de la boucle contenant les valeur de pair
                p.write(key + ";" + str(value) + '\n') # écriture et mise en page de chaque boucle de pair.
        choix = 4
    elif choix == float :
        print("""
        
Commande incorrecte""")
        choix = int(input(consigne))
    
    elif choix == complex :
        print("""
        
Commande incorrectte""")
        choix = int(input(consigne))
    else :
        print("""
        
Commande incorrecte""")
        choix = int(input(consigne))