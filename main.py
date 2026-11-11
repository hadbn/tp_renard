from random import randint

import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 300))

clock = pg.time.Clock()
taille=10

class lapin:
    def __init__(self,x,y,direction=(0,0)):
        self.x=x
        self.y=y
        self.direction=direction
        self.color=(255,255,255)

    def deplacement(self,x,y,direction=(0,0)):
        self.x=x+direction[0]
        self.y=y+direction[1]

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
    
    def deplacement(self,x,y,direction=(0,0)):
        self.x=x+direction[0]
        self.y=y+direction[1]
    

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
    
    petitLapin.deplacement(petitLapin.x,petitLapin.y,petitLapin.direction)
    screen.fill((0,255,0))
    rect = pg.Rect(taille*petitLapin.x, taille*petitLapin.y, taille, taille)
    pg.draw.rect(screen, petitLapin.color, rect)

    if tick%5==0:
        renards.append(renard(randint(0,20),randint(0,15)))


    for p in pieges:
        rect = pg.Rect(taille*p.x, taille*p.y, taille, taille)
        pg.draw.rect(screen, p.color, rect)

    for p in pieges:
        if p.x==petitLapin.x and p.y==petitLapin.y:
            running = False
            print('lapin mort')

    
    pg.display.update()

pg.quit()