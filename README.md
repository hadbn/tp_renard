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

LISTE DES CLASSES 
Classe Lapin : 
Attributs :
    x : Position X 
    y : Position Y 
    couleur


Méthodes :
    __init__(self, x_depart, y_depart)

    deplacer(self, direction, largeur_grille, hauteur_grille)
        Output : Met à jour x et y

    dessiner(self, surface, taille_case)`
        Output : Dessine le lapin

Classe Renard
Attributs :
    x : Position X
    y : Position Y
    couleur

Méthodes :
    __init__(self, x_depart, y_depart)

    traquer(self, lapin_x, lapin_y)
    Output : Modifie x et y pour se rapprocher du lapin

    dessiner(self, surface, taille_case)
    Output : Dessine le renard sur l'écran.

Classe Piege
Attributs :
   x : Position X
   y : Position Y
   couleur

**Méthodes :**
    __init__(self, x_pos, y_pos)
    dessiner(self, surface, taille_case)
    Output : dessine le piège