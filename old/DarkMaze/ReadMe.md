ReadMe.md du jeu de labyrinthe DarkMaze (ou Roboc) pour OpenClassRooms

# Avant propos :

La règle étant sujette à discussion, j'ai choisi de ne pas accepter des déplacements sur plusieures case d'un coup, déplacements gérés au tour par tour.
Cette fonction pourrait être ajoutée facilement.

L'utilisation d'une interface graphique étant demandée, j'ai fais le choix d'enlever au joueur la possbilité d'enter les commandes au clavier, tout se fait avec des boutons et des case à cocher.

Il faut lancer le serveur (maze_serveur.py) avant de lancer les client (maze_client.py)

Les données relatives au port de connection se trouvnt dans les fichiers clietns et serveur "data".

On peut activer l'affichage debug en passant à True les variables "DEBUG" dans les fichiers sv_data.py et cl_data.py.
Les fonction Data.printd() pour le serveur et printd() pour le client sont des fonctions filles de print() et utilisent la variable DEBUG. 


*** Le script a été développé sous linux, comme indiqué dans le cours openclassroom, les échanges de caractères accentués peuvent posés des soucis sous un terminal windows non configuré en utf-8. ***

# Les fonctions écrites :
	* Affichage utilisateur
	* Echanges entre client et serveur
	* gestion du jeu par le serveur
	* mouvement avec controle anti collision des murs et des robots
	* Murer une porte
	* Creuser un mur

# Ce qui n'a pas été fait :
	* les tests unitaires

# Evolutions possibles :
L'utilisation de trigramme lors d'envoi de messages entre lient t serveur permet d'ajouter simplement de nouvelles fonctionnalités.

# Le serveur :

## La cinétique du serveur :
	* Demande de choisir un labyrinthe
	* Lance le serveur
	* Accepte des nouvelles connexions et cré les robots sur la grille
	* Lance la partie avec 1 seul thread : écoute et réponse aux clients

## Caractéristiques des clients :
	Ils sont stockés dans une liste de clients sous la forme d'une liste de données définis comme suit :
		0 les donnees de connexions socket()
		1 le pseudo du joueur str()
		2 un booleen pour savoir si le joueur est encore connecté 
		3 la coordonnée x du joueur int()
		4 la coordonnee y du joueur int()
		5 un booleen pour savoir si le joueur est sur une porte
	La liste peut s'agrandir au besoin. (gestion de clef pour l'ouverture d'une porte)

## Caractéristiques de clients_connectes :
Il s'agit d'une liste ne contenant que les infos de connexion des joueurs, dans l'ordre de leur 1 ere connexion.
				

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
	* MSG : à ajouter pour un futur chat

### Messages en réception au client :
	* INI : La partie est prête à démarrer, en attente d'un retour client
	* STR : La partie démarre, donne la liste des joueurs
	* WTU : Début du tour pour le joueur cité ie : WTUJoueur1
	* ETU : Fin du tour de "pseudonyme si précisé", sinon du joueur.
	* MSG : Message
	* GRI : grille du labyrinthe
	* WIN : Indique le pseudonyme du gagnant, si non définit c'est que le joueur est gagnant
