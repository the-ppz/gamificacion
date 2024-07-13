import pygame
import sys
import json
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego
from pantallas.minijuego import minijuego
from pantallas.preguntas_respuestas import juego_preguntas
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.configuracion import pantalla_configuracion

pygame.init()

pygame.mixer.init()

sonido_seleccion = pygame.mixer.Sound('sonidos/seleccion.mp3')
sonido_correcto = pygame.mixer.Sound('sonidos/correcto.mp3')
sonido_incorrecto = pygame.mixer.Sound('sonidos/incorrecto.mp3')

sonidos = [sonido_seleccion, sonido_correcto, sonido_incorrecto]

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("EXPLORADORES DEL TIEMPO - ECUADOR")

def cargar_configuraciones():
    try:
        with open('configuraciones.json', 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"volumen": 5, "dificultad": 1}

def guardar_configuraciones(configuraciones):
    with open('configuraciones.json', 'w') as archivo:
        json.dump(configuraciones, archivo)

def main():
    configuraciones = cargar_configuraciones()
    
    for sonido in sonidos:
        sonido.set_volume(configuraciones["volumen"] / 10.0)
    
    while True:
        pantalla_inicio(pantalla, ANCHO, ALTO)
        nivel = seleccion_niveles(pantalla, ANCHO, ALTO, sonido_seleccion)
        
        if nivel == "Minijuego":
            puntuacion = minijuego(pantalla, ANCHO, ALTO)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "minijuego", puntuacion)
        elif nivel == "Nivel 1: Historia Antigua":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 1: Historia Antigua", puntuacion)
        elif nivel == "Nivel 2: Cultura Colonial":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 2: Cultura Colonial", puntuacion)
        elif nivel == "Nivel 3: Independencia":
            puntuacion = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 3: Independencia", puntuacion)
        elif nivel == "Configuración":
            pantalla_configuracion(pantalla, ANCHO, ALTO, configuraciones, sonidos)
            guardar_configuraciones(configuraciones)
        else:
            pantalla_juego(pantalla, ANCHO, ALTO, nivel)
            
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
