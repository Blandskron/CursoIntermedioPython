### Ejemplo 1: Decorador para Medir Tiempo de Ejecución

Este decorador calculará y mostrará el tiempo que tarda una función en ejecutarse.

```python
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
```

En este ejemplo:
- `calcular_tiempo_ejecucion` es un decorador que calcula y muestra el tiempo que tarda una función en ejecutarse.
- `wrapper` es la función interna que calcula el tiempo antes y después de llamar a `funcion`.
- El decorador se aplica a la función `factorial`, y cuando se llama a `factorial(5)`, se muestra el tiempo de ejecución.

### Ejemplo 2: Decorador para Verificar Parámetros

Este decorador verifica si los argumentos de una función son todos números enteros antes de llamar a la función.

```python
# Definición del decorador
def verificar_enteros(funcion):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            resultado = funcion(*args, **kwargs)
            return resultado
        else:
            raise TypeError("Todos los argumentos deben ser enteros.")
    return wrapper

# Uso del decorador
@verificar_enteros
def sumar(a, b):
    return a + b

# Llamada a la función decorada
print(sumar(3, 5))  # Salida: 8

# Si se intenta llamar sumar con un argumento no entero, generará un error
# print(sumar(3, "5"))  # Generará un TypeError
```

En este ejemplo:
- `verificar_enteros` es un decorador que verifica si todos los argumentos de una función son enteros antes de llamar a la función.
- `wrapper` verifica cada argumento de `args` para asegurarse de que sea un entero usando `isinstance`.
- Si todos los argumentos son enteros, llama a la función original; de lo contrario, genera un `TypeError`.

### Ejemplo 3: Decorador para Imprimir Nombre de la Clase

Este decorador agrega un método `imprimir_clase()` a una clase decorada para imprimir su nombre.

```python
# Definición del decorador para clases
def decorador_clase(cls):
    class NuevaClase(cls):
        def imprimir_clase(self):
            print(f"Soy una instancia de la clase {self.__class__.__name__}.")
    return NuevaClase

# Uso del decorador en una clase
@decorador_clase
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Creación de una instancia de la clase decorada
persona = Persona("Alice")
persona.saludar()       # Salida: Hola, soy Alice.
persona.imprimir_clase()  # Salida: Soy una instancia de la clase Persona.
```

En este ejemplo:
- `decorador_clase` es un decorador que toma una clase `cls` como argumento y devuelve una nueva clase `NuevaClase` que hereda de `cls`.
- `NuevaClase` agrega un método `imprimir_clase()` que imprime el nombre de la clase utilizando `self.__class__.__name__`.
- La clase `Persona` se decora con `decorador_clase`, agregando así el método `imprimir_clase()` a sus instancias.

Estos ejemplos demuestran cómo los decoradores pueden extender y modificar el comportamiento de funciones y clases de manera flexible y reutilizable en Python.