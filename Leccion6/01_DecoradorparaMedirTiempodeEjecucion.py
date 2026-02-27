"""
01 DecoradorparaMedirTiempodeEjecucion.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

import time

# Definición del decorador
def calcular_tiempo_ejecucion(funcion):
    # Función wrapper: implementa una parte específica del flujo de ejemplo.
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        tiempo_total = time.time() - inicio
        print(f"Tiempo de ejecución de {funcion.__name__}: {tiempo_total} segundos")
        return resultado
    return wrapper

# Uso del decorador
@calcular_tiempo_ejecucion
# Función factorial: implementa una parte específica del flujo de ejemplo.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Llamada a la función decorada
print(factorial(5))  # Salida: 120
