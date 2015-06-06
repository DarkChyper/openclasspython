#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
from select         import *
from os            import listdir,path
# Interne
from res.settings   import *


########## RECUPÉRATION MAP ##########


def obtenir_liste_maps(dossier):
    """
        Retourne une liste de nom de maps
    """

    nom_maps = []

    # On charge le nom des cartes existantes
    for i, nom_fichier in enumerate(listdir(dossier)):
        if nom_fichier.endswith(".txt"):
            chemin = path.join("cartes", nom_fichier)
            nom_maps.append( nom_fichier[:-4].lower() )

    return nom_maps

def demander_map(nom_maps):
    """
        Demande au joueur quelle map il souhaite choisir
    """

    # On affiche la liste des labyrinthes disponibles
    map_msg = "Labyrinthes existants : "
    print(map_msg)

    # On affiche les choix possibles
    for i, nom in enumerate(nom_maps):
        print(" {} - {}".format(i + 1, nom))

    # Tant que l'input est incorrecte...
    indice = None
    while indice not in range(1, len(nom_maps) + 1):
        # ...On demande l'indice du labyrinthe
        try:
            indice = int(input("Entrez un numéro de labyrinthe pour commencer à jouer : "))
        except:
            pass

    return indice - 1

def obtenir_map(dossier):
    """
        Récupère le contenu du fichier de map
        indiqué par l'indice dans le dossier en paramètre.
    """
    nom_maps = obtenir_liste_maps(dossier)
    indice = demander_map(nom_maps)

    nom_fichier = listdir(dossier)[indice]
    chemin = path.join(dossier, nom_fichier)
    with open(chemin, "r") as fichier:
        contenu = fichier.read()

    return contenu


########## SERVEUR ##########


def init_connexion():
    connexion = socket(AF_INET, SOCK_STREAM)
    connexion.bind((hote, port))

    return connexion

def prevenir_partie_commence(clients_connectes):
    for client in clients_connectes:
        client.send(b"Msg:La partie commence !")

def send_map(clients_connectes, _map, joueur_courant):
   for client in clients_connectes:
        # Réception du message
        to_send = "id:{}:map:{}".format( joueur_courant, _map.__str__() )
        msg_recu = client.send(to_send.encode())

def receive_action(clients_connectes, joueur_courant):
        while True:
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select(clients_connectes, [], [], 0.05)
            except error:
                pass

            for client in clients_a_lire:
                # Réception du message

                try:
                    msg_recu = client.recv(1024).decode()
                except (ConnectionResetError, ConnectionAbortedError):
                    print("Un joueur est parti, veuillez redémarrer le serveur.")
                    exit(0)

                donnees = controler_entree_client(msg_recu,joueur_courant)

                if donnees == None:
                    continue

                return donnees

def prevenir_joueur(clients_connectes):
    nb = len(clients_connectes) - 1
    msg = "{} autres joueurs".format(nb)

    for client in clients_connectes:
        client.send(str.encode(msg))


########## CONTROLE UTILISATEUR ##########


def controler_partie_commencee(msg_recu):
    """
        Contrôle si le message reçu est "c"
    """
    # Si aucune longueur n'est indiquée ou égale à 0
    if msg_recu == 'c':
        print("c!")
        return True
    return False

def controler_entree_client(msg_recu, joueur_courant):
    """
        Contrôle si le message reçu provient bien du joueur courant
        Les données sont du format suivant :
        id:1:type:e:lg:3
    """
    parse = msg_recu.split(":")

    try:
        if int(parse[1]) == joueur_courant:
            _type = parse[3]
            longueur = parse[5]

            return _type, longueur
    except:
        return None


########## CLIENT ##########


def init_connexion_serveur():
    """
        Initialise la connexion du client au serveur
    """

    print("On tente de se connecter au serveur...")
    try:
        connexion = socket(AF_INET, SOCK_STREAM)
        connexion.connect((hote, port))
    except ConnectionError:
        print("Connexion au serveur impossible")
    else:
        print("Connexion établie avec le serveur.")

    return connexion

def obtenir_id(connexion, msg):
    """
        Permet d'obtenir l'ID sous forme d'entier
    """

    id_ = None
    try:
        id_ = int(msg)
    except:
        print("Récupération de l'ID impossible")
        connexion.close()
        exit(1)

    print("Bienvenue, joueur {}.".format(id_ + 1))

    return id_

def traiter_message(msg_recu, id_):
    """
        Contrôle si le message reçu provient bien du joueur courant
        Les données sont du format suivant :
        id:1:type:e:lg:3
    """
    parse = msg_recu.split(":")
    joueur_courant_id = parse[1]
    map_ = parse[3]

    if joueur_courant_id == id_:
        pass
        # ToDo: Passer à Tkinter

def entree_correcte(entree):
    """
        Renvoie le type de déplacement et la longueur
        ou None si l'entrée est incorrecte.
        Si l'utilisateur demande de l'aide, on renvoie entree
    """

    # Si l'utilisateur demande de l'aide, on ne touche à rien
    if entree == touches['aide']:
        afficher_aide()
        return None

    # Si le premier caractère est correct
    if len(entree) != 0 and entree[0] in touches.values():
        type_deplacement = entree[0]

        # Si le reste est un nombre
        try:
            lg = int(entree[1:])
        except:
            # Si aucune longueur n'est indiquée ou égale à 0
            if entree[1:].strip() == '' or entree[1:].strip() == '0':
                lg = 1
                return type_deplacement, lg
        else:
            return type_deplacement, lg

    return None

def afficher_aide(self):
    """
        Affiche toutes les touches possibles
    """
    for c, v in touches.items():
        print( "{} : {}".format(c.title(), v) )