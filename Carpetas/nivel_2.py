import pygame
import sys
from AA_Kitty import *
from Modulo import *
from CC_Pantalla import *
from DD_Plataformas import *
from AA_Enemigos import *
from CC_Recolectar import *
from CC_textos import *
from AA_trampas import *
import time
from AA_kittana import *
from CC_Barra import *
from CC_Puntos import *
from AA_puerta_final import Puerta, diccionario_puerta

from FF_Crear_nivel import *
from DD_piso import *

pygame.init()
pygame.font.init()


class nivelDos(Nivel):
    def __init__(self, pantalla: pygame.surface) -> None:
        w = pantalla.get_width()
        h = pantalla.get_height()

        fondo = pygame.image.load("Imagenes\Fondo_dos_n.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 8)

        piso = Piso(0, 785, W, 20)

        piso.crear_piso(pantalla)

        # contador_reloj(tiempo_inicial, self._slave)
        # Vidas_personaje(self._slave, self.jugador)

        plataforma_M_uno = Plataformas("Plataformas\Plataforma_Dos.jpg", (467, 675), (400,75),(812, 682))
        plataforma_dos = Plataformas("Plataformas\Plataforma_Dos.jpg", (788, 565), (500, 75), (1235, 509))### dejo 
        plataforma_tres = Plataformas("Plataformas\Plataforma_Dos.jpg", (347, 361), (91, 60), (493, 419))# mover - (347, 361)
        plataforma_cuatro = Plataformas("Plataformas\Plataforma_Dos.jpg",(0, 293), (300, 60), (201, 298))
        plataforma_cinco = Plataformas("Plataformas\Plataforma_Dos.jpg",(446, 200), (610, 75), (974, 160))
        plataforma_seis = Plataformas("Plataformas\Plataforma_Dos.jpg", (1105, 344), (550, 75), (1495, 275))#mas abajo -(1105, 344) mas largo - 550
        plataforma_siete = Plataformas("Plataformas\Plataforma_Dos.jpg", (530, 467), (90, 75), (1495, 275)) #mas corto 90

        lista_movimientos = [plataforma_M_uno]


        lista_plataformas = [plataforma_dos, plataforma_tres, plataforma_cuatro,
                            plataforma_cinco, plataforma_seis, plataforma_siete]

        lista_gravedad = [piso.lados["main"],plataforma_M_uno.lados["top"], plataforma_dos.lados["top"],
                    plataforma_tres.lados["top"], plataforma_cuatro.lados["top"], 
                    plataforma_cinco.lados["top"], plataforma_seis.lados["top"], plataforma_siete.lados["top"]]
        
        enemigo_uno = enemigo( (788, 488),(1188, 493), diccionario_enemigo, Tamaño_enemigo, 2)# (788, 488) a (1188, 493)
        enemigo_dos = enemigo((462, 127), (932, 102), diccionario_enemigo, Tamaño_enemigo, 2)
        enemigo_tres = enemigo((1108, 257) ,(1385, 260), diccionario_enemigo, Tamaño_enemigo, 2)

        Enemigos = [enemigo_uno, enemigo_dos, enemigo_tres]

        frutilla_uno = Elementos(animaciones_frutilla, (519, 620), (40,40))#(519, 620)
        frutilla_dos = Elementos(animaciones_frutilla, (639, 620), (40,40))#(639, 620)
        frutilla_tres = Elementos(animaciones_frutilla, (795, 497), (40,40))#(795, 497)
        frutilla_cuatro = Elementos(animaciones_frutilla, (904, 497), (40,40))#(904, 497)
        frutilla_cinco = Elementos(animaciones_frutilla, (1024, 497), (40,40))#(1024, 497)
        frutilla_seis = Elementos(animaciones_frutilla, (1136, 502), (40,40))#(1136, 502)
        frutilla_siete = Elementos(animaciones_frutilla, (556, 425), (40,40))#(556, 425)
        frutilla_ocho = Elementos(animaciones_frutilla, (373, 311), (40,40))#(373, 311)
        frutilla_nueve = Elementos(animaciones_frutilla, (235, 245), (40,40))#(235, 245)
        frutilla_diez = Elementos(animaciones_frutilla, (137, 245), (40,40))#(137, 245)
        frutilla_once = Elementos(animaciones_frutilla, (857, 150), (40,40))#(857, 150)
        frutilla_doce  =Elementos(animaciones_frutilla, (771, 150), (40,40))#(771, 150)
        frutilla_trece = Elementos(animaciones_frutilla, (623, 150), (40,40))#(623, 150)
        frutilla_catorce = Elementos(animaciones_frutilla, (498, 150), (40,40))#(498, 150)
        frutilla_quince = Elementos(animaciones_frutilla, (1398, 295), (40,40))#(1398, 295)
        frutilla_diezseis = Elementos(animaciones_frutilla, (1275, 295), (40,40))#(1275, 295)
        frutilla_diezsiete = Elementos(animaciones_frutilla, (1275, 295), (40,40))#(1275, 295)

        lista_objetos = [frutilla_uno, frutilla_dos, frutilla_tres, frutilla_cuatro, frutilla_cinco, 
                        frutilla_seis, frutilla_siete, frutilla_ocho, frutilla_nueve, frutilla_diez, 
                        frutilla_once, frutilla_doce, frutilla_trece, frutilla_catorce, frutilla_quince,
                        frutilla_diezseis, frutilla_diezsiete]

        elemento_recuperar_uno = Elementos(animacion_mas_vidas, (948, 151), (40,40))# (948, 151)

        lista_recuperar = [elemento_recuperar_uno]

        llave = Elementos(animaciones_llave, (45, 226), (25, 60))# (45, 226)

        lista_llave_uno = [llave]

        flor_trampa = Trampas((331, 48), (331, 266), (80,80))# (331, 48) a (331, 266)

        listas_trampas = [flor_trampa]

        puerta_nivel_uno = Puerta(diccionario_puerta, (1357, 642))# - (1356, 617)

        super().__init__(pantalla, fondo, mi_personaje, lista_plataformas, lista_gravedad, 
                        Enemigos, lista_objetos, lista_recuperar, listas_trampas, lista_llave_uno, 
                        puerta_nivel_uno, lista_movimientos, True, True, lista_jefe)

