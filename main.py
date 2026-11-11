from random import randint

import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 300))

clock = pg.time.Clock()
taille=10

class lapin:
    def __init__(self,x,y,nbrRenards=0,direction=(0,0)):
        self.x=x
        self.y=y
        self.nbrRenards=nbrRenards
        self.direction=direction
        self.color=(255,255,255)

    def deplacement(self,direction=(0,0)):
        self.x=self.x+direction[0]
        self.y=self.y+direction[1]

class piege:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        piege.color=((0,0,0))

class renard:
    def __init__(self,x,y,direction=(0,0)):
        self.x=x
        self.y=y
        self.direction=direction
        self.color=(255, 127, 0)
    
    def deplacement(self,direction=(0,0)):
        self.x=self.x+direction[0]
        self.y=self.y+direction[1]
    

petitLapin=lapin(20,15)
pieges=list()
renards=list()
running=True
tick=0
while running==True:
    tick+=1
    clock.tick(5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            if event.key==pg.K_UP:
                petitLapin.direction=(0,-1)
            if event.key==pg.K_DOWN:
                petitLapin.direction=(0,1)
            if event.key==pg.K_RIGHT:
                petitLapin.direction=(1,0)
            if event.key==pg.K_LEFT:
                petitLapin.direction=(-1,0)
            if event.key==pg.K_p:
                pieges.append(piege(petitLapin.x,petitLapin.y))
    
    petitLapin.deplacement(petitLapin.direction)
    screen.fill((0,255,0))
    rect = pg.Rect(taille*petitLapin.x, taille*petitLapin.y, taille, taille)
    pg.draw.rect(screen, petitLapin.color, rect)

    if tick%10==0:
        renards.append(renard(randint(0,40),randint(0,30)))


    for p in pieges:
        rect = pg.Rect(taille*p.x, taille*p.y, taille, taille)
        pg.draw.rect(screen, p.color, rect)

    for r in renards:           #pour calculer la direction de déplacement des renards
        dx=petitLapin.x-r.x
        dy=petitLapin.y-r.y
        if dx==0 and dy==0:
            running = False
            print('lapin mangé par renard')
            print('nombre renards capturés : ', petitLapin.nbrRenards)
        elif dx==0 and dy!=0:
            direction=[0,dy/abs(dy)]
            r.deplacement(direction) #ça ajoute 1 ou -1 en fonction du signe
        elif dy==0 and dx!=0:
            direction=[dx/abs(dx),0]
            r.deplacement(direction) #idem
        else :
            direction=[dx/abs(dx),dy/abs(dy)]
            i=randint(0,1)                          #le renard se déplace ou bien sur l'axe x ou bien y de manière aléatoier
            direction[1-i]=0
            r.deplacement(direction)

    for r in renards:
            rect = pg.Rect(taille*r.x, taille*r.y, taille, taille)
            pg.draw.rect(screen, r.color, rect)


    for p in pieges:
        if p.x==petitLapin.x and p.y==petitLapin.y:
            running = False
            print('lapin mort')
            print('nombre renards capturés : ', petitLapin.nbrRenards)
        for r in renards:
            if p.x==r.x and p.y==r.y:
                renards.remove(r)
                pieges.remove(p)
                petitLapin.nbrRenards+=1
                print('nombre renards capturés : ', petitLapin.nbrRenards)

                break           #au début j'avais pas mis le break mais si les renards se reprennent le piege dans la même bouclke ça fait planter le code 


    if petitLapin.x<0 or petitLapin.x>40 or petitLapin.y<0 or petitLapin.y>30:
        running = False
        print('sortie du cadre')
        print('nombre renards capturés : ', petitLapin.nbrRenards)
    pg.display.update()

pg.quit()