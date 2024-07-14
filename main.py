import pygame
import sys
import json
from pantallas.pantalla_inicio import pantalla_inicio
from pantallas.seleccion_niveles import seleccion_niveles
from pantallas.pantalla_juego import pantalla_juego
from pantallas.minijuego import minijuego
from pantallas.preguntas_respuestas import juego_preguntas, mostrar_logros
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.configuracion import pantalla_configuracion
from pantallas.pantalla_ayuda import pantalla_ayuda
from pantallas.pantalla_equipo import pantalla_equipo
from pantallas.experiencia import guardar_experiencia, cargar_experiencia, obtener_nivel_experiencia

pygame.init()

pygame.mixer.init()

sonido_seleccion = pygame.mixer.Sound('sonidos/seleccion.mp3')
sonido_correcto = pygame.mixer.Sound('sonidos/correcto.mp3')
sonido_incorrecto = pygame.mixer.Sound('sonidos/incorrecto.mp3')

sonidos = [sonido_seleccion, sonido_correcto, sonido_incorrecto]

ANCHO, ALTO = 1200, 750
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
    puntos_experiencia = cargar_experiencia()

    for sonido in sonidos:
        sonido.set_volume(configuraciones["volumen"] / 10.0)
    
    while True:
        pantalla_inicio(pantalla, ANCHO, ALTO)
        nivel = seleccion_niveles(pantalla, ANCHO, ALTO, sonido_seleccion)
        
        if nivel == "Minijuego":
            puntuacion = minijuego(pantalla, ANCHO, ALTO, configuraciones["dificultad"])
            puntos_experiencia += puntuacion
            guardar_experiencia(puntos_experiencia)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "minijuego", puntuacion)
        elif nivel == "Nivel 1: Historia Antigua":
            puntuacion, puntos_experiencia, logros_obtenidos = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto, puntos_experiencia)
            guardar_experiencia(puntos_experiencia)
            mostrar_logros(pantalla, ANCHO, ALTO, logros_obtenidos)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 1: Historia Antigua", puntuacion)
        elif nivel == "Nivel 2: Cultura Colonial":
            puntuacion, puntos_experiencia, logros_obtenidos = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto, puntos_experiencia)
            guardar_experiencia(puntos_experiencia)
            mostrar_logros(pantalla, ANCHO, ALTO, logros_obtenidos)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 2: Cultura Colonial", puntuacion)
        elif nivel == "Nivel 3: Independencia":
            puntuacion, puntos_experiencia, logros_obtenidos = juego_preguntas(pantalla, ANCHO, ALTO, nivel, 0, sonido_correcto, sonido_incorrecto, puntos_experiencia)
            guardar_experiencia(puntos_experiencia)
            mostrar_logros(pantalla, ANCHO, ALTO, logros_obtenidos)
            mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 3: Independencia", puntuacion)
        elif nivel == "Configuración":
            pantalla_configuracion(pantalla, ANCHO, ALTO, configuraciones, sonidos)
            guardar_configuraciones(configuraciones)
        elif nivel == "Ayuda":
            pantalla_ayuda(pantalla, ANCHO, ALTO)
        elif nivel == "Equipo de Desarrolladores":
            pantalla_equipo(pantalla, ANCHO, ALTO)
        elif nivel == "pantalla_inicio":
                continue
        else:
            pantalla_juego(pantalla, ANCHO, ALTO, nivel, puntos_experiencia)
            
if __name__ == "__main__":
    try:
        main()
    finally:
        guardar_experiencia(0) 
        pygame.quit()
        sys.exit()