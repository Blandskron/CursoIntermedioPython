"""
01 HerenciaSimple.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de herencia simple en Python
class Animal:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, nombre):
        self.nombre = nombre

    # Función hablar: implementa una parte específica del flujo de ejemplo.
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método.")

# Clase Perro: encapsula el ejemplo principal de este archivo.
class Perro(Animal):
    # Función hablar: implementa una parte específica del flujo de ejemplo.
    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"

# Clase Gato: encapsula el ejemplo principal de este archivo.
class Gato(Animal):
    # Función hablar: implementa una parte específica del flujo de ejemplo.
    def hablar(self):
        return f"{self.nombre} dice ¡Miau!"

# Creación de objetos (instancias) de las clases derivadas
mi_perro = Perro("Bobby")
mi_gato = Gato("Misi")

print(mi_perro.hablar())  # Salida: Bobby dice ¡Guau!
print(mi_gato.hablar())   # Salida: Misi dice ¡Miau!
