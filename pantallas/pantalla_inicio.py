import pygame
import sys
from pantallas.experiencia import obtener_nivel_experiencia, cargar_experiencia

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

fondo = pygame.image.load('src/fondo_inicio.jpg')
logo = pygame.image.load('src/logo_juego.png')

fuente_titulo = pygame.font.Font(None, 74)
fuente_opciones = pygame.font.Font(None, 36)
fuente_nivel = pygame.font.Font(None, 28)

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_inicio(pantalla, ANCHO, ALTO):
    puntos_experiencia = cargar_experiencia()
    nivel_experiencia = obtener_nivel_experiencia(puntos_experiencia)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return 

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(logo, (ANCHO // 2 - logo.get_width() // 2, 50))

        mostrar_texto(pantalla, "Historia y Cultura Local", fuente_titulo, NEGRO, (ANCHO // 2, ALTO // 2))
        mostrar_texto(pantalla, "Presiona Enter para comenzar", fuente_opciones, ROJO, (ANCHO // 2, ALTO // 2 + 100))
        
        mostrar_texto(pantalla, f"Nivel: {nivel_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 50))
        mostrar_texto(pantalla, f"XP: {puntos_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 20))

        #pygame.draw.circle(pantalla, AZUL, (ANCHO // 2, ALTO - 50), 20, 0)
        pygame.display.flip()
