# Definición de una clase con métodos en Python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.estado = 'apagado'

    def encender(self):
        self.estado = 'encendido'
        print(f"{self.marca} {self.modelo} está encendido.")

    def apagar(self):
        self.estado = 'apagado'
        print(f"{self.marca} {self.modelo} está apagado.")

# Creación de objetos (instancias) de la clase Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Uso de métodos para cambiar el estado del coche
coche1.encender()  # Salida: Toyota Corolla está encendido.
coche2.apagar()  # Salida: Honda Civic está apagado.
