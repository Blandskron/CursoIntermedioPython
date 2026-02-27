"""
03 SobrescrituradeMetodos.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de sobrescritura de métodos en Python
class Vehiculo:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Función descripcion: implementa una parte específica del flujo de ejemplo.
    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Clase Coche: encapsula el ejemplo principal de este archivo.
class Coche(Vehiculo):
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    # Función descripcion: implementa una parte específica del flujo de ejemplo.
    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}, Color: {self.color}"

# Creación de objetos (instancias) de las clases
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Accediendo a métodos sobrescritos
print(mi_coche.descripcion())  # Salida: Coche: Toyota Corolla, Color: Rojo
