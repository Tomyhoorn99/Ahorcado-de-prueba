import pygame
import sys
from funciones.ahorcado import JuegoAhorcado
from funciones.interfaz import imprimir_fondo
from funciones.utils import leer_json
import random

# Inicialización pygame
pygame.init()
pygame.mixer.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ahorcado Fisura")

# Configuración de sonido
sonido_fondo = pygame.mixer.Sound("sonido/haudio_terror.mp3")
sonido_fondo.play(-1)

# Lectura de datos palabras 
palabras = leer_json("json/palabras.json", "ahorcado")
palabras_idioma = palabras.get("ES", [])
palabra = random.choice(palabras_idioma)

# Inicializar juego
juego = JuegoAhorcado(palabra, window)

# Bucle principal
running = True
estado_juego = 'jugando'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if estado_juego == 'jugando' and event.type == pygame.KEYDOWN:
            letra = pygame.key.name(event.key)
            juego.procesar_letra(letra)
            estado_juego = juego.verificar_estado()
    
    # Renderizar fondo
    imprimir_fondo(window, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Renderizar elementos del juego
    juego.mostrar_palabra()
    juego.mostrar_vidas()
    juego.mostrar_letras_incorrectas()
    
    # Manejar estados del juego
    if estado_juego == 'victoria':
        texto_victoria = juego.fuente.render("¡GANASTE!", True, (0, 255, 0))
        texto_rect = texto_victoria.get_rect(center=(500, 400))
        window.blit(texto_victoria, texto_rect)
    
    if estado_juego == 'derrota':
        texto_derrota = juego.fuente.render(f"¡PERDISTE! La palabra era: {palabra}", True, (255, 0, 0))
        texto_rect = texto_derrota.get_rect(center=(500, 400))
        window.blit(texto_derrota, texto_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()