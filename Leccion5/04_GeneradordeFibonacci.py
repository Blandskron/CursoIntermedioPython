# Ejemplo de generador de la secuencia Fibonacci en Python
def fibonacci(maximo):
    a, b = 0, 1
    while a < maximo:
        yield a
        a, b = b, a + b

# Uso del generador de Fibonacci para obtener los números menores que 100
gen = fibonacci(100)

for numero in gen:
    print(numero, end=' ')  # Salida: 0 1 1 2 3 5 8 13 21 34 55 89
