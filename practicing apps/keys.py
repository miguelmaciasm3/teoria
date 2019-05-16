import pygame, sys
from pygame.locals import *
import random

class Runner():
    __custome = ('turtle.png', 'fish.png', 'moray.png', 'octopus.png')
    def __init__(self, x=0, y=0):
        ixcustome = random.randint(0, 4)
        self.custome = pygame.image.load("images/{}".format(self.__custome[ixcustome]))
        self.position = [x, y]
        self.name = ''
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320, 240)
        
        
    def start(self):
        gameover = False
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        #mover runner hacia arriba
                        self.runner.position[1] -= 10
                    elif event.key == K_DOWN:
                        #mover runner hacia abajo
                        self.runner.position[1] += 10
                    elif event.key == K_LEFT:
                        #mover runner a la izqda
                        self.runner.position[0] -= 10
                    elif event.key == K_RIGHT:
                        #mover runner a la derecha
                        self.runner.position[0] += 10
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            pygame.display.flip()
            
print("my name is {}".format(__name__))

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()