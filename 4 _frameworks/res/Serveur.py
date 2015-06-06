#!/usr/bin/env python
# Coding: utf-8

# Externe
from os         import listdir, path
from random     import randrange
from time       import sleep
# Interne
from res.Map        import *
from res.settings   import *
from res.func       import *

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
        self.initialiser_labyrinthe()


    def jouer(self):
        """
            Demande au joueur quel déplacement il souhaite effectuer
            et renvoie s'il a gagné ou non
        """

        while True:
            send_map(self.clients_connectes, self._map, self.joueur_courant)
            entree = receive_action(self.clients_connectes, self.joueur_courant)
            gagne = self._map.deplacement(*entree)

        return gagne

    def terminer(self):
        """Message de sortie pour le joueur, selon qu'il ait gagné ou non"""
        #ToDo : indiquer au joueur gagnant qu'il a gagné et fermer toutes les connexions
        print("Fermeture des connexions")
        for client in self.clients_connectes:
            client.close()

        self.connexion.close()

######################################################################################################################################################

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
                    print("Un joueur est parti, redémarrer le serveur.")
                    exit(0)

                if controler_partie_commencee(msg_recu):
                    partie_commencee = True
                    prevenir_partie_commence(self.clients_connectes)
                else:
                    client.send(b"Msg:pass !")


    def initialiser_labyrinthe(self):
        """
            Positionne les joueurs sur la map.
            Détermine qui sera le premier joueur.
        """
        ligne = self._map.len_lig()
        colonne = self._map.len_col()

        for joueur in self.clients_connectes:
            pos_ligne = randrange(0,ligne)
            pos_col = randrange(0, colonne)

            while not self._map.est_vide(pos_ligne, pos_col):
                pos_ligne = randrange(0,ligne )
                pos_col = randrange(0, colonne )

            self.position_clients.append( (pos_ligne, pos_col) )

        self.joueur_courant = randrange( 0, len(self.clients_connectes) )