#!/usr/bin/python3.4
# -*- coding: utf8 -*-

import socket

hote = ''
port = 12800

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind((hote, port))
connexion.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

listenclients = NewClient(connexion)
msgclients = DataExchange()

listenclients.start()
msgclients.start()

#join est bloquant jusqu'à la fermeture es 2 processus
listenclients.join()
msgclients.join()

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
