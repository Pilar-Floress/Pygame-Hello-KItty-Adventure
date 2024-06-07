from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *



class GanarForm(Form):
    def __init__(self, screen, x, y, w, h, color_background, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, active)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen

        self.titulo = Label(self._slave, x, y, w, h, "", "Verdana", 0, "White", "Imagenes\You_Win.png")
        self._btn_home = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")

        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.titulo)


    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()  









