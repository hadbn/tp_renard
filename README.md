Ce tp a pour objectif d'écrire un autre jeu, en s'inspirant de ce qui a été fait pour Snake.
Le jeu se joue sur une grille dont certaines cases sont des pièges que vous (le lapin) avez laissé.
Le joueur (un lapin) est représenté par une unique case, et peut se déplacer sur tout le plateau.

Des renards apparaissent régulièrement sur le plateau et ont pour objectif de manger le joueur. Les prédateurs se déplacent donc toujours vers le joueur (à la vitesse d'une case par pas de temps).

Si un renard passe sur un piège, il tombe dedans.

La partie se finit si un renard vous rattrape, ou si vous tombez dans un de vos pièges.

Le but est de capturer le plus de renards.

En utilisant pygame et en repartant de la structure du code du snake, implémentez ce jeu.

Il vous faudra créer une classe lapin, une classe renard, et une classe piège.

Commencez par lister dans le readme les attributs et méthodes de chaque classes (en détaillant les input et output des méthodes).

Implémentez ensuite le jeu.

Liste des classes :
Rabbit(Animal) :
- attribut : x,y, nombre de piège restant, nombre de capture
- méthode : déplacement (input : un des veceurs direction : [1,0],[0,1],[-1,0],[0,-1] , output : None) (modification sur place de la pisition)

Fox(Animal) : 
- attribut : x,y
- méthode : déplacement (input : un des veceurs direction : [1,0],[0,1],[-1,0],[0,-1])

Foxes:
-move()
-has_eaten

Piege : 
-attribut : liste_position

Animal : 
-attribut : is_fallen
-method : draw()