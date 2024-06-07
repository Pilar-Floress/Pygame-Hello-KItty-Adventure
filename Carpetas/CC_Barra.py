import pygame
from CC_textos import *

#Tiempo
def contador_reloj(tiempo_inicial, pantalla):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    minutos = tiempo_transcurrido // 60000
    segundos = (tiempo_transcurrido // 1000) % 60

    crear_texto(pantalla, f"{minutos:02d}:{segundos:02d}", (680, 10), (205, 92, 92), 40)

tiempo_inicial = pygame.time.get_ticks()



def Vidas_personaje(pantalla, personaje):
    if personaje.vidas <= 0:
        imagen_path = "Vidas\Vidas_tres.png" 
    elif personaje.vidas == 1:
        imagen_path = "Vidas\Vidas_dos.png"  
    elif personaje.vidas == 2:
        imagen_path = "Vidas\Vidas_uno.png"  
    elif personaje.vidas == 3:
        imagen_path = "Vidas\Vidas_Completas.png"  
    elif personaje.vidas == 4:
        imagen_path = "Vidas\Vidas_Completas.png" 
    
    imagen = pygame.image.load(imagen_path)  
    imagen_redimensionada = pygame.transform.scale(imagen, (100, 40)) 
    
    imagen_rect = imagen_redimensionada.get_rect()  
    imagen_rect.x = 40 
    imagen_rect.y = 5  
    # (37, 5)
    
    pantalla.blit(imagen_redimensionada, imagen_rect)


# def puntajes(pantalla, personaje):
#     puntos = "Fotos\Frutilla_nv.png"
#     frutilla_img = pygame.image.load(puntos)  
#     imagen_redimensionada_frutilla = pygame.transform.scale(frutilla_img, (40, 40)) 
    
#     rect_frutilla = imagen_redimensionada_frutilla.get_rect()  
#     rect_frutilla.x = 170
#     rect_frutilla.y = 5 

#     pantalla.blit(imagen_redimensionada_frutilla, rect_frutilla)
#     crear_texto(pantalla, f"{personaje.frutillas}", (185, 25), "Black", 20)    


def vidas_jefe(pantalla, vidas):
    if vidas <= 0:
        imagen_path = "Vidas Jefe\Jefe_muerte_vd.png" 
    elif vidas == 1:
        imagen_path = "Vidas Jefe\Jefe_cero_vd.png"  
    elif vidas == 2:
        imagen_path = "Vidas Jefe\Jefe_una_vd.png"  
    elif vidas == 3:
        imagen_path = "Vidas Jefe\Jefe_dos_vd.png"  
    elif vidas == 4:
        imagen_path = "Vidas Jefe\Jefe_cuatro_vd.png" 
    elif vidas == 5:
        imagen_path = "Vidas Jefe\Jefe_cinco_vd.png"

    imagen = pygame.image.load(imagen_path)  
    imagen_redimensionada = pygame.transform.scale(imagen, (180, 40)) 
    

    imagen_rect = imagen_redimensionada.get_rect()  
    imagen_rect.x = 890
    imagen_rect.y = 7 
    # (37, 5)
    
    pantalla.blit(imagen_redimensionada, imagen_rect)