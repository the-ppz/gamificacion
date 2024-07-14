import pygame
import sys
import random
from pantallas.experiencia import obtener_nivel_experiencia

pygame.font.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

fuente_pregunta = pygame.font.Font(None, 36)
fuente_respuesta = pygame.font.Font(None, 28)
fuente_feedback = pygame.font.Font(None, 36)
fuente_pausa = pygame.font.Font(None, 48)

preguntas = {
    "Nivel 1: Historia Antigua": [
        ("¿Cuál es la civilización más antigua de Ecuador?", ["Inca", "Cañari", "Manta", "Chimú"], 1),  # Cañari
        ("¿Qué cultura construyó Ingapirca?", ["Inca", "Cañari", "Manta", "Chimú"], 0),  # Inca
        ("¿Cuál es el sitio arqueológico más grande de Ecuador?", ["Ingapirca", "La Tolita", "Cochasquí", "Pumapungo"], 2),  # Cochasquí
        ("¿Cuál es la civilización más conocida de los Andes?", ["Inca", "Cañari", "Manta", "Chimú"], 0),  # Inca
        ("¿Qué cultura desarrolló la cerámica más avanzada?", ["Inca", "Cañari", "Manta", "Chimú"], 2),  # Manta
        ("¿Dónde se encuentra la pirámide más antigua de Ecuador?", ["Pumapungo", "La Tolita", "Cochasquí", "Ingapirca"], 2),  # Cochasquí
        ("¿Qué cultura fue conocida por sus trabajos en oro?", ["Inca", "Cañari", "Manta", "Chimú"], 2),  # Manta
        ("¿Cuál es el río más importante para las civilizaciones antiguas de Ecuador?", ["Guayas", "Esmeraldas", "Amazonas", "Napo"], 0),  # Guayas
        ("¿Qué cultura es conocida por sus tumbas en forma de pozo?", ["Cañari", "Manta", "Chimú", "La Tolita"], 3),  # La Tolita
        ("¿Cuál es el sitio arqueológico más importante de la cultura Valdivia?", ["Real Alto", "Cochasquí", "Ingapirca", "La Tolita"], 0),  # Real Alto
        ("¿Qué civilización precolombina es conocida por sus cabezas de piedra gigantes?", ["Valdivia", "La Tolita", "Cañari", "Manta"], 1),  # La Tolita
        ("¿Qué cultura ecuatoriana es famosa por sus figurillas femeninas de cerámica?", ["Valdivia", "Manta", "Cañari", "Chimú"], 0)  # Valdivia
    ],
    "Nivel 2: Cultura Colonial": [
        ("¿Quién fue el primer presidente de Ecuador?", ["Simón Bolívar", "Juan José Flores", "José de San Martín", "Manuela Sáenz"], 1),  # Juan José Flores
        ("¿En qué año se declaró la independencia de Ecuador?", ["1820", "1822", "1830", "1835"], 1),  # 1822
        ("¿Qué ciudad es conocida como la cuna de la independencia de Ecuador?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 0),  # Quito
        ("¿Cuál fue la principal actividad económica durante la colonia?", ["Agricultura", "Minería", "Comercio", "Ganadería"], 1),  # Minería
        ("¿Qué religioso fundó la primera universidad de Ecuador?", ["San Francisco", "San Agustín", "La Compañía", "San Gabriel"], 0),  # San Francisco
        ("¿Qué ciudad se destacó por su producción textil?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 2),  # Cuenca
        ("¿Qué ciudad fue el centro del comercio colonial?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 1),  # Guayaquil
        ("¿Quién fue el líder indígena en la rebelión de 1592?", ["Rumiñahui", "Nangotaz", "Píllaro", "Atahualpa"], 1),  # Nangotaz
        ("¿Qué evento marcó el inicio de la colonia en Ecuador?", ["Conquista de Quito", "Fundación de Guayaquil", "Expedición de Francisco Pizarro", "Llegada de Cristóbal Colón"], 0),  # Conquista de Quito
        ("¿Qué orden religiosa estableció las primeras misiones en Ecuador?", ["Jesuitas", "Franciscanos", "Dominicos", "Agustinos"], 1),  # Franciscanos
        ("¿Qué edificio colonial es conocido como la 'Escuela Quiteña'?", ["La Catedral de Quito", "La Iglesia de San Francisco", "La Iglesia de La Compañía", "El Convento de Santo Domingo"], 2),  # La Iglesia de La Compañía
        ("¿Qué ciudad es conocida como 'La Atenas del Ecuador'?", ["Quito", "Cuenca", "Guayaquil", "Loja"], 1)  # Cuenca
    ],
    "Nivel 3: Independencia": [
        ("¿Quién lideró la batalla de Pichincha?", ["Simón Bolívar", "Antonio José de Sucre", "José de San Martín", "Manuela Sáenz"], 1),  # Antonio José de Sucre
        ("¿En qué fecha se celebra la independencia de Ecuador?", ["10 de Agosto", "24 de Mayo", "9 de Octubre", "3 de Noviembre"], 1),  # 24 de Mayo
        ("¿Cuál es el nombre del primer grito de independencia?", ["Grito de Yaguachi", "Grito de Pichincha", "Grito de Loja", "Grito de Independencia"], 0),  # Grito de Yaguachi
        ("¿Quién fue el principal líder de la independencia de Quito?", ["Simón Bolívar", "Antonio José de Sucre", "José de San Martín", "Eugenio Espejo"], 3),  # Eugenio Espejo
        ("¿Qué batalla aseguró la independencia de Guayaquil?", ["Batalla de Pichincha", "Batalla de Tarqui", "Batalla de Junín", "Batalla de Boyacá"], 0),  # Batalla de Pichincha
        ("¿Qué líder militar ayudó en la independencia de Ecuador?", ["Simón Bolívar", "José de San Martín", "Antonio José de Sucre", "Francisco de Paula Santander"], 2),  # Antonio José de Sucre
        ("¿En qué ciudad se firmó el Acta de Independencia?", ["Quito", "Guayaquil", "Cuenca", "Loja"], 1),  # Guayaquil
        ("¿Quién fue el líder del primer movimiento independentista?", ["Eugenio Espejo", "José Joaquín de Olmedo", "Manuela Sáenz", "Simón Bolívar"], 0),  # Eugenio Espejo
        ("¿Qué país ayudó a Ecuador en su lucha por la independencia?", ["Perú", "Colombia", "Chile", "Venezuela"], 1),  # Colombia
        ("¿Quién fue la heroína que luchó por la independencia de Quito?", ["Manuela Sáenz", "Dolores Cacuango", "Eugenia del Pino", "Matilde Hidalgo"], 0),  # Manuela Sáenz
        ("¿Qué provincia ecuatoriana se unió primero al movimiento independentista?", ["Pichincha", "Guayas", "Azuay", "Loja"], 1),  # Guayas
        ("¿Qué tratado reconoció la independencia de Ecuador?", ["Tratado de Tordesillas", "Tratado de Guayaquil", "Tratado de Quito", "Tratado de Córdoba"], 2)  # Tratado de Quito
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

def juego_preguntas(pantalla, ANCHO, ALTO, nivel, puntuacion, sonido_correcto, sonido_incorrecto, puntos_experiencia):
    preguntas_nivel = preguntas[nivel]
    pregunta_actual = 0
    respuesta_seleccionada = 0
    puntuacion_total = puntuacion
    vidas = 3
    preguntas_pendientes = list(range(len(preguntas_nivel)))

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
                        puntuacion_total += 100
                        puntos_experiencia += 100
                        sonido_correcto.play()
                    else:
                        vidas -= 1
                        sonido_incorrecto.play()
                        if vidas == 0:
                            return puntuacion_total, puntos_experiencia

                    preguntas_pendientes.remove(pregunta_actual)
                    if preguntas_pendientes:
                        pregunta_actual = random.choice(preguntas_pendientes)
                    else:
                        return puntuacion_total, puntos_experiencia

        pantalla.fill(BLANCO)
        pregunta, respuestas, _ = preguntas_nivel[pregunta_actual]
        mostrar_pregunta(pantalla, pregunta, respuestas, respuesta_seleccionada)
        mostrar_texto(pantalla, f"Puntuación: {puntuacion_total}", fuente_pregunta, NEGRO, (ANCHO // 2, 50))
        mostrar_texto(pantalla, f"Vidas: {vidas}", fuente_pregunta, ROJO, (ANCHO // 2, 100))

        # Mostrar el nivel de experiencia
        nivel_experiencia = obtener_nivel_experiencia(puntos_experiencia)
        mostrar_texto(pantalla, f"Nivel: {nivel_experiencia}", fuente_pregunta, NEGRO, (ANCHO - 150, 50))
        mostrar_texto(pantalla, f"XP: {puntos_experiencia}", fuente_pregunta, NEGRO, (ANCHO - 150, 80))

        pygame.display.flip()