## Lección: Decoradores

### 1. Funciones Decoradoras

#### Objetivos
- Comprender qué son los decoradores en Python y cómo pueden mejorar la funcionalidad de las funciones existentes.
- Aprender a definir y aplicar funciones decoradoras para modificar o extender el comportamiento de otras funciones.
- Explorar ejemplos prácticos de uso de decoradores en diferentes contextos.

#### ¿Qué son los Decoradores?
- Los decoradores son funciones que modifican el comportamiento de otras funciones o métodos sin cambiar su código fuente.
- Utilizan la sintaxis `@decorador` colocada antes de la definición de la función a decorar.

#### Definición de un Decorador

```python
# Ejemplo básico de un decorador en Python
def decorador(funcion):
    def wrapper():
        print("Antes de llamar a la función.")
        funcion()
        print("Después de llamar a la función.")
    return wrapper

@decorador
def saludar():
    print("¡Hola, mundo!")

# Llamada a la función decorada
saludar()
```

En este ejemplo:
- `decorador` es una función que toma otra función `funcion` como argumento y define una función interna `wrapper` que envuelve la ejecución de `funcion`.
- El decorador `decorador` modifica el comportamiento de `saludar`, imprimiendo mensajes antes y después de llamar a la función original.

#### Uso de Argumentos en Decoradores

```python
# Ejemplo de decorador con argumentos en Python
def decorador_con_argumentos(arg1, arg2):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print(f"Argumentos del decorador: {arg1}, {arg2}")
            funcion(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_argumentos("Hola", "Mundo")
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# Llamada a la función decorada
saludar("Alice")
```

En este ejemplo:
- `decorador_con_argumentos` es un decorador que acepta argumentos `arg1` y `arg2`.
- Define una función interna `decorador` que a su vez define `wrapper`, el cual imprime los argumentos del decorador y luego llama a `funcion` con sus argumentos.

### 2. Decoradores Aplicados a Clases

#### Objetivos
- Entender cómo los decoradores pueden aplicarse a clases para modificar o extender su comportamiento.
- Aprender a implementar decoradores que afecten la inicialización, métodos o atributos de una clase.
- Explorar ejemplos prácticos de uso de decoradores en clases para mejorar su funcionalidad.

#### Decoradores en Clases

```python
# Ejemplo de decorador aplicado a una clase en Python
def decorador_clase(cls):
    class NuevaClase(cls):
        def nuevo_metodo(self):
            print(f"Método añadido por el decorador a la clase {cls.__name__}")
    return NuevaClase

@decorador_clase
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Uso de la clase decorada
objeto = MiClase("Alice")
objeto.saludar()    # Salida: Hola, soy Alice.
objeto.nuevo_metodo()  # Salida: Método añadido por el decorador a la clase MiClase
```

En este ejemplo:
- `decorador_clase` es un decorador que toma una clase `cls` como argumento.
- Define una nueva clase `NuevaClase` que hereda de `cls` y agrega un nuevo método `nuevo_metodo`.
- La clase `MiClase` se decora con `decorador_clase`, extendiendo su funcionalidad con el método `nuevo_metodo`.

### Resumen y Tareas

- En esta lección, exploraste cómo los decoradores pueden mejorar y extender tanto funciones como clases en Python.
- Aprendiste a implementar funciones decoradoras para modificar el comportamiento de las funciones existentes de manera no intrusiva.
- También viste cómo los decoradores pueden aplicarse a clases para añadir métodos adicionales o modificar su comportamiento inicial.
- **Tarea:** Diseña y aplica un decorador en una función o clase en tu proyecto actual o en un escenario práctico que involucre la extensión o modificación de su comportamiento.
