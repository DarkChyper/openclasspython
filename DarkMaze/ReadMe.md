ReadMe.md du jeu de labyrinthe DarkMaze (ou Roboc) pour OpenClassRooms

# Avant propos :

# Les fonctions écrites :

# Les fonctions non écrites :
	* Murer une porte
	* Creuser une porte
	* Tests

# Le serveur :

	## La cinétique du serveur :
		* Demande de choisir un labyrinthe
		* Lance le serveur
		* Accepte des nouvelles connexions et cré les robots sur la grille
		* Lance la partie avec 1 seul thread : écoute des clients
			

# Le client :

	## La cinétique du client:

		* Demande de pseudoyme au joueur
		* Connexion au sereur de jeu
		* Lancement des 3 threads de la partie :
			* Interface graphique
			* Ecoute du serveur
			* Discussion avec le serveur

	## Définition des messages :

		### Messages en émission du client :
			* PSD : translission du Pseudonyme du joueur au serveur
			* INI : Demande de début de partie par le joueur
			* MVT : Tentative de mouvement du joueur (envoi de N, S, E, O)
			* MUR : Tentative de murage d'une porte  (envoi de MN, MS, ME, MO)
			* CRE : Tentative de creusage d'un mur pour en faire une porte (envoi de CN, CS, CE, CO)
			* EXI : fin de la partie pour le joueur et déconnexion côté serveur

		### Messages en réception au client :
			* INI : La partie est prête à démarrer, en attente d'un retour client
			* STR : La partie démarre, donne la liste des joueurs
			* UTU : Début du tour pour le joueur
			* OTU : Début du tour du joueur "pseudonyme" (message recu : "OTUpseudonyme")
			* ETU : Fin du tour de "pseudonyme si précisé", sinon du joueur.
			* MSG : Message
			* GRI : grille du labyrinthe
			* WIN : Indique le pseudonyme du gagnant, si non définit c'est que le joueur est gagnant
