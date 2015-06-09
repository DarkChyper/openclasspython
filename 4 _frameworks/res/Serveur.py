#!/usr/bin/env python
# Coding: utf-8

# Externe
from os         import listdir, path
from random     import randrange
from time       import sleep
from socket     import *
from select     import *
from time       import sleep
# Interne
from res.Map        import *
from res.settings   import *


########## CLASSE SERVEUR ##########
class Serveur:
    """
        Classe gérant entièrement la partie serveur.
        1. Attends les joueurs et le signale de démarrage
        2. Écoute tous les messages des joueurs et filtre
           ne faire jouer que le bon joueur
    """

    def __init__(self):
        self._map = Map( obtenir_map(dossier_maps) )
        """Carte du labyrinthe avec laquelle on interagis tout au long de la partie"""
        self.joueur_courant = None
        """Indice du joueur courant"""
        self.connexion = init_connexion()
        """self.connexion principale du serveur"""

        self.attente_joueur()
        self.definir_premier_joueur()

    def jouer(self):
        """
            Méthode principale permettant de faire jouer au tour par tour
            les joueurs
        """
        # On assigne le joueur suivant en tant que joueur courant
        self.joueur_courant = (self.joueur_courant + 1) % self._map.nb_joueurs

        # On envoie la map à tous les joueurs
        self._map.maj_carte_joueurs(self.joueur_courant)

        # On réceptionne la prochaine action
        type_ = self._receive_action()

        # Tant que le déplacement est incorrect, on continue
        while True:
            try:
                self._map.action(type_, self.joueur_courant)
            # Si le mouvement est impossible...
            except IndexError:
                # ...on prévient le joueur et on récupère une nouvelle action
                self._map.obtenir_joueur(self.joueur_courant).envoi_message_client("Msg", "Déplacement impossible")
                type_ = self._receive_action()
            else:
                break

        return self._map.etat_jeu()

    def terminer(self, msg):
        """
            Ferme le serveur proprement en prévenant tous les clients
            avec un message personnalisé facultatif
        """

        if len(msg) != 0:
            self._map.prevenir_joueurs("Msg", msg)

        self._map.fermer_connexions()
        exit(0)

    def attente_joueur(self):
        """
            Toutes les 0.05 secondes, accepte les connexions
            et vérifie si un joueur n'a pas demandé que la partie commence

        """
        self.connexion.listen(5)
        print("On attends les clients")

        partie_commencee = False
        while not partie_commencee:
            # On va vérifier que de nouveaux clients ne demandent pas à se connecter
            connexions_demandees, wlist, xlist = select([self.connexion], [], [], 0.05)

            # On ajoute les sockets connectés à la liste des clients et on lui donne son ID
            for con in connexions_demandees:
                connexion_avec_client, infos_connexion = con.accept()

                # On ajoute le joueur
                self._map.ajouter_joueur(connexion_avec_client)

                # On prévient les autres joueurs
                sleep(2)
                msg = "{} autres joueurs\nAppuyez sur c pour commencer !".format(self._map.nb_joueurs - 1)
                self._map.prevenir_joueurs("Msg", msg)

                # On vérifie qu'il n'y a pas le maximum de joueurs (4)
                partie_commencee = self._map.nb_joueurs > nb_max_joueurs - 1
                if partie_commencee:
                    sleep(1)
                    self._map.prevenir_joueurs("Msg", "La partie commence !\nAttendez votre tour")

            # Maintenant, on écoute la liste des clients connectés
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select(self._map.sockets, [], [], 0.05)
            except:
                pass

            for client in clients_a_lire:
                # Réception du message

                try:
                    msg_recu = client.recv(1024).decode()
                except (ConnectionResetError, ConnectionAbortedError):
                    print("Un joueur est parti, veuillez redémarrer le serveur.")
                    self.terminer("Un joueur est parti ou\nle serveur rencontre un problème.\nVous pouvez quitter")

                if controler_partie_commencee(msg_recu):
                    partie_commencee = True
                    self._map.prevenir_joueurs("Msg", "La partie commence !")

    def definir_premier_joueur(self):
        self.joueur_courant = randrange(0, self._map.nb_joueurs)

    def prevenir_joueur_partie_gagne(self):
        """
            Prévient les joueurs qu'un joueur a gagné
            et prévient le joueur gagnant, qu'il a gagné
        """
        self._map.maj_carte_joueurs(self.joueur_courant)
        # On prévient tous les joueurs que la partie est gagné
        self._map.prevenir_joueurs("Msg","Un autre joueur a gagné\nla partie.\nVous pouvez quitter.")
        # On prévient le joueur gagnant que c'est lui le gagnant
        sleep(0.5)
        self._map.obtenir_joueur(self.joueur_courant).envoi_message_client("Msg","Vous avez gagné !\nVous pouvez quitter.")

        self.terminer("")

    def _receive_action(self):
        """
            Attends de recevoir une action correcte du joueur courant
        """

        while True:
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select(self._map.sockets, [], [], 0.05)
            except:
                pass

            for client in clients_a_lire:
                # Réception du message
                try:
                    msg_recu = client.recv(1024).decode()
                # Si un des client est parti
                except (ConnectionResetError, ConnectionAbortedError):
                    print("Un joueur est parti, veuillez redémarrer le serveur.")
                    self.terminer("Un joueur est parti ou\nle serveur rencontre un problème.\nVous pouvez quitter")

                type_ = controler_entree_client(msg_recu, self.joueur_courant)

                if type_ == None:
                    continue

                return type_


########## FONCTIONS SERVEUR ##########


def init_connexion():
    """
        Initialisation de la connexion du serveur
    """
    connexion = socket(AF_INET, SOCK_STREAM)
    connexion.bind((hote, port))

    return connexion


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
        Contrôle si le message reçu provient bien du joueur courant et
        qu'elles sont au bon format (balise et données)
        Les données sont du format suivant :
        Id:1:Type:e
    """

    parse = msg_recu.split(":")

    try:
        # On contrôle que les balises sont bien présente
        if  not parse[0] == "Id" and not parse[2] == "Type":
            raise ValueError("Balises incorrectes, message : \"{}\"".format(msg_recu))

        # On contrôle que les données sont au bon format et qu'elle viennent du bon joueur
        if int(parse[1]) == joueur_courant:
            _type = parse[3]
        else:
            raise ValueError("Réception d'un client qui n'est pas le joueur courant, message : \"{}\"".format(msg_recu))
    except (ValueError, IndexError) as e:
        print("Contenu des balises incorrect, message : \"{}\"".format(msg_recu))
        return None
    except Exception as e:
        print(e.value)
        return None

    return _type