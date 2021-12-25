import pygame
from game import *
import numpy as np


def position(a):
	x=a[0]
	y=a[1]

	if(x in range(31,73))and(y in range(66,104)):
		return 0
	if(x in range(124,165))and(y in range(67,105)):
		return 1
	if(x in range(222,263))and(y in range(67,105)):
		return 2
	if(x in range(317,357))and(y in range(67,105)):
		return 3
	if(x in range(412,454))and(y in range(67,105)):
		return 4
	if(x in range(508,550))and(y in range(67,105)):
		return 5
	if(x in range(603,645))and(y in range(67,105)):
		return 6
	
	if(x in range(36,168))and(y in range(8,46)):
		return 10					

def change(p):
	if(p==1):
		return 2
	if(p==2):
		return 1	





def show(d,p):
	if(p==1):
		screen.blit(p1,(10,30))
	elif(p==2):
		screen.blit(p2,(10,30))	
	else:	
		
		for i in range(6):
				for j in range(7):
					if(d[i][j]==1):
						screen.blit(W,(6+(j*96),131+(i*96)))
					if(d[i][j]==2):
						screen.blit(R,(6+(j*96),131+(i*96)))




# initialize game engine
pygame.init()

window_width=673
window_height=700

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Jeux puissance 4")

dead=False

W = pygame.image.load("img/W.png")

R = pygame.image.load("img/R.png")

p1 = pygame.image.load("img/P1win.png")

p2 = pygame.image.load("img/P2win.png")

g=the_game()
player=1


background_image = pygame.image.load("img/bg.png").convert()


while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        	if pygame.mouse.get_pressed()[0]:
        		pos= pygame.mouse.get_pos()
        		p=position(pos)
        		if(p!=None):
	        		
	        		if(g.get_game_end()==0):
	        			av=available(g.get_d(),p)
	        			
	        			if(av==-2):
	        				g.reset()

	        			elif(av!=-1):
	        				g.play(player,p)
	        				player=change(player)

    screen.blit(background_image, [0, 0])
    
    show(g.get_d(),g.check_win())


    pygame.display.flip()      