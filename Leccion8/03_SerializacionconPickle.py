"""
03 SerializacionconPickle.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

import pickle

# Ejemplo de serialización de un objeto Python con Pickle
datos = {
    "nombre": "Alice",
    "edad": 30,
    "email": "alice@example.com"
}

# Serializar datos y guardar en un archivo binario
with open('datos.pickle', 'wb') as archivo_pickle:
    pickle.dump(datos, archivo_pickle)

print("Objeto serializado y guardado exitosamente como datos.pickle.")

# Ejemplo de deserialización de un archivo Pickle
with open('datos.pickle', 'rb') as archivo_pickle:
    datos_cargados = pickle.load(archivo_pickle)
    print("Datos cargados desde Pickle:", datos_cargados)
