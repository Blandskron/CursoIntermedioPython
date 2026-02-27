"""
02 Usode-ELSE-y-Finally.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de uso de cláusulas else y finally en Python
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
else:
    print("Lectura exitosa del archivo:")
    print(contenido)
finally:
    if 'archivo' in locals():
        archivo.close()
