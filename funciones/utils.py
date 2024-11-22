import json

def leer_json(ruta, clave):
    """Lee un archivo JSON y devuelve los datos de la clave especificada."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos[clave]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return {"ES": ["python", "programacion", "juego"]}
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON: {ruta}")
        return {"ES": ["python", "programacion", "juego"]}

def guardar_puntuacion(nombre, puntos):
    """Guarda la puntuación de un jugador."""
    try:
        with open('puntuaciones.json', 'r+', encoding='utf-8') as archivo:
            puntuaciones = json.load(archivo)
            puntuaciones.append({"nombre": nombre, "puntos": puntos})
            archivo.seek(0)
            json.dump(puntuaciones, archivo, indent=2)
    except FileNotFoundError:
        with open('puntuaciones.json', 'w', encoding='utf-8') as archivo:
            json.dump([{"nombre": nombre, "puntos": puntos}], archivo, indent=2)