import pygame
import sys
import os

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL_CLARO = (173, 216, 230)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

fondo = pygame.image.load(resource_path('src/fondo_inicio.jpg'))

fuente_titulo = pygame.font.Font(None, 74)
fuente_texto = pygame.font.Font(None, 36)
fuente_nombre = pygame.font.Font(None, 42)

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_equipo(pantalla, ANCHO, ALTO):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_ESCAPE:
                    return

        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, "Equipo de Desarrolladores", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        desarrolladores = [
            "Franklin Alvarez - 6854",
            "Sebastián Peñaherrera - 6835",
            "Cesar Ayala - 6814",
            "Bryan Castelo - 6866"
        ]

        for i, desarrollador in enumerate(desarrolladores):
            mostrar_texto(pantalla, desarrollador, fuente_nombre, NEGRO, (ANCHO // 2, 150 + i * 60))

        mostrar_texto(pantalla, "Presiona Enter o ESC para volver", fuente_texto, ROJO, (ANCHO // 2, ALTO - 50))

        pygame.display.flip()
