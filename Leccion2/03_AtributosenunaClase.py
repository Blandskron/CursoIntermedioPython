# Definición de una clase con atributos en Python
class Circulo:
    pi = 3.14159  # Variable de clase

    def __init__(self, radio):
        self.radio = radio  # Variable de instancia

    def area(self):
        return self.pi * (self.radio ** 2)

# Creación de objetos (instancias) de la clase Circulo
circulo1 = Circulo(5)
circulo2 = Circulo(7)

# Accediendo a los atributos y utilizando métodos
print(circulo1.radio)  # Salida: 5
print(circulo2.area())  # Salida: 153.93886 (aprox.)
