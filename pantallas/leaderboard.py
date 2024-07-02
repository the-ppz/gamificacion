import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

fuente_leaderboard = pygame.font.Font(None, 48)

# Datos ficticios para el leaderboard
leaderboard_data = [
    ("Jugador1", 5000),
    ("Jugador2", 4500),
    ("Jugador3", 4000),
    ("Jugador4", 3500),
    ("Jugador5", 3000),
]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def mostrar_leaderboard(pantalla, ANCHO, ALTO):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_ESCAPE:
                    return

        pantalla.fill(BLANCO)

        mostrar_texto(pantalla, "Leaderboard", fuente_leaderboard, NEGRO, (ANCHO // 2, 50))

        for i, (jugador, puntuacion) in enumerate(leaderboard_data):
            texto = f"{i + 1}. {jugador} - {puntuacion} puntos"
            mostrar_texto(pantalla, texto, fuente_leaderboard, NEGRO, (ANCHO // 2, 150 + i * 50))

        mostrar_texto(pantalla, "Presiona Enter para continuar", fuente_leaderboard, NEGRO, (ANCHO // 2, ALTO - 50))

        pygame.display.flip()
