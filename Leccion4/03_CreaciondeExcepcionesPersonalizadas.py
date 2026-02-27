"""
03 CreaciondeExcepcionesPersonalizadas.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de creación de excepción personalizada en Python
class MiError(Exception):
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0 or edad > 120:
        raise MiError("La edad ingresada no es válida.")
    else:
        print(f"Edad ingresada: {edad}")
except MiError as e:
    print(e)
except ValueError:
    print("Error: Ingrese un número entero válido para la edad.")
