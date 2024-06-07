import pygame
import pygame.locals
import sys

# Inicializar pygame
pygame.init()

# Establecer los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Establecer el tamaño de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Cronómetro")

# Crear el reloj para controlar las actualizaciones de tiempo
reloj = pygame.time.Clock()

# Variables para el cronómetro
tiempo_inicial = pygame.time.get_ticks()
tiempo_transcurrido = 0

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcular el tiempo transcurrido
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    # Limpiar la pantalla
    ventana.fill(NEGRO)

    # Mostrar el tiempo transcurrido en la ventana
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(str(tiempo_transcurrido // 1000), True, BLANCO)
    ventana.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))

    # Actualizar la ventana
    pygame.display.update()

    # Establecer el límite de frames por segundo
    reloj.tick(60)