"""
03 DecoradorparaImprimirNombresdelaClase.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Definición del decorador para clases
def decorador_clase(cls):
    # Clase NuevaClase: encapsula el ejemplo principal de este archivo.
    class NuevaClase(cls):
        # Función imprimir_clase: implementa una parte específica del flujo de ejemplo.
        def imprimir_clase(self):
            print(f"Soy una instancia de la clase {self.__class__.__name__}.")
    return NuevaClase

# Uso del decorador en una clase
@decorador_clase
# Clase Persona: encapsula el ejemplo principal de este archivo.
class Persona:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, nombre):
        self.nombre = nombre

    # Función saludar: implementa una parte específica del flujo de ejemplo.
    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

# Creación de una instancia de la clase decorada
persona = Persona("Alice")
persona.saludar()       # Salida: Hola, soy Alice.
persona.imprimir_clase()  # Salida: Soy una instancia de la clase Persona.
