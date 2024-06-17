# Definición de una clase en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Accediendo a los atributos y métodos de los objetos
print(persona1.nombre)  # Salida: Juan
persona2.saludar()  # Salida: Hola, soy María y tengo 25 años.
