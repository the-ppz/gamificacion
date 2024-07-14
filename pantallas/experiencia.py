import json

niveles_experiencia = {
    "Principiante": 0,
    "Aprendiz": 500,
    "Historico": 1000,
    "Erudito": 1500,
    "Sabio": 2000
}

def obtener_nivel_experiencia(puntos_experiencia):
    if puntos_experiencia >= niveles_experiencia["Sabio"]:
        return "Sabio"
    elif puntos_experiencia >= niveles_experiencia["Erudito"]:
        return "Erudito"
    elif puntos_experiencia >= niveles_experiencia["Historico"]:
        return "Historico"
    elif puntos_experiencia >= niveles_experiencia["Aprendiz"]:
        return "Aprendiz"
    else:
        return "Principiante"

def guardar_experiencia(puntos_experiencia=0):
    with open('experiencia.json', 'w') as archivo:
        json.dump({"puntos_experiencia": puntos_experiencia}, archivo)

def cargar_experiencia():
    try:
        with open('experiencia.json', 'r') as archivo:
            datos = json.load(archivo)
            return datos["puntos_experiencia"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0
