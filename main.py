import pygame
import sys
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.minijuego import minijuego
from pantallas.preguntas_respuestas import juego_preguntas

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("EXPLORADORES DEL TIEMPO - ECUADOR")

def main():
    while True:
        pantalla_inicio(pantalla, ANCHO, ALTO)
        nivel = seleccion_niveles(pantalla, ANCHO, ALTO)
        if nivel == "Minijuego":
            minijuego(pantalla, ANCHO, ALTO)
        else:
            puntuacion = pantalla_juego(pantalla, ANCHO, ALTO, nivel)
            juego_preguntas(pantalla, ANCHO, ALTO, nivel, puntuacion)
        mostrar_leaderboard(pantalla, ANCHO, ALTO)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
