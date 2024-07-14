import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

fuente_titulo = pygame.font.Font(None, 74)
fuente_opciones = pygame.font.Font(None, 36)

opciones = ["Volumen: ", "Dificultad del Minijuego: "]
dificultades = ["Fácil", "Medio", "Difícil"]

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def pantalla_configuracion(pantalla, ANCHO, ALTO, configuraciones, sonidos):
    opcion_seleccionada = 0
    volumen = configuraciones["volumen"]
    dificultad = configuraciones["dificultad"]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_LEFT:
                    if opcion_seleccionada == 0:
                        volumen = max(0, volumen - 1)
                    elif opcion_seleccionada == 1:
                        dificultad = (dificultad - 1) % len(dificultades)
                elif evento.key == pygame.K_RIGHT:
                    if opcion_seleccionada == 0:
                        volumen = min(10, volumen + 1)
                    elif opcion_seleccionada == 1:
                        dificultad = (dificultad + 1) % len(dificultades)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_ESCAPE:
                    configuraciones["volumen"] = volumen
                    configuraciones["dificultad"] = dificultad
                    for sonido in sonidos:
                        sonido.set_volume(volumen / 10.0)
                    return

        pantalla.fill(BLANCO)
        mostrar_texto(pantalla, "Configuración", fuente_titulo, NEGRO, (ANCHO // 2, 50))

        mostrar_texto(pantalla, f"{opciones[0]} {volumen}", fuente_opciones, ROJO if opcion_seleccionada == 0 else NEGRO, (ANCHO // 2, 150))
        mostrar_texto(pantalla, f"{opciones[1]} {dificultades[dificultad]}", fuente_opciones, ROJO if opcion_seleccionada == 1 else NEGRO, (ANCHO // 2, 200))

        mostrar_texto(pantalla, "Usa las flechas para ajustar", fuente_opciones, NEGRO, (ANCHO // 2, ALTO - 100))
        mostrar_texto(pantalla, "Presiona Enter para guardar y salir", fuente_opciones, NEGRO, (ANCHO // 2, ALTO - 50))

        pygame.display.flip()
