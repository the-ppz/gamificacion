import pygame
import sys
from .preguntas_respuestas import juego_preguntas  # Importa el módulo correctamente

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

fuente_pregunta = pygame.font.Font(None, 36)
fuente_respuesta = pygame.font.Font(None, 28)

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_juego(pantalla, ANCHO, ALTO, nivel):
    puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0)
    return puntuacion

def main():
    ANCHO, ALTO = 800, 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego de Preguntas")

    nivel = "Nivel 1: Historia Antigua"  # Puedes cambiar esto para probar diferentes niveles

    puntuacion = pantalla_juego(pantalla, ANCHO, ALTO, nivel)
    print(f"Puntuación: {puntuacion}")  # Puedes reemplazar esto con la llamada al leaderboard

if __name__ == "__main__":
    main()
