"""
02 ManejodeArchivosJSON.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

import json

# Ejemplo de escritura de datos en un archivo JSON
datos = {
    "empleados": [
        {"nombre": "Alice", "edad": 30, "email": "alice@example.com"},
        {"nombre": "Bob", "edad": 25, "email": "bob@example.com"},
        {"nombre": "Charlie", "edad": 35, "email": "charlie@example.com"}
    ]
}

# Escribir datos en un archivo JSON
with open('datos.json', 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)

print("Archivo JSON creado exitosamente.")

# Ejemplo de lectura de datos desde un archivo JSON
with open('datos.json', 'r') as archivo_json:
    datos_cargados = json.load(archivo_json)
    for empleado in datos_cargados['empleados']:
        print(empleado)
