import pygame
import sys
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.experiencia import obtener_nivel_experiencia, cargar_experiencia

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
AZUL_CLARO = (173, 216, 230)

fondo = pygame.image.load('src/fondo_inicio.jpg')

fuente_titulo = pygame.font.Font(None, 74)
fuente_niveles = pygame.font.Font(None, 36)
fuente_nivel = pygame.font.Font(None, 28)

niveles = [
    "Nivel 1: Historia Antigua",
    "Nivel 2: Cultura Colonial",
    "Nivel 3: Independencia",
    "Minijuego",
    "Clasificación Minijuego",
    "Clasificación Nivel 1",
    "Clasificación Nivel 2",
    "Clasificación Nivel 3",
    "Configuración",
    "Ayuda",
    "Equipo de Desarrolladores"
]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def seleccion_niveles(pantalla, ANCHO, ALTO, sonido_seleccion):
    nivel_seleccionado = 0
    puntos_experiencia = cargar_experiencia()
    nivel_experiencia = obtener_nivel_experiencia(puntos_experiencia)
    
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
                    pygame.mixer.Sound.play(sonido_seleccion)
                    if niveles[nivel_seleccionado] == "Clasificación Minijuego":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "minijuego")
                    elif niveles[nivel_seleccionado] == "Clasificación Nivel 1":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 1: Historia Antigua")
                    elif niveles[nivel_seleccionado] == "Clasificación Nivel 2":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 2: Cultura Colonial")
                    elif niveles[nivel_seleccionado] == "Clasificación Nivel 3":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 3: Independencia")
                    else:
                        return niveles[nivel_seleccionado]
                elif evento.key == pygame.K_ESCAPE:
                    return "pantalla_inicio"

        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, "Selecciona un Nivel", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        for i, nivel in enumerate(niveles):
            color = ROJO if i == nivel_seleccionado else NEGRO
            mostrar_texto(pantalla, nivel, fuente_niveles, color, (ANCHO // 2, 150 + i * 50))
            
        # Añadir barra de progreso de experiencia
        pygame.draw.rect(pantalla, NEGRO, (ANCHO - 210, ALTO - 30, 200, 20), 2)
        pygame.draw.rect(pantalla, AMARILLO, (ANCHO - 208, ALTO - 28,200 * puntos_experiencia / 2500, 16))
            
        mostrar_texto(pantalla, f"Nivel: {nivel_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 50))
        mostrar_texto(pantalla, f"XP: {puntos_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 20))

        pygame.display.flip()
