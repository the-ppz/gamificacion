import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

fuente_titulo = pygame.font.Font(None, 74)
fuente_texto = pygame.font.Font(None, 36)

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

        pantalla.fill(BLANCO)
        mostrar_texto(pantalla, "Equipo de Desarrolladores", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        desarrolladores = [
            "Franklin Alvarez - 6854",
            "Sebastián Peñaherrera - 6835",
            "Cesar Ayala - 6814",
            "Bryan Castelo - 6866"
        ]

        for i, desarrollador in enumerate(desarrolladores):
            mostrar_texto(pantalla, desarrollador, fuente_texto, NEGRO, (ANCHO // 2, 150 + i * 50))

        mostrar_texto(pantalla, "Presiona Enter o ESC para volver", fuente_texto, NEGRO, (ANCHO // 2, ALTO - 50))

        pygame.display.flip()
