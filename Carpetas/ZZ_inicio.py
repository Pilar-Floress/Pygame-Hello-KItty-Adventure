import pygame
import sys
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *

from ZZ_ajustes import *
from ZZ_niveles import *
from ZZ_datos import *
from ZZ_ranking import *

Rosita_ajustes = (240, 128, 128)

Rosa_Bordes = (235,182,250)
Rosa_centro = (252,144,221)
LightCoral = (240,128,128)
Salmon = (250,128,114)

class Inicio(Form):
    def __init__(self, screen, x, y, w, h,  active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self.pantalla = screen
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.btn_ajustes = Button_Image(self._slave, x, y, 180, 100, 150, 40, "sin_fondo\Ajustes_img-removebg-preview.png", self.btn_ajustes, "Ajustes")
        self.btn_niveles = Button_Image(self._slave, x, y, 180, 30, 150, 40, "sin_fondo\Inicio_opciones-removebg-preview.png", self.btn_play, "Niveles")
        self.btn_salir = Button_Image(self._slave, x, y, 180, 240, 150, 40, "sin_fondo\Salir_opciones-removebg-preview.png", self.btn_salir, "salir")
        self.btn_ranking = Button_Image(self._slave, x, y, 180, 170, 150, 40, "sin_fondo\Ranking_img-removebg-preview.png", self.btn_ranking, "ranking")

        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.btn_ajustes)#rankin otra ventana
        self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.btn_salir)

        
    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)
            
    def btn_salir(self, texto):
        pygame.quit()
        sys.exit()
    
    def btn_ajustes(self, texto):
        opciones = FormAjustes(self._master, 493, 229, 500, 550, (247, 208, 208), Rosita_ajustes, 3, True)
        self.show_dialog(opciones)


    def btn_play(self, texto):
        # niveles = FormNiveles(self._master, 493, 229, 500, 550, (220,0,220), True, "nada.png")
        # self.show_dialog(niveles)
        usuario = FormDatos(self.pantalla , 493, 230, 500, 400, "pink", Rosita_ajustes, 3, True)
        self.show_dialog(usuario)

    def btn_ranking(self, texto):
        ranking = FormRanking(self._master, 493, 230, 500, 550, "pink", Rosita_ajustes, 3, True)
        self.show_dialog(ranking)