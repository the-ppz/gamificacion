import pygame
import sys
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.minijuego import minijuego

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("EXPLORADORES DEL TIEMPO - ECUADOR")

def main():
    while True:
        pantalla_inicio(pantalla, ANCHO, ALTO)
        nivel = seleccion_niveles(pantalla, ANCHO, ALTO)
        if nivel == "Minijuego":
            puntuacion = minijuego(pantalla, ANCHO, ALTO)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "minijuego", puntuacion)
        else:
            puntuacion = pantalla_juego(pantalla, ANCHO, ALTO, nivel)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "preguntas", puntuacion)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
