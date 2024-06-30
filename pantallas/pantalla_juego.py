import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

fondos = {
    "Nivel 1: Historia Antigua": pygame.image.load('src/logo_juego.jpg'),
    "Nivel 2: Cultura Colonial": pygame.image.load('src/logo_juego.jpg'),
    "Nivel 3: Independencia": pygame.image.load('src/logo_juego.jpg')
}

jugador_img = pygame.image.load('src/jugador.png')
obstaculo_img = pygame.image.load('src/obstaculo.png')

fuente_puntuacion = pygame.font.Font(None, 36)

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_juego(pantalla, ANCHO, ALTO, nivel):
    jugador_rect = jugador_img.get_rect()
    jugador_rect.topleft = (ANCHO // 2, ALTO - 100)
    velocidad_jugador = 5

    obstaculos = [pygame.Rect(ANCHO // 4, ALTO - 200, 50, 50),
                  pygame.Rect(ANCHO // 2, ALTO - 300, 50, 50),
                  pygame.Rect(3 * ANCHO // 4, ALTO - 400, 50, 50)]

    puntuacion = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and jugador_rect.top > 0:
            jugador_rect.y -= velocidad_jugador
        if teclas[pygame.K_DOWN] and jugador_rect.bottom < ALTO:
            jugador_rect.y += velocidad_jugador
        if teclas[pygame.K_LEFT] and jugador_rect.left > 0:
            jugador_rect.x -= velocidad_jugador
        if teclas[pygame.K_RIGHT] and jugador_rect.right < ANCHO:
            jugador_rect.x += velocidad_jugador

        # Actualizar la pantalla
        pantalla.blit(fondos[nivel], (0, 0))

        # Dibujar el jugador
        pantalla.blit(jugador_img, jugador_rect.topleft)

        # Dibujar los obstáculos
        for obstaculo in obstaculos:
            pantalla.blit(obstaculo_img, obstaculo.topleft)

        # Mostrar la puntuación
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente_puntuacion, NEGRO, (100, 50))

        pygame.display.flip()
