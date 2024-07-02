import pygame
import sys

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

fuente_pregunta = pygame.font.Font(None, 36)
fuente_respuesta = pygame.font.Font(None, 28)

preguntas = {
    "Nivel 1: Historia Antigua": [
        ("¿Cuál es la civilización más antigua de Ecuador?", ["Inca", "Cañari", "Manta", "Chimú"], 1),
        ("¿Qué cultura construyó Ingapirca?", ["Inca", "Cañari", "Manta", "Chimú"], 0),
        ("¿Cuál es el sitio arqueológico más grande de Ecuador?", ["Ingapirca", "La Tolita", "Cochasquí", "Pumapungo"], 2)
    ],
    "Nivel 2: Cultura Colonial": [
        ("¿Quién fue el primer presidente de Ecuador?", ["Simón Bolívar", "Juan José Flores", "José de San Martín", "Manuela Sáenz"], 1),
        ("¿En qué año se declaró la independencia de Ecuador?", ["1820", "1822", "1830", "1835"], 1),
        ("¿Qué ciudad es conocida como la cuna de la independencia de Ecuador?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 0)
    ],
    "Nivel 3: Independencia": [
        ("¿Quién lideró la batalla de Pichincha?", ["Simón Bolívar", "Antonio José de Sucre", "José de San Martín", "Manuela Sáenz"], 1),
        ("¿En qué fecha se celebra la independencia de Ecuador?", ["10 de Agosto", "24 de Mayo", "9 de Octubre", "3 de Noviembre"], 1),
        ("¿Cuál es el nombre del primer grito de independencia?", ["Grito de Yaguachi", "Grito de Pichincha", "Grito de Loja", "Grito de Independencia"], 0)
    ]
}

def mostrar_texto(pantalla, texto, fuente, color, centro):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = centro
    pantalla.blit(superficie, rect)

def mostrar_pregunta(pantalla, pregunta, respuestas, seleccionada):
    mostrar_texto(pantalla, pregunta, fuente_pregunta, NEGRO, (400, 150))
    for i, respuesta in enumerate(respuestas):
        color = ROJO if i == seleccionada else NEGRO
        mostrar_texto(pantalla, respuesta, fuente_respuesta, color, (400, 250 + i * 40))

def juego_preguntas(pantalla, ANCHO, ALTO, nivel, puntuacion):
    preguntas_nivel = preguntas[nivel]
    pregunta_actual = 0
    respuesta_seleccionada = 0
    puntuacion_total = puntuacion

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    respuesta_seleccionada = (respuesta_seleccionada - 1) % 4
                elif evento.key == pygame.K_DOWN:
                    respuesta_seleccionada = (respuesta_seleccionada + 1) % 4
                elif evento.key == pygame.K_RETURN:
                    _, respuestas, correcta = preguntas_nivel[pregunta_actual]
                    if respuesta_seleccionada == correcta:
                        puntuacion_total += 100  # Ganar puntos por respuesta correcta
                    pregunta_actual += 1
                    if pregunta_actual >= len(preguntas_nivel):
                        return puntuacion_total

        pantalla.fill(BLANCO)
        pregunta, respuestas, _ = preguntas_nivel[pregunta_actual]
        mostrar_pregunta(pantalla, pregunta, respuestas, respuesta_seleccionada)
        mostrar_texto(pantalla, f"Puntuación: {puntuacion_total}", fuente_pregunta, NEGRO, (ANCHO // 2, 50))

        pygame.display.flip()
