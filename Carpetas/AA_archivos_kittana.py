import pygame
from BB_Modificacion_imagenes import *
from CC_Pantalla import *


lista_kittana_caminar_d = [pygame.image.load("Kittana\\0.png"),
                            pygame.image.load("Kittana\\0.png"),
                            pygame.image.load("Kittana\\2.png"),
                            pygame.image.load("Kittana\\2.png"),
                            pygame.image.load("Kittana\\1.png"),
                            pygame.image.load("Kittana\\1.png")]


lista_kittana_caminar_i = girar_imagenes(lista_kittana_caminar_d, True, False)

lista_kittana_ataques_d = [pygame.image.load("Kittana\Ataque_cero.png"), 
                        pygame.image.load("Kittana\Ataque_cero.png"),
                        pygame.image.load("Kittana\Ataque_cero.png"),
                        pygame.image.load("Kittana\Ataque_uno.png"),
                        pygame.image.load("Kittana\Ataque_uno.png"),
                        pygame.image.load("Kittana\Ataque_uno.png")]

lista_kittana_ataques_i = girar_imagenes(lista_kittana_ataques_d, True, False)


diccionario_kittana_movimientos = {}
diccionario_kittana_movimientos["Derecha"] = lista_kittana_caminar_d
diccionario_kittana_movimientos["Izquierda"] = lista_kittana_caminar_i
diccionario_kittana_movimientos["Ataque D"] = lista_kittana_ataques_d
diccionario_kittana_movimientos["Ataque I"] = lista_kittana_ataques_i

