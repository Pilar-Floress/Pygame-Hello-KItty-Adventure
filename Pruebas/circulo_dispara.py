import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini programa con clases")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Clase del círculo
class Circulo:
    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio
        self.velocidad = 0.5
        self.direccion = None
        self.disparando = False
    
    def dibujar(self):
        pygame.draw.circle(VENTANA, ROJO, (self.x, self.y), self.radio)
    
    def mover(self, direccion):
        if direccion == "IZQUIERDA":
            self.x -= self.velocidad
        elif direccion == "DERECHA":
            self.x += self.velocidad
        elif direccion == "ARRIBA":
            self.y -= self.velocidad
        elif direccion == "ABAJO":
            self.y += self.velocidad
        
        # Guardar la dirección actual del movimiento
        self.direccion = direccion
    
    def disparar(self):
        if not self.disparando:
            self.disparando = True
    
    def dejar_de_disparar(self):
        self.disparando = False

class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 1

    def actualizar(self):
        self.y -= self.velocidad
    
    def dibujar(self):
        pygame.draw.circle(VENTANA, BLANCO, (self.x, self.y), 5)

def cronometro():
    pass




pygame.font.init()
color_blanco = (255, 255, 255)

def crear_texto(pantalla, texto, posicion, color, tamaño):
    Formato = pygame.font.Font(None, tamaño)
    texto = Formato.render(texto, True, color)
    pantalla.blit(texto, posicion)




# Crear el círculo y los proyectiles
circulo = Circulo(ANCHO // 2, ALTO // 2, 25)

proyectiles = []

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        circulo.mover("DERECHA")
    elif keys[pygame.K_LEFT]:
        circulo.mover("IZQUIERDA")
    elif keys[pygame.K_UP]:
        circulo.mover("ARRIBA")
    elif keys[pygame.K_DOWN]:
        circulo.mover("ABAJO")
    elif keys[pygame.K_SPACE]:
        circulo.disparar()
    else:
        circulo.dejar_de_disparar()
    
    # Disparar un proyectil
    if circulo.disparando:
        proyectil = Proyectil(circulo.x, circulo.y - circulo.radio)
        proyectiles.append(proyectil)
        circulo.dejar_de_disparar()
    
    # Actualizar la posición de los proyectiles
    for proyectil in proyectiles:
        proyectil.actualizar()
    
    # Eliminar los proyectiles que salgan de la pantalla
    proyectiles = [proyectil for proyectil in proyectiles if proyectil.y > 0]
    
    # Actualizar la pantalla
    VENTANA.fill((0, 0, 0))
    
    for proyectil in proyectiles:
        proyectil.dibujar()
    
    circulo.dibujar()
    
    pygame.display.flip()