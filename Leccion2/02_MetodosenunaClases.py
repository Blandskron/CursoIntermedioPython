"""
02 MetodosenunaClases.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Definición de una clase con métodos en Python
class Coche:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.estado = 'apagado'

    # Función encender: implementa una parte específica del flujo de ejemplo.
    def encender(self):
        self.estado = 'encendido'
        print(f"{self.marca} {self.modelo} está encendido.")

    # Función apagar: implementa una parte específica del flujo de ejemplo.
    def apagar(self):
        self.estado = 'apagado'
        print(f"{self.marca} {self.modelo} está apagado.")

# Creación de objetos (instancias) de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Uso de métodos para cambiar el estado del coche
coche1.encender()  # Salida: Toyota Corolla está encendido.
coche2.apagar()  # Salida: Honda Civic está apagado.
