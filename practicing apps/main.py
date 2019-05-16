import pygame, sys
import random


class Runner():
    __custome = ('turtle.png', 'fish.png', 'moray.png', 'octopus.png')
    def __init__(self, x=0, y=0):
        ixcustome = random.randint(0, 4)
        self.custome = pygame.image.load("images/{}".format(self.__custome[ixcustome]))
        self.position = [x, y]
        self.name = ''
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __names = ('rayo', 'nemo', 'culebra', 'paul')
    __posy = (160, 200, 240, 280)
    __startline = 5
    __finishline = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            therunner = Runner(self.__startline, self.__posy[i])
            therunner.name = self.__names[i]
            self.runners.append(therunner)

    
        
    
    
    def competir(self):
        gameover = False
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
            
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishline:
                    print("{} ha ganado!!".format(runner.name))
                    gameover = True
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()