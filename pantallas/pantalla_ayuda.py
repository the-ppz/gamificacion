import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

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

        pantalla.fill(BLANCO)
        mostrar_texto(pantalla, "Ayuda", fuente_titulo, NEGRO, (ANCHO // 2, 50))
        mostrar_texto(pantalla, "Usa las flechas para moverte", fuente_texto, NEGRO, (ANCHO // 2, 150))
        mostrar_texto(pantalla, "Presiona Enter para seleccionar", fuente_texto, NEGRO, (ANCHO // 2, 200))
        mostrar_texto(pantalla, "Presiona P para pausar", fuente_texto, NEGRO, (ANCHO // 2, 250))
        mostrar_texto(pantalla, "Presiona ESC para salir", fuente_texto, NEGRO, (ANCHO // 2, 300))
        mostrar_texto(pantalla, "Presiona Enter para volver", fuente_texto, ROJO, (ANCHO // 2, ALTO - 50))

        pygame.display.flip()
