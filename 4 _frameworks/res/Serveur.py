#!/usr/bin/env python
# Coding: utf-8

# Externe
from os         import listdir, path
from random     import randrange
from time       import sleep
from socket     import *
from select     import *
# Interne
from res.Map        import *
from res.settings   import *


########## CLASSE SERVEUR ##########
class Serveur:
    """
        Objet permettant de gérer toute une partie de roboc.
    """

    def __init__(self):
        self._map = Map( obtenir_map(dossier_maps) )
        """Carte du labyrinthe avec laquelle on interagis tout au long de la partie"""
        self.clients_connectes = []
        """Liste des clients connectés au serveur"""
        self.position_clients = []
        """Liste dela position des clients"""
        self.joueur_courant = None
        """Indice du joueur courant"""
        self.connexion = init_connexion()
        """self.connexion principale du serveur"""

        print(self._map) # DEBUG premier affichage
        self.attente_joueur()
        self._initialiser_labyrinthe()


    def jouer(self):
        """
            Demande au joueur quel déplacement il souhaite effectuer
            et renvoie s'il a gagné ou non
        """
        # On assigne le joueur suivant ne tant que joueur courant
        self.joueur_courant = (self.joueur_courant + 1) % len(self.clients_connectes)

        self._send_map()
        type_, lg = self._receive_action()
        lig_j_courant, col_j_courant = self.position_clients[self.joueur_courant]
        self.position_clients[self.joueur_courant] = self._map.deplacement(type_, lg, lig_j_courant, col_j_courant)

        return etat_jeu(self._map.__str__())

    def terminer(self):
        """Message de sortie pour le joueur, selon qu'il ait gagné ou non"""
        #ToDo : indiquer au joueur gagnant qu'il a gagné et fermer toutes les connexions
        print("Fermeture des connexions")
        for client in self.clients_connectes:
            try:
                client.close()
            except:
                pass

        self.connexion.close()
        exit(0)

    def attente_joueur(self):
        self.connexion.listen(5)
        print("On attends les clients")

        partie_commencee = False
        while not partie_commencee:
            # On va vérifier que de nouveaux clients ne demandent pas à se connecter
            connexions_demandees, wlist, xlist = select([self.connexion], [], [], 0.05)

            # On ajoute les sockets connectés à la liste des clients et on lui donne son ID
            for con in connexions_demandees:
                connexion_avec_client, infos_connexion = con.accept()
                # Envoi de l'ID
                id_joueur = str(len(self.clients_connectes))
                connexion_avec_client.send( str.encode(id_joueur) )
                # On prévient les autres joueurs
                prevenir_joueur(self.clients_connectes)
                # Ajout
                self.clients_connectes.append(connexion_avec_client)

            # Maintenant, on écoute la liste des clients connectés
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select(self.clients_connectes, [], [], 0.05)
            except:
                pass

            for client in clients_a_lire:
                # Réception du message

                try:
                    msg_recu = client.recv(1024).decode()
                except (ConnectionResetError, ConnectionAbortedError):
                    print("Un joueur est parti, veuillez redémarrer le serveur.")
                    self.terminer()

                if controler_partie_commencee(msg_recu):
                    partie_commencee = True
                    prevenir_partie_commence(self.clients_connectes)

    def prevenir_joueur_partie_gagne():
        pass

    def _initialiser_labyrinthe(self):
        """
            Positionne les joueurs sur la map.
            Détermine qui sera le premier joueur.
        """
        # Positionne tous les joueurs
        for joueur in self.clients_connectes:
            ligne, colonne = self._map.set_joueur()
            self.position_clients.append( (ligne, colonne) )

        # Détermine le premier joueur
        self.joueur_courant = randrange( 0, len(self.clients_connectes) )

    def _receive_action(self):
        while True:
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select(self.clients_connectes, [], [], 0.05)
            except error:
                pass

            for client in clients_a_lire:
                # Réception du message

                try:
                    msg_recu = client.recv(1024).decode()
                except (ConnectionResetError, ConnectionAbortedError):
                    print("Un joueur est parti, veuillez redémarrer le serveur.")
                    self.terminer()

                donnees = controler_entree_client(msg_recu,self.joueur_courant)

                if donnees == None:
                    continue

                return donnees

    def _send_map(self):
       for i, client in enumerate(self.clients_connectes):
            map_joueur = self._map.get_map_joueur_courant( *self.position_clients[i] )
            to_send = "Id:{}:Map:{}".format( self.joueur_courant, map_joueur )
            msg_recu = client.send(to_send.encode())

########## FONCTIONS SERVEUR ##########


def init_connexion():
    connexion = socket(AF_INET, SOCK_STREAM)
    connexion.bind((hote, port))

    return connexion

def prevenir_partie_commence(clients_connectes):
    for client in clients_connectes:
        client.send(b"Msg:La partie commence !")

def prevenir_joueur(clients_connectes):
    nb = len(clients_connectes) - 1
    msg = "{} autres joueurs".format(nb)

    for client in clients_connectes:
        client.send(str.encode(msg))


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


########## FONCTIONS SERVEUR ##########


def etat_jeu(map_): # ToDo : Déplacer Map
    """
        Retourne False si le jeu n'est pas gagné et True s'il est gagné.

        Le robot doit remplacer la sortie lors de son dernier mouvement
        pour que cette méthode fonctionne correctement.
    """

    # Pour chacune des lignes...
    for row, i in enumerate(map_):
        # ...on cherche l'indice de la colonne...
        try:

            column = i.index(representation['sortie'])

            # ...si on trouve la sortie, le joueur n'a pas encore gagné
            return False
        # ...si la sortie n'est pas encore trouvé, on continue la recherche...
        except ValueError:
            continue

    # ...si on arrive ici, c'est que la sortie n'a pas été trouvée et que le joueur a gagné
    return True

########## CONTROLES ##########


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
    print(msg_recu) # DEBUG
    parse = msg_recu.split(":")

    try:
        if int(parse[1]) == joueur_courant:
            _type = parse[3]
            longueur = parse[5]

            return _type, int(longueur)
    except:
        raise
        #return None