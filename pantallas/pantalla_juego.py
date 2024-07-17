import pygame
import sys
import random
import os
from pantallas.experiencia import obtener_nivel_experiencia

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

fuente_puntuacion = pygame.font.Font(None, 36)
fuente_pausa = pygame.font.Font(None, 48)
fuente_game_over = pygame.font.Font(None, 74)

jugador_img = pygame.image.load(resource_path('src/principiante.png'))
jugador_img = pygame.transform.scale(jugador_img, (50, 50))
obstaculo_img = pygame.image.load(resource_path('src/obstaculo.png'))
obstaculo_img = pygame.transform.scale(obstaculo_img, (50, 50))
moneda_img = pygame.image.load(resource_path('src/moneda.png'))
moneda_img = pygame.transform.scale(moneda_img, (25, 25))

fondos = {
    "Nivel 1: Historia Antigua": pygame.image.load(resource_path('src/fondo_inicio.jpg')),
    "Nivel 2: Cultura Colonial": pygame.image.load(resource_path('src/fondo_inicio.jpg')),
    "Nivel 3: Independencia": pygame.image.load(resource_path('src/fondo_inicio.jpg'))
}

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_juego(pantalla, ANCHO, ALTO, nivel, puntos_experiencia):
    # Configuración inicial del jugador
    jugador_rect = jugador_img.get_rect()
    jugador_rect.topleft = (ANCHO // 2, ALTO - 100)
    velocidad_jugador = 5

    # Configuración inicial de los obstáculos y monedas
    obstaculos = [pygame.Rect(random.randint(0, ANCHO - 50), random.randint(-500, 0), 50, 50) for _ in range(5)]
    monedas = [pygame.Rect(random.randint(0, ANCHO - 25), random.randint(-500, 0), 25, 25) for _ in range(10)]

    puntuacion = 0
    puntos_compensables = 0
    monedas_recolectadas = 0
    velocidad_obstaculo = 2
    pausa = False
    game_over = False
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausa = not pausa
                if evento.key == pygame.K_ESCAPE:
                    return puntuacion, puntos_experiencia
                if evento.key == pygame.K_m:
                    return puntuacion, puntos_experiencia

        if not pausa and not game_over:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and jugador_rect.left > 0:
                jugador_rect.x -= velocidad_jugador
            if teclas[pygame.K_RIGHT] and jugador_rect.right < ANCHO:
                jugador_rect.x += velocidad_jugador

            for obstaculo in obstaculos:
                obstaculo.y += velocidad_obstaculo
                if obstaculo.top > ALTO:
                    obstaculo.topleft = (random.randint(0, ANCHO - 50), random.randint(-500, 0))
                    puntuacion += 50
                    puntos_experiencia += 50
                    velocidad_obstaculo += 0.1

            for moneda in monedas:
                moneda.y += velocidad_obstaculo
                if moneda.top > ALTO:
                    moneda.topleft = (random.randint(0, ANCHO - 25), random.randint(-500, 0))

            for obstaculo in obstaculos:
                if jugador_rect.colliderect(obstaculo):
                    game_over = True

            for moneda in monedas:
                if jugador_rect.colliderect(moneda):
                    monedas.remove(moneda)
                    monedas.append(pygame.Rect(random.randint(0, ANCHO - 25), random.randint(-500, 0), 25, 25))
                    monedas_recolectadas += 1
                    puntos_compensables += 20

            pantalla.blit(fondos[nivel], (0, 0))
            pantalla.blit(jugador_img, jugador_rect.topleft)
            for obstaculo in obstaculos:
                pantalla.blit(obstaculo_img, obstaculo.topleft)
            for moneda in monedas:
                pantalla.blit(moneda_img, moneda.topleft)

            mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente_puntuacion, NEGRO, (100, 50))
            mostrar_texto(pantalla, f"Puntos Compensables: {puntos_compensables}", fuente_puntuacion, NEGRO, (100, 80))
            mostrar_texto(pantalla, f"Monedas: {monedas_recolectadas}", fuente_puntuacion, NEGRO, (100, 110))
            mostrar_texto(pantalla, "Presiona M para Minijuego", fuente_puntuacion, ROJO, (ANCHO // 2, ALTO - 50))

            nivel_experiencia = obtener_nivel_experiencia(puntos_experiencia)
            mostrar_texto(pantalla, f"Nivel: {nivel_experiencia}", fuente_puntuacion, NEGRO, (ANCHO - 150, 50))
            mostrar_texto(pantalla, f"XP: {puntos_experiencia}", fuente_puntuacion, NEGRO, (ANCHO - 150, 80))
            
        elif game_over:
            mostrar_texto(pantalla, "GAME OVER", fuente_game_over, ROJO, (ANCHO // 2, ALTO // 2))
            mostrar_texto(pantalla, "Presiona ESC para regresar al menú", fuente_pausa, ROJO, (ANCHO // 2, ALTO // 2 + 100))
        else:
            mostrar_texto(pantalla, "Juego en Pausa", fuente_pausa, ROJO, (ANCHO // 2, ALTO // 2))

        pygame.display.flip()
        reloj.tick(60)
