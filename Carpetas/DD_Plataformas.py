import pygame
from BB_Modificacion_imagenes import *
from CC_Pantalla import *
from AA_Kitty import *
# from DD_piso import *

# PISO
# piso = pygame.Rect(0, 380, W, 20)
# piso.top = mi_personaje.lados["main"].bottom
# lados_piso = obtener_rectangulo(piso)



class Plataformas():
    def __init__(self, animacion, inicio, tamaño, final) -> None:
        # self.reescalar = reescalar_imagenes(animacion, tamaño[0], tamaño[1])
        self.animaciones = pygame.image.load(animacion)
        self.animaciones = pygame.transform.scale(self.animaciones, (tamaño[0], tamaño[1]))
        self.rectangulo_plataforma = self.animaciones.get_rect()
        self.rectangulo_plataforma.x = inicio[0]
        self.rectangulo_plataforma.y = inicio[1]
        self.inicio = inicio
        self.final = final
        self.velocidad = 3
        self.lados = obtener_rectangulo(self.rectangulo_plataforma)

        self.direccion = 1

    def animar(self, pantalla):
        pantalla.blit(self.animaciones, self.lados["main"])

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update_movimiento(self, pantalla):
        if self.direccion == 1:
            if self.lados["main"].x < self.final[0]:
                self.animar(pantalla)
                self.mover(self.velocidad)
            else:
                self.animar(pantalla)
                self.direccion = -1  
        else:
            if self.lados["main"].x > self.inicio[0]:
                self.animar(pantalla)
                self.mover(-self.velocidad)  
            else:
                self.animar(pantalla)
                self.direccion = 1 



# plataforma_uno = Plataformas("Fotos\Piedra.png",(500,620),(400,75), (500, 680) )
# # Plataforma_lados_dos = Plataformas((400,75),(1000,500),"Fotos\Piedra.png")

# plataforma_uno = crear_plataforma((400,75),(500,620), "Fotos\Piedra.png")
# plataforma_dos = crear_plataforma((400,75),(1000,500),"Fotos\Piedra.png")

# plataforma_uno = Plataformas("Fotos\Piedra.png",(276, 633),(400,120), (500,620))
# plataforma_dos = Plataformas("Fotos\Piedra.png",(606, 513), (400,75), (1076, 503))
# plataforma_tres = Plataformas("Fotos\Piedra.png",(1024, 410), (400,75), (0, 0))
# plataforma_cuatro = Plataformas("Fotos\Piedra.png",(520, 285), (400,75), (0, 0))
# plataforma_cinco = Plataformas("Fotos\Piedra.png",(3, 189), (400,75), (509, 193))


# lista_plataformas_uno = [plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro]

# plataforma_seis = Plataformas("Fotos\Piedra.png",(3, 663), (400,125), (509, 193))
# plataforma_siete = Plataformas("Fotos\Piedra.png",(1216, 590), (400,75), (509, 193))

# lista_plataformas_dos = [plataforma_seis, plataforma_siete]

# #Nivel 2
# lista_plataformas_movimientos_dos = [plataforma_dos, plataforma_cinco]



# Personajes 
# lista_gravedad_uno = [lados_piso["top"], plataforma_uno.lados["top"], plataforma_dos.lados["top"],
#                     plataforma_tres.lados["top"], plataforma_cuatro.lados["top"], plataforma_cinco.lados["top"]]

# lista_gravedad_uno = [lados_piso, plataforma_uno.lados, plataforma_dos.lados,
#                     plataforma_tres.lados, plataforma_cuatro.lados, plataforma_cinco.lados]

# lista_gravedad_dos = ["Frutilla"]