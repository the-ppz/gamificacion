import pygame
import sys
from pantallas.leaderboard import mostrar_leaderboard
from pantallas.experiencia import obtener_nivel_experiencia, cargar_experiencia
from pantallas.pantalla_ayuda import pantalla_ayuda
from pantallas.pantalla_equipo import pantalla_equipo

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
AZUL_CLARO = (173, 216, 230)
VERDE = (59, 158, 98)

fondo = pygame.image.load('src/fondo_inicio.jpg')

fuente_titulo = pygame.font.Font(None, 64)  
fuente_niveles = pygame.font.Font(None, 27)  
fuente_nivel = pygame.font.Font(None, 24)  

niveles = [
    "Nivel 1: Historia Antigua",
    "Nivel 2: Cultura Colonial",
    "Nivel 3: Independencia",
    "Minijuego"
]

clasificaciones = [
    "Clasificación Nivel 1",
    "Clasificación Nivel 2",
    "Clasificación Nivel 3",
    "Clasificación Minijuego"
]

configuraciones = [
    "Configuración",
    "Ayuda",
    "Equipo de Desarrolladores"
]

niveles_imagenes = [
    "src/nivel1.png",
    "src/nivel2.png",
    "src/nivel3.png",
    "src/minijuego.png"
]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def mostrar_tarjeta_nivel(pantalla, x, y, ancho, alto, nivel, imagen, seleccionado=False):
    color_fondo = AZUL_CLARO if seleccionado else BLANCO
    pygame.draw.rect(pantalla, color_fondo, (x, y, ancho, alto), 0, 10)
    pygame.draw.rect(pantalla, NEGRO, (x, y, ancho, alto), 2, 10)
    
    nivel_texto = fuente_niveles.render(nivel, True, NEGRO)
    nivel_rect = nivel_texto.get_rect(center=(x + ancho // 2, y + 20))
    pantalla.blit(nivel_texto, nivel_rect)
    
    imagen = pygame.image.load(imagen)
    imagen = pygame.transform.scale(imagen, (ancho - 20, alto - 120))
    pantalla.blit(imagen, (x + 10, y + 50))
    
    jugar_texto = fuente_nivel.render("JUGAR", True, VERDE)
    pantalla.blit(jugar_texto, (x + ancho // 2 - jugar_texto.get_width() // 2, y + alto - 30))

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
                    nivel_seleccionado = (nivel_seleccionado - 1) % (len(niveles) + 2)
                elif evento.key == pygame.K_DOWN:
                    nivel_seleccionado = (nivel_seleccionado + 1) % (len(niveles) + 2)
                elif evento.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(sonido_seleccion)
                    if nivel_seleccionado < len(niveles):
                        return niveles[nivel_seleccionado]
                    elif nivel_seleccionado == len(niveles):
                        return "Clasificaciones"
                    elif nivel_seleccionado == len(niveles) + 1:
                        return "Configuración"
                elif evento.key == pygame.K_ESCAPE:
                    return "pantalla_inicio"

        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, "Selecciona un Nivel", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        # Mostrar tarjetas de nivel en una fila
        espacio_x = 60
        espacio_y = 150
        ancho_tarjeta = 230
        alto_tarjeta = 300
        for i in range(len(niveles)):
            x = espacio_x + i * (ancho_tarjeta + 50)
            y = espacio_y
            mostrar_tarjeta_nivel(pantalla, x, y, ancho_tarjeta, alto_tarjeta, niveles[i], niveles_imagenes[i], i == nivel_seleccionado)
        
        # Mostrar "Clasificaciones" y "Configuración" debajo de las tarjetas
        y_opciones = espacio_y + alto_tarjeta + 50
        mostrar_texto(pantalla, "Clasificaciones", fuente_niveles, ROJO if nivel_seleccionado == len(niveles) else NEGRO, (ANCHO // 2, y_opciones))
        mostrar_texto(pantalla, "Configuración", fuente_niveles, ROJO if nivel_seleccionado == len(niveles) + 1 else NEGRO, (ANCHO // 2, y_opciones + 50))

        # Añadir barra de progreso de experiencia
        pygame.draw.rect(pantalla, NEGRO, (ANCHO - 210, ALTO - 30, 200, 20), 2)
        pygame.draw.rect(pantalla, AMARILLO, (ANCHO - 208, ALTO - 28, 200 * puntos_experiencia / 2500, 16))
            
        mostrar_texto(pantalla, f"Nivel: {nivel_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 50))
        mostrar_texto(pantalla, f"XP: {puntos_experiencia}", fuente_nivel, NEGRO, (ANCHO - 100, ALTO - 20))

        pygame.display.flip()

def pantalla_clasificaciones(pantalla, ANCHO, ALTO, sonido_seleccion):
    clasificacion_seleccionada = 0
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    clasificacion_seleccionada = (clasificacion_seleccionada - 1) % len(clasificaciones)
                elif evento.key == pygame.K_DOWN:
                    clasificacion_seleccionada = (clasificacion_seleccionada + 1) % len(clasificaciones)
                elif evento.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(sonido_seleccion)
                    if clasificaciones[clasificacion_seleccionada] == "Clasificación Minijuego":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "minijuego")
                    elif clasificaciones[clasificacion_seleccionada] == "Clasificación Nivel 1":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 1: Historia Antigua")
                    elif clasificaciones[clasificacion_seleccionada] == "Clasificación Nivel 2":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 2: Cultura Colonial")
                    elif clasificaciones[clasificacion_seleccionada] == "Clasificación Nivel 3":
                        mostrar_leaderboard(pantalla, ANCHO, ALTO, "Nivel 3: Independencia")
                elif evento.key == pygame.K_ESCAPE:
                    return "pantalla_inicio"

        pantalla.blit(fondo, (0, 0))
        mostrar_texto(pantalla, "Clasificaciones", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        for i, clasificacion in enumerate(clasificaciones):
            color = ROJO if i == clasificacion_seleccionada else NEGRO
            mostrar_texto(pantalla, clasificacion, fuente_niveles, color, (ANCHO // 2, 150 + i * 50))

        pygame.display.flip()
        pygame.display.flip()

