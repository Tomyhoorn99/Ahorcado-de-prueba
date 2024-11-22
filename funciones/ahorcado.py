import pygame
import random

class JuegoAhorcado:
    def __init__(self, palabra, screen):
        self.palabra = palabra.lower()
        self.screen = screen
        self.vidas = 6
        self.letras_adivinadas = set()
        self.letras_incorrectas = set()
        self.fuente = pygame.font.Font(None, 50)
        self.estado_palabra = ['_' if c.isalpha() else c for c in self.palabra]

    def mostrar_palabra(self):
        texto_palabra = ' '.join(self.estado_palabra)
        texto_surface = self.fuente.render(texto_palabra, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=(500, 200))
        self.screen.blit(texto_surface, texto_rect)

    def mostrar_vidas(self):
        texto_vidas = f"Vidas: {self.vidas}"
        texto_surface = self.fuente.render(texto_vidas, True, (255, 0, 0))
        texto_rect = texto_surface.get_rect(center=(500, 100))
        self.screen.blit(texto_surface, texto_rect)

    def mostrar_letras_incorrectas(self):
        texto_incorrectas = f"Letras incorrectas: {' '.join(self.letras_incorrectas)}"
        texto_surface = self.fuente.render(texto_incorrectas, True, (255, 255, 255))
        texto_rect = texto_surface.get_rect(center=(500, 250))
        self.screen.blit(texto_surface, texto_rect)

    def procesar_letra(self, letra):
        letra = letra.lower()
        if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
            return False

        if letra in self.palabra:
            self.letras_adivinadas.add(letra)
            for i, char in enumerate(self.palabra):
                if char == letra:
                    self.estado_palabra[i] = letra
        else:
            self.letras_incorrectas.add(letra)
            self.vidas -= 1

        return True

    def verificar_estado(self):
        if '_' not in self.estado_palabra:
            return 'victoria'
        elif self.vidas <= 0:
            return 'derrota'
        return 'jugando'

def manejar_eventos(event, window, palabras, teclas, vidas, puntos, palabra, idioma):
    """Maneja los eventos principales del juego."""
    pass