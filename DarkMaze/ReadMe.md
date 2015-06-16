ReadMe.md du jeu de labyrinthe DarkMaze (ou Roboc) pour OpenClassRooms

# Avant propos :

La gestion de l'affichage graphine n'est pa correcte et provoque un runtimerror lors de la fermeture de la fenêtre, même avec la fonction quit().
La solution serait de travailler avec une file d'attente, ce qui sera fait plus tard.

La règle étant sujette à discussion, j'ai choisi de ne pas accepter des déplacement sur plusieures case d'un coup, déplacements gérés au tour par tour.
Cette fonction pourrait être ajoutée facielement.

# Les fonctions écrites :
	* Affichage utilisateur
	* Echanges entre client et serveur
	* gestion du jeu par le serveur

# Ce qui n'a pas été fait :
	* Murer une porte
	* Creuser une porte
	* les tests unitaires

# Evolutions possibles :
## Chat : 
Les bases d'un chat sont posées dans le programme. Il existe déjà un préfixe (MSG) que le serveur peut recevoir pour renvoyer à tout le monde le message.
Un booleen est aussi définit sur le serveur (Partie.joueur) pour déterminer le pseudo a utiliser entre Partie.clientAutre et Partie.clientQuiJoue.
	ie : Si c'est au tour de ClientQuijoue mais que c'est clientAutre qui envoie un message de type MSG contenant "Je suis le meilleurs", 
		 tous les joueurs connectés recevront "pseudo_de_clientAutre : Je suis le meilleurs"

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
	La liste peut s'agrandir au besoin. (exemple gestion d'un déplacement sur )

## Caractéristiques de clients_connectes :

				

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
