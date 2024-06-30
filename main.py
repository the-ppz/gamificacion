import pygame
import sys
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("EXPLORADORES DEL TIEMPO - ECUADOR")

def main():
    pantalla_inicio(pantalla, ANCHO, ALTO)
    nivel = seleccion_niveles(pantalla, ANCHO, ALTO)
    print(f"Nivel seleccionado: {nivel}")
    pantalla_juego(pantalla, ANCHO, ALTO, nivel)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
