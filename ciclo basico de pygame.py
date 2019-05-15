import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
#color rojo 
screen.fill((255, 0, 0))
#titulo del juego
pygame.display.set_caption("ciclo basico de pygame")
pygame.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    pygame.display.flip()

pygame.quit()