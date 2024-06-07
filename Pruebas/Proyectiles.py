import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de disparos")



class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):  
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5  # Velocidad del disparo

    def update(self):
        self.rect.y -= self.speed


disparos = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Crea un nuevo disparo en la posición del jugador
                disparo = Disparo(60, 60)
                disparos.add(disparo)

    disparos.update()
    for disparo in disparos:
        if disparo.rect.bottom < 0:
            disparos.remove(disparo)
    disparos.draw(screen)

    pygame.display.update()

