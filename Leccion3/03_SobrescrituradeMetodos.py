# Ejemplo de sobrescritura de métodos en Python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}, Color: {self.color}"

# Creación de objetos (instancias) de las clases
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Accediendo a métodos sobrescritos
print(mi_coche.descripcion())  # Salida: Coche: Toyota Corolla, Color: Rojo
