from random import randint
import pygame as pg


LARGEUR_FENETRE = 800
HAUTEUR_FENETRE = 800
TAILLE_CASE = 20

COLONNES = LARGEUR_FENETRE // TAILLE_CASE
LIGNES = HAUTEUR_FENETRE // TAILLE_CASE

COULEUR_FOND = (30, 150, 50)   
COULEUR_LAPIN = (255, 255, 255) 
COULEUR_RENARD = (220, 80, 0) 
COULEUR_PIEGE = (50, 50, 50)  

class Lapin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.couleur = COULEUR_LAPIN

    def deplacer(self, dx, dy):
        self.x = max(0, min(COLONNES - 1, self.x + dx))    # On empeche le lapin de sortir de la grille de jeu
        self.y = max(0, min(LIGNES - 1, self.y + dy))

    def dessiner(self, surface):
        rect = pg.Rect(self.x * TAILLE_CASE, self.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
        pg.draw.rect(surface, self.couleur, rect)

class Renard:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.couleur = COULEUR_RENARD

    def traquer(self, cible_x, cible_y):
        diff_x = cible_x - self.x       #Distance lapin renard
        diff_y = cible_y - self.y
        if abs(diff_x) > abs(diff_y):       #On cherche si le renard doit se deplacer en x ou en y 
            if diff_x > 0 :
                self.x += 1
            else :
                self.x += -1
        else:
            if diff_y > 0:
                self.y += 1
            else :
                self.y += -1

    def dessiner(self, surface):
        rect = pg.Rect(self.x * TAILLE_CASE, self.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
        pg.draw.rect(surface, self.couleur, rect)

class Piege:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.couleur = COULEUR_PIEGE

    def dessiner(self, surface):
        rect = pg.Rect(self.x * TAILLE_CASE, self.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
        pg.draw.rect(surface, self.couleur, rect)


# on initialise pygame
pg.init()
screen = pg.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))

# on crée aussi un objet "horloge"
clock = pg.time.Clock()


score = 0
compteur_tours = 0
dx, dy = 0, 0

# On initialise : 

lapin = Lapin(COLONNES // 2, LIGNES // 2)
renards = []
pieges = []
jeu= True

# enfin on boucle à l'infini pour faire le rendu de chaque image
while jeu:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    clock.tick(8)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            jeu = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                dx, dy = 0, -1
            elif event.key == pg.K_DOWN:
                dx, dy = 0, 1
            elif event.key == pg.K_LEFT:
                dx, dy = -1, 0
            elif event.key == pg.K_RIGHT:
                dx, dy = 1, 0
            elif event.key == pg.K_SPACE:
                pieges.append(Piege(lapin.x, lapin.y))          #espace = poser un piege

    if dx != 0 or dy != 0:
        lapin.deplacer(dx, dy)
        compteur_tours += 1                     #chaque mouvement du lapin ajoute 1 tour
    
    for r in renards:
        r.traquer(lapin.x, lapin.y)                                 #Tous les renards ciblent le lapin
    if compteur_tours % 25 == 0 and compteur_tours>0:                       #Tous les 25 tours un nouveau renard apparait
        rx, ry = randint(0, COLONNES - 1), randint(0, LIGNES - 1)
        renards.append(Renard(rx, ry))

    for p in pieges:                                    #Check si le lapin tombe dans un piège
        if lapin.x == p.x and lapin.y == p.y:
            print("Perdu cause de la mort : CHUTE FATALE")
            jeu = False

    renards_vivants = []
    for r in renards:
        if r.x == lapin.x and r.y == lapin.y:          #Check si un renard a mangé un lapin
            print("Perdu cause de la mort : RENARD")
            jeu = False
        est_tombe = False

        for p in pieges:
            if r.x == p.x and r.y == p.y:              #Check si un renard tombe dans un piège
                est_tombe = True
                score += 1
                break
        
        if not est_tombe:
            renards_vivants.append(r)                   #Si il tombe pas il reste vivant pour prochaine boucle
    renards = renards_vivants
    screen.fill(COULEUR_FOND)

    for p in pieges:
        p.dessiner(screen)
    for r in renards:
        r.dessiner(screen)
    lapin.dessiner(screen)

    # Afficher le score
    pg.display.set_caption(f"Score: {score}")
    pg.display.flip()

pg.quit()

    
pass