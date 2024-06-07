import pygame
import sys
from Modulo import *
from CC_Pantalla import *
from CC_Barra import *
from CC_Puntos import *

class Nivel:
    def __init__(self, pantalla, fondo, personaje, plataformas, plataformas_gravedad, enemigos, objetos, vidas, trampas, llave, puerta, movimientos_plataformas, movimientos:bool, jefe_nivel: bool, Jefe) -> None:
        self._slave = pantalla
        self.fondo = fondo
        self.jugador = personaje
        self.plataformas = plataformas
        self.movimientos = movimientos_plataformas
        self.con_movimientos = movimientos
        self.enemigos = enemigos
        self.elementos = objetos
        self.trampas = trampas
        self.llave = llave
        self.final = puerta
        self.gravedad = plataformas_gravedad
        self.vidas = vidas

        self.jefe = Jefe
        self.nivel_jefe = jefe_nivel

        self.pausa = False

    def Teclas(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"
            
        if keys[pygame.K_e]:
            self.jugador.que_hace = "Ataque_Frutilla"
        
        if keys[pygame.K_x]:
            self.jugador.que_hace = "Ataque_Moño"

    def dibujar_rect(self): 
        if get_mode():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Pink", self.jugador.lados[lado], 2)
            for proyectil in self.jugador.lista_proyectil:
                pygame.draw.rect(self._slave, "Red", proyectil.rectangulo, 2)
            
            for trampa in self.trampas:
                pygame.draw.rect(self._slave, "Yellow", trampa.rectangulo, 2)

    def actualizar_elementos(self):
        for plataforma in self.plataformas:
            plataforma.animar(self._slave)

        if self.con_movimientos == True:
            for plataforma in self.movimientos:
                plataforma.update_movimiento(self._slave)

        if self.nivel_jefe == True:
            for jefe in self.jefe:
                jefe.update(self._slave, self.jugador, self.gravedad, self.enemigos, self.jugador.lista_proyectil)

        for trampa in self.trampas:
            trampa.update(self._slave, self.jugador)

        self.final.update(self._slave, self.jugador)
        self.jugador.update(self._slave, self.gravedad, self.enemigos, self.elementos, self.vidas, self.trampas, self.llave)

        for enemigo in self.enemigos:
            enemigo.update(self._slave, self.gravedad, self.jugador.lista_proyectil, self.jugador, self.enemigos)

        for proyectil in self.jugador.lista_proyectil:
            proyectil.update(self._slave, self.jugador, self.enemigos) 

        for llave in self.llave:
            llave.update(self._slave)

    def pausar(self):
        self.pausa = True

    def update(self, lista_eventos):
        if self.pausa:
            return

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo() 
            if evento.type == pygame.MOUSEBUTTONDOWN: #toco la pantalla
                print(evento.pos)

        self._slave.blit(self.fondo, (0, 0)) 
        self.Teclas()    
        self.dibujar_rect()
        Vidas_personaje(self._slave, self.jugador)
        self.actualizar_elementos()
        contador_reloj(tiempo_inicial, self._slave)
