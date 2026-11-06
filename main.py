import pygame as pg
import random as rd

#initialisation pieges
nb_piege=10
pieges=[[rd.randint(0,30),rd.randint(0,30)] for _ in range(nb_piege)]

#définition classes
class Animal():
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def draw(self):
        pg.draw.rect(screen, self.color, (self.x*20, self.y*20,20,20))

    def is_fallen(self):
        if [self.x,self.y] in pieges:
            return True
        return False


class Rabbit(Animal):
    def __init__(self,x,y,nb_pieges,nb_captures=0):
        self.nb_pieges=nb_pieges
        self.nb_captures=nb_captures
        super().__init__(x,y,[128,128,128])

    def moove(self,rabbit_direction):
        self.x+=rabbit_direction[0]
        self.y+=rabbit_direction[1]


class Fox(Animal):
    def __init__(self,x,y):
        super().__init__(x,y,[255,127,0])

    def moove(self,fox_direction):
        self.x+=fox_direction[0]
        self.y+=fox_direction[1]

class Foxes:
    def __init__(self,foxes): #foxes est une liste de Fox
        self.foxes=foxes

    def delect(self):
        foxes_prime=[]
        for fox in self.foxes:
            if not fox.is_fallen():
                foxes_prime.append(fox)
        self.foxes=foxes_prime

    def add(self):
        while len(self.foxes)<nb_foxes:
            x=rd.randint(0,30)
            y=rd.randint(0,30)
            self.foxes.append(Fox(x,y))


#initialisation du jeux
pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

#initialisation joueur
(x0,y0)=(10,10)
player=Rabbit(x0,y0,10)
rabbit_direction=(1,0)

#initialisation renards
nb_foxes=3
foxes=Foxes([Fox(rd.randint(0,30),rd.randint(0,30)) for _ in range(nb_foxes)])


#fonctions utiles
def damier():
    width, height = 20, 20 
    for j in range(31):
        for i in range(31):   
            rect = pg.Rect(j*20, i*20, width, height)
            if (i+j)%2==0:
                e=150
            else:
                e=100
            color = (0, e, 0) 
            pg.draw.rect(screen, color, rect)

def fox_direction_calculation(fox,rabbit):
    xf,yf=fox.x,fox.y
    xr,yr=rabbit.x,rabbit.y
    if abs(xf-xr) > abs(yf-yr):
        if xf-xr > 0:
            return (-1,0)
        else :
            return (1,0)
    else:
        if yf-yr > 0:
            return (0,-1)
        else :
            return (0,1)
    

# boucle de rendu
running=True
while running:
    clock.tick(4)

    if (player.x<=0 and rabbit_direction == (-1,0)) or (player.x>=29 and rabbit_direction == (1,0)) or (player.y<=0 and rabbit_direction == (0,-1)) or (player.y>=29 and rabbit_direction == (0,1)):
        rabbit_direction = (0,0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

            #déplacement du lapin
            if event.key == pg.K_UP :
                rabbit_direction = (0,-1)
            
            if event.key == pg.K_DOWN :
                rabbit_direction = (0,1)

            if event.key == pg.K_RIGHT :
                rabbit_direction = (1,0)

            if event.key == pg.K_LEFT :
                rabbit_direction = (-1,0)
                          
    damier()

    # mise à jour player
    player.moove(rabbit_direction)
    player.draw()
    if player.is_fallen():
        running = False

    #mise à jour fox
    foxes.add()
    foxes.delect()
    for fox in foxes.foxes:
        if fox.x==player.x and fox.y==player.y:
            running=False
        else:
            fox.moove(fox_direction_calculation(fox,player))
        fox.draw()

    #mise à jour des pièges
    for piege in pieges:
        rect = pg.Rect(piege[0]*20, piege[1]*20, 20, 20)
        pg.draw.rect(screen, [150, 75, 0], rect)
    
    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()

pg.quit()