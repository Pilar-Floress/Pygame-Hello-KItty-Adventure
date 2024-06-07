# from GUI_button import *
# from GUI_slider import *
# from GUI_textbox import *
# from GUI_label import *
# from GUI_form import *
# from GUI_button_image import *

# import pygame
# import sys


# from nivel_1 import *
# from nivel_2 import *
# from ZZ_manejador import *
# from ZZ_FormContenedor import *
# # from ZZ_niveles import FormNiveles


# Rosa_Bordes = (235,182,250)
# Rosa_centro = (252,144,221)
# LightCoral = (240,128,128)
# Salmon = (250,128,114)

# class PausaForm(Form):
#     def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
#         super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
#         self.titulo = Label(self._slave, 115, 10, 250, 80, "", "Verdana", 0, Salmon, "sin_fondo\Pausa.png")
#         self._btn_home = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")
#         self.jugar = Button_Image(screen=self._slave, x=100, y=100, master_x=x, master_y=y, 
#                                 w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), 
#                                 onclick=self.jugar_dnv, onclick_param="", text="", font="Verdana", 
#                                 font_size=15, font_color=(0,255,0), 
#                                 path_image="sin_fondo\Inicio_opciones-removebg-preview.png")

#         self.lista_widgets.append(self.titulo)
#         self.lista_widgets.append(self._btn_home)
#         self.lista_widgets.append(self.jugar)
#         self.render()
    
#     def btn_home_click(self, param): #Volver a los ajustes 
#         niveles = FormNiveles(self._master, 493, 229, 500, 550, (220,0,220), True, "Imagenes\\nada.png")
#         self.show_dialog(niveles)
#         self.end_dialog()

#     def jugar_dnv(self, param):
#         self.end_dialog()

#     def render(self):
#         self._slave.fill(self._color_background)

#     def update(self, lista_eventos):
#         if self.active:
#             self.draw()
#             self.render()
#             for wid in self.lista_widgets:
#                 wid.update(lista_eventos)
