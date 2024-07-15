# pantalla_personajes.py
import pygame
import sys

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL_CLARO = (173, 216, 230)
VERDE = (59, 158, 98)

fuente_titulo = pygame.font.Font(None, 64)
fuente_niveles = pygame.font.Font(None, 27)
fuente_nivel = pygame.font.Font(None, 24)

personajes = [
    "Principiante",
    "Aprendiz",
    "Historico",
    "Erudito",
    "Sabio"
]

personajes_imagenes = [
    "src/principiante.png",
    "src/aprendiz.png",
    "src/historico.png",
    "src/erudito.png",
    "src/sabio.png"
]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def mostrar_tarjeta(pantalla, x, y, ancho, alto, titulo, imagen, seleccionado=False):
    color_fondo = AZUL_CLARO if seleccionado else BLANCO
    pygame.draw.rect(pantalla, color_fondo, (x, y, ancho, alto), 0, 10)
    pygame.draw.rect(pantalla, NEGRO, (x, y, ancho, alto), 2, 10)
    
    titulo_texto = fuente_niveles.render(titulo, True, NEGRO)
    titulo_rect = titulo_texto.get_rect(center=(x + ancho // 2, y + 20))
    pantalla.blit(titulo_texto, titulo_rect)
    
    imagen = pygame.image.load(imagen)
    imagen = pygame.transform.scale(imagen, (ancho - 20, alto - 120))
    pantalla.blit(imagen, (x + 10, y + 50))
    
    seleccionar_texto = fuente_nivel.render("SELECCIONAR", True, VERDE)
    pantalla.blit(seleccionar_texto, (x + ancho // 2 - seleccionar_texto.get_width() // 2, y + alto - 30))

def pantalla_personajes(pantalla, ANCHO, ALTO, sonido_seleccion):
    personaje_seleccionado = 0
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    personaje_seleccionado = (personaje_seleccionado - 1) % len(personajes)
                elif evento.key == pygame.K_RIGHT:
                    personaje_seleccionado = (personaje_seleccionado + 1) % len(personajes)
                elif evento.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(sonido_seleccion)
                    return "pantalla_inicio"
                elif evento.key == pygame.K_ESCAPE:
                    return "pantalla_inicio"

        pantalla.fill(BLANCO)
        mostrar_texto(pantalla, "Selecciona un Personaje", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        # Mostrar tarjetas de personaje en una fila
        espacio_x = 40
        espacio_y = 150
        ancho_tarjeta = 200
        alto_tarjeta = 300
        for i in range(len(personajes)):
            x = espacio_x + i * (ancho_tarjeta + 50)
            y = espacio_y
            mostrar_tarjeta(pantalla, x, y, ancho_tarjeta, alto_tarjeta, personajes[i], personajes_imagenes[i], i == personaje_seleccionado)
        
        pygame.display.flip()
