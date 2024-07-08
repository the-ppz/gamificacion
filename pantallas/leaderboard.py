import pygame
import sys
import json
import os

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

fuente_leaderboard = pygame.font.Font(None, 48)
fuente_nombre = pygame.font.Font(None, 36)

LEADERBOARD_FILES = {
    "minijuego": "src/leaderboard_minijuego.json",
    "preguntas": "src/leaderboard_preguntas.json"
}

def verificar_crear_archivo(tipo):
    archivo = LEADERBOARD_FILES[tipo]
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            json.dump([], f)

def cargar_leaderboard(tipo):
    archivo = LEADERBOARD_FILES[tipo]
    verificar_crear_archivo(tipo)
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_leaderboard(tipo, leaderboard_data):
    archivo = LEADERBOARD_FILES[tipo]
    with open(archivo, 'w') as f:
        json.dump(leaderboard_data, f)

def pedir_nombre(pantalla, ANCHO, ALTO, puntuacion):
    nombre = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        pantalla.fill(BLANCO)
        mostrar_texto(pantalla, "Ingresa tu nombre:", fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2 - 50))
        mostrar_texto(pantalla, nombre, fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2))
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2 + 50))
        pygame.display.flip()

def actualizar_leaderboard(tipo, leaderboard_data, nombre, puntuacion):
    leaderboard_data.append((nombre, puntuacion))
    leaderboard_data = sorted(leaderboard_data, key=lambda x: x[1], reverse=True)[:5]
    guardar_leaderboard(tipo, leaderboard_data)
    return leaderboard_data

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def mostrar_leaderboard(pantalla, ANCHO, ALTO, tipo, puntuacion=None):
    leaderboard_data = cargar_leaderboard(tipo)

    if puntuacion is not None:
        nombre = pedir_nombre(pantalla, ANCHO, ALTO, puntuacion)
        leaderboard_data = actualizar_leaderboard(tipo, leaderboard_data, nombre, puntuacion)

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
