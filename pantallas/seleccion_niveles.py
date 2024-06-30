import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

fuente_titulo = pygame.font.Font(None, 74)
fuente_niveles = pygame.font.Font(None, 36)

niveles = ["Nivel 1: Historia Antigua", "Nivel 2: Cultura Colonial", "Nivel 3: Independencia"]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def seleccion_niveles(pantalla, ANCHO, ALTO):
    nivel_seleccionado = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    nivel_seleccionado = (nivel_seleccionado - 1) % len(niveles)
                elif evento.key == pygame.K_DOWN:
                    nivel_seleccionado = (nivel_seleccionado + 1) % len(niveles)
                elif evento.key == pygame.K_RETURN:
                    return niveles[nivel_seleccionado] 

        pantalla.fill(BLANCO)

        mostrar_texto(pantalla, "Selecciona un Nivel", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        for i, nivel in enumerate(niveles):
            color = ROJO if i == nivel_seleccionado else NEGRO
            mostrar_texto(pantalla, nivel, fuente_niveles, color, (ANCHO // 2, 150 + i * 50))

        pygame.display.flip()
