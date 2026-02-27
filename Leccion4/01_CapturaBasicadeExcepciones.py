"""
01 CapturaBasicadeExcepciones.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de captura básica de excepciones en Python
try:
    num = int(input("Ingrese un número entero: "))
    resultado = 10 / num
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Ingrese un valor entero válido.")
except Exception as e:
    print(f"Error desconocido: {e}")
