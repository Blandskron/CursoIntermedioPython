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
