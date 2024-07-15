import pygame
import sys
import json
import os

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
GRIS_CLARO = (240, 240, 240)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

fuente_leaderboard = pygame.font.Font(None, 48)
fuente_nombre = pygame.font.Font(None, 36)

LEADERBOARD_FILES = {
    "minijuego": resource_path("src/leaderboard_minijuego.json"),
    "Nivel 1: Historia Antigua": resource_path("src/leaderboard_nivel1.json"),
    "Nivel 2: Cultura Colonial": resource_path("src/leaderboard_nivel2.json"),
    "Nivel 3: Independencia": resource_path("src/leaderboard_nivel3.json")
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

        pantalla.fill(GRIS_CLARO)
        mostrar_texto(pantalla, "Ingresa tu nombre:", fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2 - 50), fondo=BLANCO, padding=10, border_radius=10)
        mostrar_texto(pantalla, nombre, fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2), fondo=BLANCO, padding=10, border_radius=10)
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", fuente_nombre, NEGRO, (ANCHO // 2, ALTO // 2 + 50), fondo=BLANCO, padding=10, border_radius=10)
        pygame.display.flip()

def actualizar_leaderboard(tipo, leaderboard_data, nombre, puntuacion):
    leaderboard_data.append((nombre, puntuacion))
    leaderboard_data = sorted(leaderboard_data, key=lambda x: x[1], reverse=True)[:5]
    guardar_leaderboard(tipo, leaderboard_data)
    return leaderboard_data

def mostrar_texto(pantalla, texto, fuente, color, centro, fondo=BLANCO, padding=10, border_radius=10):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro

    # Dibujar fondo redondeado
    fondo_rect = rect.inflate(padding * 2, padding * 2)
    pygame.draw.rect(pantalla, fondo, fondo_rect, border_radius=border_radius)
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

        pantalla.fill(GRIS_CLARO)
        mostrar_texto(pantalla, "Clasificación", fuente_leaderboard, NEGRO, (ANCHO // 2, 50), padding=20)

        for i, (jugador, puntuacion) in enumerate(leaderboard_data):
            texto = f"{i + 1}. {jugador} - {puntuacion} puntos"
            mostrar_texto(pantalla, texto, fuente_nombre, NEGRO, (ANCHO // 2, 150 + i * 50), fondo=BLANCO, padding=10, border_radius=10)

        mostrar_texto(pantalla, "Presiona Enter para continuar", fuente_nombre, NEGRO, (ANCHO // 2, ALTO - 50), fondo=VERDE, padding=10, border_radius=10)

        pygame.display.flip()
