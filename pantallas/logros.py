logros_definidos = {
    "mejor_tiempo_nivel_1": {
        "nombre": "Mejor Tiempo Personal en Nivel 1",
        "descripcion": "Logra el mejor tiempo en el nivel 1",
        "nivel": "Nivel 1: Historia Antigua",
        "condicion": lambda tiempo_actual, mejor_tiempo: tiempo_actual < mejor_tiempo
    },
    "respuestas_consecutivas_nivel_1": {
        "nombre": "Mayor Número de Respuestas Correctas Consecutivas en Nivel 1",
        "descripcion": "Responde correctamente a todas las preguntas consecutivamente en nivel 1",
        "nivel": "Nivel 1: Historia Antigua",
        "condicion": lambda respuestas_correctas, total_preguntas: respuestas_correctas == total_preguntas
    },
    "sin_errores_nivel_1": {
        "nombre": "Nivel 1 Completo sin Errores",
        "descripcion": "Completa el nivel 1 sin cometer errores",
        "nivel": "Nivel 1: Historia Antigua",
        "condicion": lambda errores: errores == 0
    },
    "mejor_tiempo_nivel_2": {
        "nombre": "Mejor Tiempo Personal en Nivel 2",
        "descripcion": "Logra el mejor tiempo en el nivel 2",
        "nivel": "Nivel 2: Cultura Colonial",
        "condicion": lambda tiempo_actual, mejor_tiempo: tiempo_actual < mejor_tiempo
    },
    "respuestas_consecutivas_nivel_2": {
        "nombre": "Mayor Número de Respuestas Correctas Consecutivas en Nivel 2",
        "descripcion": "Responde correctamente a todas las preguntas consecutivamente en nivel 2",
        "nivel": "Nivel 2: Cultura Colonial",
        "condicion": lambda respuestas_correctas, total_preguntas: respuestas_correctas == total_preguntas
    },
    "sin_errores_nivel_2": {
        "nombre": "Nivel 2 Completo sin Errores",
        "descripcion": "Completa el nivel 2 sin cometer errores",
        "nivel": "Nivel 2: Cultura Colonial",
        "condicion": lambda errores: errores == 0
    },
    "mejor_tiempo_nivel_3": {
        "nombre": "Mejor Tiempo Personal en Nivel 3",
        "descripcion": "Logra el mejor tiempo en el nivel 3",
        "nivel": "Nivel 3: Independencia",
        "condicion": lambda tiempo_actual, mejor_tiempo: tiempo_actual < mejor_tiempo
    },
    "respuestas_consecutivas_nivel_3": {
        "nombre": "Mayor Número de Respuestas Correctas Consecutivas en Nivel 3",
        "descripcion": "Responde correctamente a todas las preguntas consecutivamente en nivel 3",
        "nivel": "Nivel 3: Independencia",
        "condicion": lambda respuestas_correctas, total_preguntas: respuestas_correctas == total_preguntas
    },
    "sin_errores_nivel_3": {
        "nombre": "Nivel 3 Completo sin Errores",
        "descripcion": "Completa el nivel 3 sin cometer errores",
        "nivel": "Nivel 3: Independencia",
        "condicion": lambda errores: errores == 0
    }
}

def verificar_logros(nivel, puntuacion, respuestas_correctas_consecutivas, tiempo_total, errores):
    logros_obtenidos = []

    for key, logro in logros_definidos.items():
        if logro["nivel"] == nivel:
            if "tiempo" in key and logro["condicion"](tiempo_total, 60):  # Suponiendo 60 segundos como el mejor tiempo
                logros_obtenidos.append(logro["nombre"])
            elif "respuestas_consecutivas" in key and logro["condicion"](respuestas_correctas_consecutivas, 10):  # Suponiendo 10 preguntas
                logros_obtenidos.append(logro["nombre"])
            elif "sin_errores" in key and logro["condicion"](errores):
                logros_obtenidos.append(logro["nombre"])

    return logros_obtenidos
