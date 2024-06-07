from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *

from ZZ_niveles import *
from ZZ_sql import *

Rosa_Bordes = (235,182,250)
Rosa_centro = (252,144,221)
LightCoral = (240,128,128)
Salmon = (250,128,114)


class FormDatos(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        #self.txtbox = TextBox(self._slave, x, y ,50, 50, 150, 30, "Blue", "Orange", "Pink", "Red", 2, font = "Comic Sans", font_size=15, font_color= "Black")

        self.titulo = Label(self._slave, 100, 17, 250, 80, "", "Verdana", 0, Salmon, "sin_fondo\Titulo_usuario.png")
        self.usuario = Label(self._slave, 20, 150, 150, 40, "Ingrese el usuario", "Verdana", 15, "White", "sin_fondo\\nada.png")

        self.nombre_jugador = TextBox(self._slave, x, y, 180, 150, 150, 30, Rosa_centro, (235,182,250), "White", "White", 2, font = "Comic Sans", font_size=15, font_color= "White" )
        self.niveles = Button_Image(self._slave, x, y, 280, 320, 140, 40, "sin_fondo\\fHello_KItty_Adventure__2_-removebg-preview.png", self.btn_play, "Niveles")
        self._btn_home = Button_Image(screen=self._slave, x=100, y=320, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")

        self.lista_widgets.append(self.titulo)
        self.lista_widgets.append(self.usuario)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.nombre_jugador)
        self.lista_widgets.append(self.niveles)

        self.render()

    def btn_play(self, texto):
        nombre_jugador = self.nombre_jugador.get_text()
        if nombre_jugador:
            gestionar_base_datos(nombre_jugador, 0)  # Guardar el nombre del jugador en la base de datos con un puntaje inicial de 0
            niveles = FormNiveles(self._master, 493, 229, 500, 550, (220,0,220), True, "Imagenes\\nada.png")
            self.show_dialog(niveles)
            print(f"{nombre_jugador}")

    def btn_home_click(self, param): #Volver a los ajustes 
        self.end_dialog() 

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                self.render()
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
        else:
            self.hijo.update(lista_eventos)