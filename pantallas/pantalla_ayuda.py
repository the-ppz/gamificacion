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

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_ayuda(pantalla, ANCHO, ALTO):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_ESCAPE:
                    return

        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, "Ayuda", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        instrucciones = [
            "Usa las flechas para moverte",
            "Presiona Enter para seleccionar",
            "Presiona P para pausar",
            "Presiona ESC para salir",
            "Presiona Enter para volver"
        ]

        for i, instruccion in enumerate(instrucciones):
            color = ROJO if "volver" in instruccion else NEGRO
            mostrar_texto(pantalla, instruccion, fuente_texto, color, (ANCHO // 2, 150 + i * 50))

        pygame.display.flip()
