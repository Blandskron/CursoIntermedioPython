### Ejemplo 1: Uso de Iteradores

```python
# Ejemplo de uso de iteradores en Python
iterable = [1, 2, 3, 4, 5]
iterador = iter(iterable)

print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3

# Iteración completa usando un bucle for
for elemento in iterador:
    print(elemento)  # Salida: 4 y 5
```

En este ejemplo:
- Se crea un iterador a partir de una lista usando la función `iter()`.
- Se utilizan llamadas a `next()` para obtener los siguientes elementos del iterador.
- Se muestra cómo iterar completamente sobre el iterador usando un bucle `for`, imprimiendo los elementos restantes.

### Ejemplo 2: Creación y Uso de Generadores

```python
# Ejemplo de creación de un generador en Python
def generador_pares(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 2

# Uso del generador para obtener números pares menores que 10
gen = generador_pares(10)

for numero in gen:
    print(numero)  # Salida: 0, 2, 4, 6, 8
```

En este ejemplo:
- Se define la función `generador_pares()` como un generador usando la palabra clave `yield`.
- El generador produce números pares menores que el valor máximo especificado.
- Se itera sobre el generador usando un bucle `for`, imprimiendo cada número generado.

### Ejemplo 3: Generador Infinito

```python
# Ejemplo de generador infinito en Python
def generador_infinito():
    num = 1
    while True:
        yield num
        num += 1

# Uso del generador infinito para obtener los primeros 5 números naturales
gen = generador_infinito()

for _ in range(5):
    print(next(gen))  # Salida: 1, 2, 3, 4, 5
```

En este ejemplo:
- Se define `generador_infinito()` como un generador que produce números naturales infinitamente.
- Se utiliza el generador en un bucle `for` con `range(5)` para obtener los primeros 5 números naturales.

### Ejemplo 4: Generador de Fibonacci

```python
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
```

En este ejemplo:
- Se define la función `fibonacci()` como un generador que produce la secuencia de Fibonacci.
- Se utiliza el generador para generar números de Fibonacci menores que 100 y se imprimen en una sola línea.

Estos ejemplos muestran cómo implementar y utilizar tanto iteradores como generadores en Python para manipular y generar secuencias de datos de manera eficiente y efectiva.