
import pygame
from AA_archivos_kitty import *
from BB_Modificacion_imagenes import *
from CC_Recolectar import *
from CC_Archivos_ataques import *
from CC_textos import *
from AA_proyectiles import *
from CC_Archivos_ataques import *
from CC_Pantalla import *
from CC_Barra import *



# lista_proyectiles = []

# recolectar_frutillas = pygame.mixer.Sound("")

class Personaje():
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        self.vidas = 3
        # Configuración
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # Gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        # Animaciones
        self.contador_pasos = 0
        self.que_hace = diccionario_animaciones["quieto_derecha"]
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # Rectángulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        self.velocidad = velocidad
        # Movimientos:
        self.bandera_derecha = True
        self.bandera_izquierda = False
        # daños:
        self.tiempo_invulnerable = 0
        self.tiempo_invulnerable_total = 60
        #DISPAROS
        self.tiempo_disparos = 0
        self.tiempo_disparos_total = 15

        self.tiempo_moño = 0
        self.tiempo_moño_total = 60

        self.bandera_gravedad = True
        self.posicion_inicial = posicion_inicial
        
        #PUNTOS:
        self.puntos = 0
        self.llaves_obtenidas = 0 
        self.frutillas = 0 #Balas
        self.puntos_enemigos = 0

        # recargas:
        self.balas = 10
        self.moños = 3
        
        #Proyectiles
        self.lista_proyectil = []
        self.lista_moños = []

        
    
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
    
    def aplicar_gravedad(self, pantalla, lista_plataformas):
            if self.esta_saltando:
                if self.bandera_derecha == True:
                    self.animar(pantalla, "salta_derecha")
                elif self.bandera_izquierda == True:
                    self.animar(pantalla, "salta_izquierda")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
            for plataforma in lista_plataformas:
                if self.lados["bottom"].colliderect(plataforma):
                    self.lados["main"].bottom = plataforma.top + 5
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
            


    def update(self, pantalla, lista_plataformas, lista_enemigos, lista_objetos, lista_mas_vidas, trampas, llaves):
        if self.que_hace == "derecha":
            nueva_x = self.rectangulo.x + 10
            if nueva_x < W - self.rectangulo.width:
                self.mover(self.velocidad)
            if not self.esta_saltando:
                self.animar(pantalla, "camina_derecha")
            self.bandera_derecha = True
            self.bandera_izquierda = False

        elif self.que_hace == "izquierda":
            nueva_x = self.rectangulo.x - 10
            if nueva_x > 0:
                self.mover(-self.velocidad)
            if not self.esta_saltando:
                self.animar(pantalla, "camina_izquierda")
            self.bandera_derecha = False
            self.bandera_izquierda = True    
            
        elif self.que_hace == "salta":
            if self.bandera_derecha == True:
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            elif self.bandera_izquierda == True:
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
        elif self.que_hace == "quieto":
            if self.bandera_derecha == True:
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto_derecha")
            elif self.bandera_izquierda == True:
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto_izquierda")
        if self.balas != 0 and self.que_hace == "Ataque_Frutilla":
            self.disparar_frutillas()
            self.animar(pantalla, "frutilla")
            
        elif self.balas == 0:
            crear_texto(pantalla, "Te quedaste sin frutilla, recoge más", (50,50), (205, 92, 92), 20)
            
        # if self.moños != 0 and self.que_hace == "Ataque_Moño":
        #     self.disparar_moño()
        # elif self.moños == 0:
        #     crear_texto(pantalla, "Te quedaste sin moños, espera a la proxima ronda", (100,100), (205, 92, 92), 20)

        ### DAÑOS ###
        if self.vidas == 0:
            self.restablecer_personaje()
            self.bandera_gravedad = True

        #LLAMADOS
        self.daño_enemigos( lista_enemigos)
        self.trampas(pantalla, trampas)
        self.datos(pantalla)
        self.tiempos()
        self.llaves(llaves)
        self.Frutillas(pantalla, lista_objetos)
        self.obtener_vidas(pantalla, lista_mas_vidas)
        self.aplicar_gravedad(pantalla, lista_plataformas)
        self.verificar_salida_pantalla()


    def tiempos(self):
        if self.tiempo_invulnerable > 0:
            self.tiempo_invulnerable -= 1

        if self.tiempo_disparos	> 0:
            self.tiempo_disparos -= 1

        if self.tiempo_moño > 0:
            self.tiempo_moño -= 1


    def verificar_salida_pantalla(self):
        if self.lados["main"].bottom > H:
            self.vidas -= 3

    # def disparar_moño(self):
    #     if self.tiempo_moño == 0:
    #         if self.bandera_derecha:
    #             direccion_moño = 1
    #         else:
    #             direccion_moño = -1

    #         self.moños -= 1
    #         moñitos = Proyectil(self.rectangulo.x, self.rectangulo.y, direccion_moño, "Ataques\moño.png", 2, 8)
    #         self.lista_moños.append(moñitos)

    #         self.tiempo_moño = self.tiempo_moño_total


    def disparar_frutillas(self):
        if self.tiempo_disparos == 0:
            self.tirar = pygame.mixer.Sound("musica\XSE01107.WAV.wav")
            self.tirar.play
            if self.bandera_derecha:
                direccion = 1  # El proyectil se moverá hacia la derecha
                
            else:
                direccion = -1  # El proyectil se moverá hacia la izquierda
            self.balas -= 1
            proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y, direccion, "Fotos\Frutilla_nv.png", 1, 8)
            self.lista_proyectil.append(proyectil)
            self.tiempo_disparos = self.tiempo_disparos_total
            
        # musica\XSE00627.WAV.wav


    def daño_enemigos(self, lista_enemigos):
        if self.tiempo_invulnerable == 0:  
            for enemigo in lista_enemigos:
                if self.lados["main"].colliderect(enemigo.lados["main"]):
                    self.puntos -= 10
                    self.vidas -= 1
                    self.sonido_vidas = pygame.mixer.Sound("musica\Menos_vida.wav")
                    self.sonido_vidas.play()
                    break
            self.tiempo_invulnerable = self.tiempo_invulnerable_total

        # self.datos(pantalla)


    def Frutillas(self, pantalla, lista_elemento):
        for elemento in lista_elemento:
            if self.lados["main"].colliderect(elemento.lados["main"]):
                self.balas += 1
                self.puntos += 20
                self.sonido = pygame.mixer.Sound("musica\Frutila.wav")
                self.sonido.play()
                lista_elemento.remove(elemento)
            else:
                elemento.update(pantalla)
        # self.datos(pantalla)
    
    
    def llaves(self, llaves):
        for llave in llaves:
            if self.lados["main"].colliderect(llave.lados["main"]):
                self.llavesitas = pygame.mixer.Sound("musica\XSE00627.WAV.wav")
                self.llavesitas.play()
                print("llave recogida")
                self.llaves_obtenidas += 1
                llaves.remove(llave)
                break



    def obtener_vidas(self,pantalla, lista_elementos):
        for elemento in lista_elementos:
            if self.lados["main"].colliderect(elemento.lados["main"]):
                if self.vidas >= 3:
                    crear_texto(pantalla, "Oh no, tienes la vida completa", (890, 12), (205, 92, 92), 20 )
                elif self.vidas < 3:    
                    self.vidas += 1
                    self.puntos += 30
                    self.sonido_mas_vida = pygame.mixer.Sound("musica\Vidas.wav")
                    self.sonido_mas_vida.play()
                    lista_elementos.remove(elemento)
            else:
                elemento.update(pantalla)

        # self.datos(pantalla)



    def datos(self, pantalla):
        puntos = "Fotos\Frutilla_nv.png"
        frutilla_img = pygame.image.load(puntos)  
        imagen_redimensionada_frutilla = pygame.transform.scale(frutilla_img, (40, 40)) 
        
        rect_frutilla = imagen_redimensionada_frutilla.get_rect()  
        rect_frutilla.x = 170
        rect_frutilla.y = 5 
        pantalla.blit(imagen_redimensionada_frutilla, rect_frutilla)
        crear_texto(pantalla, f"{self.balas}", (185, 25), "Black", 20)

        crear_texto(pantalla, f"PUNTOS: {self.puntos}", (288, 15), "Black", 30 )


    def trampas(self,pantalla, lista_trampas):
        if self.tiempo_invulnerable == 0:  
            for trampa in lista_trampas:
                if self.lados["main"].colliderect(trampa["main"]):
                    self.vidas -= 1
                    self.puntos -= 15
                    self.sonido_vidas = pygame.mixer.Sound("musica\Menos_vida.wav")
                    self.sonido_vidas.play()
                    self.tiempo_invulnerable = self.tiempo_invulnerable_total
                    break
        # self.datos(pantalla)

    def restablecer_personaje(self):
        self.puntos = 0
        self.balas = 10
        self.vidas = 3
        self.tiempo_invulnerable = 0
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = self.posicion_inicial[0]
        rectangulo.y = self.posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)  

    # def ubicacion_personaje(self):
    #     print("Posición actual del personaje: ({}, {})".format(self.lados["main"].x, self.lados["main"].y))

# mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 8)









'''
def restablecer_personaje(self):
        self.vidas = 3
        self.tiempo_invulnerable = 0
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = self.posicion_inicial[0]
        rectangulo.y = self.posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
'''



