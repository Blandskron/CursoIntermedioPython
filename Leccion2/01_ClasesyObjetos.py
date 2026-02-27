"""
01 ClasesyObjetos.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Definición de una clase en Python
class Persona:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Función saludar: implementa una parte específica del flujo de ejemplo.
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Accediendo a los atributos y métodos de los objetos
print(persona1.nombre)  # Salida: Juan
persona2.saludar()  # Salida: Hola, soy María y tengo 25 años.
