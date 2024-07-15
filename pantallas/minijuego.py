import pygame
import sys
import random
import json

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Cargar imágenes de fondo según el nivel
fondos = {
    "Nivel 1: Historia Antigua": pygame.image.load('src/fondo_inicio.jpg'),
    "Nivel 2: Cultura Colonial": pygame.image.load('src/fondo_inicio.jpg'),
    "Nivel 3: Independencia": pygame.image.load('src/fondo_inicio.jpg')
}

# Cargar y escalar imágenes del jugador, obstáculos y monedas
personajes = {
    "Principiante": pygame.transform.scale(pygame.image.load('src/principiante.png'), (120, 100)),
    "Aprendiz": pygame.transform.scale(pygame.image.load('src/aprendiz.png'), (120, 100)),
    "Historico": pygame.transform.scale(pygame.image.load('src/historico.png'), (120, 100)),
    "Erudito": pygame.transform.scale(pygame.image.load('src/erudito.png'), (120, 100)),
    "Sabio": pygame.transform.scale(pygame.image.load('src/sabio.png'), (120, 100))
}

obstaculo_img = pygame.image.load('src/obstaculo.png')
obstaculo_img = pygame.transform.scale(obstaculo_img, (50, 50))

moneda_img = pygame.image.load('src/moneda.png')
moneda_img = pygame.transform.scale(moneda_img, (25, 25))

# Definición de fuentes
fuente_puntuacion = pygame.font.Font(None, 28)
fuente_pausa = pygame.font.Font(None, 48)
fuente_game_over = pygame.font.Font(None, 74)

# Definición de niveles de experiencia
niveles_experiencia = {
    "Principiante": 0,
    "Aprendiz": 500,
    "Historico": 1000,
    "Erudito": 1500,
    "Sabio": 2000
}

def obtener_nivel_experiencia(puntos_experiencia):
    if puntos_experiencia >= niveles_experiencia["Sabio"]:
        return "Sabio"
    elif puntos_experiencia >= niveles_experiencia["Erudito"]:
        return "Erudito"
    elif puntos_experiencia >= niveles_experiencia["Historico"]:
        return "Historico"
    elif puntos_experiencia >= niveles_experiencia["Aprendiz"]:
        return "Aprendiz"
    else:
        return "Principiante"

def guardar_experiencia(puntos_experiencia=0):
    with open('experiencia.json', 'w') as archivo:
        json.dump({"puntos_experiencia": puntos_experiencia}, archivo)

def cargar_experiencia():
    try:
        with open('experiencia.json', 'r') as archivo:
            datos = json.load(archivo)
            return datos["puntos_experiencia"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def minijuego(pantalla, ANCHO, ALTO, dificultad):
    # Cargar la experiencia y determinar el nivel
    puntos_experiencia = cargar_experiencia()
    nivel_experiencia = obtener_nivel_experiencia(puntos_experiencia)
    jugador_img = personajes[nivel_experiencia]
    
    # Configuración inicial del jugador
    jugador_rect = jugador_img.get_rect()
    jugador_rect.topleft = (ANCHO // 2, ALTO - 100)
    
    if dificultad == 0:  # Fácil
        velocidad_jugador = 7
        velocidad_obstaculo = 2
    elif dificultad == 1:  # Medio
        velocidad_jugador = 5
        velocidad_obstaculo = 4
    else:  # Difícil
        velocidad_jugador = 3
        velocidad_obstaculo = 6

    # Configuración inicial de los obstáculos y monedas
    obstaculos = [pygame.Rect(random.randint(0, ANCHO - 50), random.randint(-500, 0), 50, 50) for _ in range(5)]
    monedas = [pygame.Rect(random.randint(0, ANCHO - 25), random.randint(-500, 0), 25, 25) for _ in range(10)]

    puntuacion = 0
    puntos_compensables = 0
    monedas_recolectadas = 0
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
                    guardar_experiencia(puntuacion + puntos_experiencia)
                    return puntuacion
                if evento.key == pygame.K_m:  # Tecla M para ir al minijuego
                    return "Minijuego"

        if not pausa and not game_over:
            # Movimiento del jugador
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and jugador_rect.left > 0:
                jugador_rect.x -= velocidad_jugador
            if teclas[pygame.K_RIGHT] and jugador_rect.right < ANCHO:
                jugador_rect.x += velocidad_jugador

            # Movimiento de los obstáculos
            for obstaculo in obstaculos:
                obstaculo.y += velocidad_obstaculo
                if obstaculo.top > ALTO:
                    obstaculo.topleft = (random.randint(0, ANCHO - 50), random.randint(-500, 0))
                    puntuacion += 50  # Ganar puntos de experiencia
                    if dificultad == 2:  # Aumentar la velocidad gradualmente solo en difícil
                        velocidad_obstaculo += 0.1

            # Movimiento de las monedas
            for moneda in monedas:
                moneda.y += velocidad_obstaculo
                if moneda.top > ALTO:
                    moneda.topleft = (random.randint(0, ANCHO - 25), random.randint(-500, 0))

            # Detección de colisiones con obstáculos
            for obstaculo in obstaculos:
                if jugador_rect.colliderect(obstaculo):
                    game_over = True

            # Detección de recolección de monedas
            for moneda in monedas:
                if jugador_rect.colliderect(moneda):
                    monedas.remove(moneda)
                    monedas.append(pygame.Rect(random.randint(0, ANCHO - 25), random.randint(-500, 0), 25, 25))
                    monedas_recolectadas += 1
                    puntos_compensables += 20  # Ganar puntos compensables

            # Actualizar la pantalla
            pantalla.blit(fondos["Nivel 1: Historia Antigua"], (0, 0))

            # Dibujar el jugador
            pantalla.blit(jugador_img, jugador_rect.topleft)

            # Dibujar los obstáculos
            for obstaculo in obstaculos:
                pantalla.blit(obstaculo_img, obstaculo.topleft)

            # Dibujar las monedas
            for moneda in monedas:
                pantalla.blit(moneda_img, moneda.topleft)

            # Mostrar la puntuación y otros puntos
            mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente_puntuacion, NEGRO, (150, 50))
            mostrar_texto(pantalla, f"Puntos Compensables: {puntos_compensables}", fuente_puntuacion, NEGRO, (150, 80))
            mostrar_texto(pantalla, f"Monedas: {monedas_recolectadas}", fuente_puntuacion, NEGRO, (150, 110))
            mostrar_texto(pantalla, "Presiona P para Pausar", fuente_puntuacion, ROJO, (ANCHO - 150, ALTO - 50))
            mostrar_texto(pantalla, "Presiona ESC para regresar al menú", fuente_puntuacion, ROJO, (ANCHO - 170, ALTO - 80))
        elif game_over:
            mostrar_texto(pantalla, "GAME OVER", fuente_game_over, ROJO, (ANCHO // 2, ALTO // 2))
            mostrar_texto(pantalla, "Presiona ESC para regresar al menú", fuente_pausa, ROJO, (ANCHO // 2, ALTO // 2 + 100))
        else:
            mostrar_texto(pantalla, "Juego en Pausa", fuente_pausa, ROJO, (ANCHO // 2, ALTO // 2))

        pygame.display.flip()
        reloj.tick(60)  # Limitar a 60 FPS
