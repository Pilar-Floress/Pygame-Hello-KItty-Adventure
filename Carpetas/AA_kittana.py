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

class Jefe:
    def __init__(self, posicion_inicial, posicion_final ) -> None:
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0

        self.vidas = 5
        self.ancho = 130
        self.alto = 180

        self.contador_pasos = 0
        self.que_hace = diccionario_kittana_movimientos["Derecha"]
        self.animaciones = diccionario_kittana_movimientos
        self.reescalar_animaciones()

        self.rectangulo = self.animaciones["Derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)

        self.inicio = posicion_inicial
        self.final = posicion_final

        self.velocidad = 5

        self.bandera_derecha = True
        self.bandera_izquierda = False

        self.direccion = 1

        # daños:
        self.tiempo_invulnerable = 0
        self.tiempo_invulnerable_total = 60

        # Velocidades:
        self.tiempo_normal = 0
        self.tiempo_aum_velocidad = 60
        
        self.tiempo_velocidad = 0
        self.tiempo_normalidad = 40

        # Ataques:
        self.tiempo_ataque = 0
        self.tiempo_ataque_total = 50

        self.tiempo_daños = 0
        self.tiempo_daños_total = 30
        self.activo = True


    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


    def aplicar_gravedad(self, lista_plataformas):
        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y
        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad

        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma):
                self.lados["main"].bottom = plataforma.top + 5
                self.desplazamiento_y = 0
                self.esta_saltando = False


    def update(self, pantalla, personaje, lista_plataformas, lista_enemigos, lista_proyectiles ):
        if self.tiempo_ataque > 0:
            self.tiempo_ataque -= 1

        # if self.eliminado == False:
        if self.activo:
            if self.vidas > 0:
                
                if self.direccion == 1:
                    if self.lados["main"].x < self.final[0]:
                        self.animar(pantalla, "Derecha")
                        self.mover(self.velocidad)
                        # self.ataques(pantalla, personaje)
                    else:
                        self.animar(pantalla, "Derecha")
                        self.direccion = -1
                elif self.direccion == -1:
                    if self.lados["main"].x > self.inicio[0]:
                        self.animar(pantalla, "Izquierda")
                        self.mover(-self.velocidad)
                        # self.ataques(pantalla, personaje)
                    else:
                        self.animar(pantalla, "Izquierda")
                        self.direccion = 1

                self.daño_personaje(pantalla, personaje)
                self.aplicar_gravedad(lista_plataformas)
                self.velocidades()  
                self.daños(lista_proyectiles, personaje)

        elif self.vidas < 0: 
            lista_jefe.remove(self) #DESCOMENTAR 
            personaje.puntos += 30
            print("Chau kittana")
        vidas_jefe(pantalla, self.vidas)
    

    def velocidades(self):
        if self.tiempo_normal > 0:
            self.tiempo_normal -= 1
        
        if self.tiempo_normal == 0:
            # print("Aumento")
            self.velocidad = 15
            self.tiempo_normal = self.tiempo_aum_velocidad
        else:
            if self.tiempo_velocidad > 0:
                self.tiempo_velocidad -=1
            if self.tiempo_velocidad == 0:
                self.tiempo_velocidad = self.tiempo_normalidad
                self.velocidad = 5

    def daños(self, lista_proyectiles, personaje):
        if self.tiempo_daños > 0:
            self.tiempo_daños -= 1

        if self.tiempo_daños == 0:
            for proyectil in lista_proyectiles:
                if self.lados["main"].colliderect(proyectil.rectangulo):
                    print(f"Vidas:{self.vidas}")
                    personaje.puntos += 15
                    self.vidas -= 1
                    lista_proyectiles.remove(proyectil)

            self.tiempo_daños = self.tiempo_daños_total
        
        if self.vidas == 0:
            self.activo = False

        # if self.vidas == 0 and not self.eliminado:
            
    def daño_personaje(self, pantalla, personaje):
        if self.tiempo_ataque == 0 and self.lados["main"].colliderect(personaje.lados["main"]):
            print("Ataque kittana")
            self.animar(pantalla, "Ataque D")
            personaje.puntos -= 20
            personaje.vidas -= 1
            self.ataque = pygame.mixer.Sound("musica\kittana.wav")
            self.ataque.play
            self.mover(0)
            self.tiempo_ataque = self.tiempo_ataque_total 
        


kittana = Jefe((307, 451), (700, 450))

lista_jefe = [kittana]

