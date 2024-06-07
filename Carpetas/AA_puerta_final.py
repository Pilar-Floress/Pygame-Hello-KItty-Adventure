import pygame
from AA_archivos_kittana import *
from BB_Modificacion_imagenes import *
from CC_Recolectar import *
from CC_textos import *
from AA_proyectiles import *
from CC_Archivos_ataques import *
from CC_Pantalla import *
from AA_Enemigos import *
from CC_Barra import *

from ZZ_niveles import *

# from ZZ_datos import *
# from CC_Puntos import *
# from ZZ_ganar import *
animacion_puerta_desbloqueada = [pygame.image.load("Imagenes\Puerta.png")]

animacion_puerta_bloqueada = [pygame.image.load("Imagenes\Puerta_cerrada-removebg-preview.png")]

diccionario_puerta = {}
diccionario_puerta["Desbloqueada"] = animacion_puerta_desbloqueada
diccionario_puerta["Bloqueada"] = animacion_puerta_bloqueada


class Puerta:
    def __init__(self, animacion, ubicacion) -> None:
        self.animaciones = animacion
        self.reescalar = self.reescalar_animaciones()
        self.rectangulo = self.animaciones["Desbloqueada"][0].get_rect()
        self.rectangulo.x = ubicacion[0]
        self.rectangulo.y = ubicacion[1]
        self.contador_pasos = 0
        self.lados = obtener_rectangulo(self.rectangulo)
        # self.formulario_niveles = FormNiveles()

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], 114, 136)

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    # def guardar_puntos(self, personaje):
    #     # acumulador_puntos(personaje)

    def finalizar_nivel(self, pantalla, personaje):
        if self.lados["main"].colliderect(personaje.lados["main"]):
            print("Salio")
            

    def update(self, pantalla, personaje):
        if personaje.llaves_obtenidas > 0:
            self.animar(pantalla, "Desbloqueada")
            self.finalizar_nivel(pantalla, personaje)
        else:
            self.animar(pantalla, "Bloqueada")

puerta_nivel_uno = Puerta(diccionario_puerta, (1353, 603))

# def __init__(self, animacion, ubicacion, formulario_niveles) -> None:
#         self.animaciones = animacion
#         self.reescalar = self.reescalar_animaciones()
#         self.rectangulo = self.animaciones["Desbloqueada"][0].get_rect()
#         self.rectangulo.x = ubicacion[0]
#         self.rectangulo.y = ubicacion[1]
#         self.contador_pasos = 0
#         self.lados = obtener_rectangulo(self.rectangulo)
#         self.formulario_niveles = formulario_niveles  # Referencia al formulario de niveles

#     def reescalar_animaciones(self):
#         for clave in self.animaciones:
#             reescalar_imagenes(self.animaciones[clave], 114, 136)

#     def animar(self, pantalla, que_animacion):
#         animacion = self.animaciones[que_animacion]
#         largo = len(animacion)
        
#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0
        
#         pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
#         self.contador_pasos += 1

#     def finalizar_nivel(self, pantalla, personaje):
#         if self.rectangulo.colliderect(personaje.lados["main"]) and personaje.llaves_obtenidas > 0:
#             self.formulario_niveles.manejador_nivel("")  # Llama al método manejador_nivel del formulario de niveles

#     def update(self, pantalla, personaje):
#         if personaje.llaves_obtenidas > 0:
#             self.animar(pantalla, "Desbloqueada")
#         else:
#             self.animar(pantalla, "Bloqueada")

