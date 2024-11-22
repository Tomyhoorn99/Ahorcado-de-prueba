import pygame

def imprimir_fondo(window, ancho, alto):
    """Imprime el fondo del juego."""
    try:
        # Cargar y escalar la imagen de fondo
        fondo = pygame.image.load("imagenes/fondo.jpg")
        fondo = pygame.transform.scale(fondo, (ancho, alto))
        window.blit(fondo, (0, 0))
    except FileNotFoundError:
        # Fondo de respaldo si no se encuentra la imagen
        window.fill((0, 0, 0))  # Fondo negro

def dibujar_ahorcado(window, vidas_restantes):
    """Dibuja el muñeco del ahorcado según las vidas restantes."""
    # Coordenadas base para el dibujo
    x, y = 100, 300

    # Dibujar base del ahorcado
    pygame.draw.line(window, (255, 255, 255), (x, y+200), (x+200, y+200), 3)
    pygame.draw.line(window, (255, 255, 255), (x+100, y), (x+100, y+200), 3)
    pygame.draw.line(window, (255, 255, 255), (x+100, y), (x+200, y), 3)
    pygame.draw.line(window, (255, 255, 255), (x+200, y), (x+200, y+50), 3)

    # Dibujar partes del cuerpo según vidas
    if vidas_restantes <= 5:  # Cabeza
        pygame.draw.circle(window, (255, 255, 255), (x+200, y+75), 25, 2)
    
    if vidas_restantes <= 4:  # Torso
        pygame.draw.line(window, (255, 255, 255), (x+200, y+100), (x+200, y+150), 2)
    
    if vidas_restantes <= 3:  # Brazo izquierdo
        pygame.draw.line(window, (255, 255, 255), (x+200, y+120), (x+170, y+100), 2)
    
    if vidas_restantes <= 2:  # Brazo derecho
        pygame.draw.line(window, (255, 255, 255), (x+200, y+120), (x+230, y+100), 2)
    
    if vidas_restantes <= 1:  # Pierna izquierda
        pygame.draw.line(window, (255, 255, 255), (x+200, y+150), (x+170, y+180), 2)
    
    if vidas_restantes == 0:  # Pierna derecha
        pygame.draw.line(window, (255, 255, 255), (x+200, y+150), (x+230, y+180), 2)