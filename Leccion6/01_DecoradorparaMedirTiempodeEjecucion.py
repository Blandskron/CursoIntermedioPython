import time

# Definición del decorador
def calcular_tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        tiempo_total = time.time() - inicio
        print(f"Tiempo de ejecución de {funcion.__name__}: {tiempo_total} segundos")
        return resultado
    return wrapper

# Uso del decorador
@calcular_tiempo_ejecucion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Llamada a la función decorada
print(factorial(5))  # Salida: 120
