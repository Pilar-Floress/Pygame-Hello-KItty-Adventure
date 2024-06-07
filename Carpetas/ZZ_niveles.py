from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *

import pygame
import sys
# from AA_Kitty import *
# from Modulo import *
# from CC_Pantalla import *
# from DD_Plataformas import *
# from AA_Enemigos import *
# from CC_Recolectar import *
# from CC_textos import *
# from AA_trampas import *
# from AA_kittana import *
# from CC_Barra import *

from nivel_1 import *
from nivel_2 import *
from ZZ_manejador import *
from ZZ_FormContenedor import *



class FormNiveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, active)
        self.manejador_niveles = ManejadorNiveles(self._slave)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.btn_Uno = Button_Image(screen=self._slave, x=140, y=180, master_x=x, master_y=y, w=80, h=60, color_background=(255,0,0), color_border=(255,0,255), onclick=self.manejador_nivel, onclick_param="Nivel_1", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__6_-removebg-preview.png")
        self.btn_Dos = Button_Image(screen=self._slave, x=280, y=180, master_x=x, master_y=y, w=80, h=60, color_background=(255,0,0), color_border=(255,0,255), onclick=self.manejador_nivel, onclick_param="Nivel_2", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__7_-removebg-preview.png")
        self.btn_Tres = Button_Image(screen=self._slave, x=140, y=300, master_x=x, master_y=y, w=80, h=60, color_background=(255,0,0), color_border=(255,0,255), onclick=self.manejador_nivel, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__8_-removebg-preview.png")
        self.btn_Cuatro = Button_Image(screen=self._slave, x=280, y=300, master_x=x, master_y=y, w=80, h=60, color_background=(255,0,0), color_border=(255,0,255), onclick=self.manejador_nivel, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__9_-removebg-preview.png")

        # self.btn_Dos = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_nivel_uno, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="Imagenes\Uno_img.jpg")
        self._btn_home = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")


        self.lista_widgets.append(self.btn_Uno)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.btn_Dos)
        self.lista_widgets.append(self.btn_Tres)
        self.lista_widgets.append(self.btn_Cuatro)

    # def pausa(self):
    #     pausa = PausaForm()

    def btn_home_click(self, param): #Volver a los ajustes 
        self.end_dialog() 

    def manejador_nivel(self, numero_nivel):
        nivel = self.manejador_niveles.get_nivel(numero_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for wid in self.lista_widgets:
                    wid.update(lista_eventos)
                self.draw()    
        else:
            self.hijo.update(lista_eventos)
            





















