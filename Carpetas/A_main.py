import pygame
import sys

from ZZ_inicio import *
from nivel_1 import *

W, H = 1500, 900
TAMAÑO_PANTALLA = (W, H)
FPS = 20

RELOJ = pygame.time.Clock()
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)


pygame.init()
# pygame.font.init()
pygame.display.set_caption("Hello Kitty Adventure")
icono = pygame.image.load("Fotos\Logo.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("Imagenes\Fondo_menu.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)


formulario = Inicio(pantalla,497, 397,  450, 300, True, "Imagenes\\nada.png")

# nivel_uno = nivel_uno(pantalla)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_TAB:
        #         cambiar_modo() 
        if evento.type == pygame.MOUSEBUTTONDOWN: #toco la pantalla
            print(evento.pos)
    keys = pygame.key.get_pressed()

    # movimientos()

    pantalla.blit(fondo, (0, 0))  
    # nivel_uno.update(eventos)
    formulario.update(eventos) 
    # 

    pygame.display.update()
