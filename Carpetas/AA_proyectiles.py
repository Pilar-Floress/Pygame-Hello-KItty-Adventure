from typing import Any
import pygame
# from pygame.sprite import _Group, Sprite
from BB_Modificacion_imagenes import *
# from AA_Kitty import Personaje
from CC_Archivos_ataques import *
from CC_textos import *
from CC_Pantalla import *



######################################################################################################################



class Proyectil:
    def __init__(self, x, y, direccion, animacion, daño, velocidad):
        self.x = x
        self.y = y
        self.direccion = direccion
        self.velocidad = velocidad
        self.daño = daño
        self.animaciones = animacion
        self.animaciones = pygame.image.load(self.animaciones)
        self.imagen_redimensionada = pygame.transform.scale(self.animaciones, (40, 40))
        self.rectangulo = self.imagen_redimensionada.get_rect()
        self.rectangulo.x = self.x  
        self.rectangulo.y = self.y  
        self.lados_disparo = obtener_rectangulo(self.rectangulo)

        self.tiempo_personaje = 0
        self.tiempo_personaje_total = 5

    def mover(self, mi_personaje):
        self.x += self.velocidad * self.direccion
        self.rectangulo.move_ip(self.velocidad * self.direccion, 0)  # Actualizar posición del rectángulo de colisión
        if self.x < 0 or self.x > W:
            # Eliminar el proyectil de la lista de proyectiles
            mi_personaje.lista_proyectil.remove(self)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen_redimensionada, (self.x, self.y))


    def update(self, pantalla,  lista_personaje, lista_enemigos):
        self.dibujar(pantalla)
        self.mover(lista_personaje)




    # def personaje(self, personaje):
    #     if self.tiempo_personaje > 0:
    #         tiempo_inicial -= 1

    #     if self.tiempo_personaje == 0:
    #         if self.rectangulo.colliderect(personaje.lados["main"]):
    #             # Eliminar
    #             pass
    #         self.tiempo_personaje = self.tiempo_personaje_total

    # def enemigos(self, lista_enemigos):
    #     for enemigo in lista_enemigos:
    #         if self.rectangulo.colliderect(enemigo.lados["main"]):
    #             pass


# class Proyectil:
#     def __init__(self, x, y, direccion):
#         self.x = x
#         self.y = y
#         self.direccion = direccion
#         self.velocidad = 5  
#         self.imagen = pygame.image.load("Fotos\Frutilla_nv.png")
#         self.imagen_redimensionada = pygame.transform.scale(self.imagen, (40, 40))
#         self.rectangulo = self.imagen_redimensionada.get_rect()
#         self.lados = obtener_rectangulo(self.rectangulo)

#         self.tiempo_personaje = 0
#         self.tiempo_personaje_total = 5

    
#     def mover(self, mi_personaje):
#         self.x += self.velocidad * self.direccion
#         if self.x < 0 or self.x > W:
#             # Eliminar el proyectil de la lista de proyectiles
#             mi_personaje.lista_proyectil.remove(self)

#     def dibujar(self, pantalla):
#         pantalla.blit(self.imagen_redimensionada, (self.x, self.y))

#     def enemigos(self, lista_enemigos, personaje):
#         for enemigo in lista_enemigos:
#             if enemigo.rectangulo.colliderect(self.rectangulo):
#                 print("Colisiones enemigo")
#                 enemigo.vidas -= 1
#                 personaje.lista_proyectil.remove(self)


#     def update(self, pantalla,  lista_personaje, lista_enemigos):
#         self.dibujar(pantalla)
#         self.mover(lista_personaje)
#         self.enemigos(lista_enemigos, lista_personaje)
        # self.plataformas(pantalla, lista_personaje, lista_plataformas)
    






