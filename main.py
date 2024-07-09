import pygame
import sys
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego
from pantallas.minijuego import minijuego
from pantallas.preguntas_respuestas import juego_preguntas
from pantallas.leaderboard import mostrar_leaderboard

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
        elif nivel == "Nivel 1: Historia Antigua":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 1: Historia Antigua", puntuacion)
        elif nivel == "Nivel 2: Cultura Colonial":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 2: Cultura Colonial", puntuacion)
        elif nivel == "Nivel 3: Independencia":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 3: Independencia", puntuacion)
        else:
            pantalla_juego(pantalla, ANCHO, ALTO, nivel)
            
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
