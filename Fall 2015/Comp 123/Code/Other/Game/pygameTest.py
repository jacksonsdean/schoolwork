import pygame


from pygame.locals import *


def main():
    pygame.init()

    screenSize = width, height =  640, 480

    screen = pygame.display.set_mode(screenSize)

class player(pygame.sprite.Sprite): 
    def _init_(self):
        print("hello world")
    def update(self):
	newpos = self.calcnewpos(self.rect,self.vector)
	self.rect = newpos
    
    def calcnewpos(self,rect,vector):
	(angle,z) = vector
	(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
	return rect.move(dx,dy)    



def quit():
    pygame.display.quit()
    




main()