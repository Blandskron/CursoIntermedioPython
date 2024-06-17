# Ejemplo de herencia simple en Python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método.")

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice ¡Miau!"

# Creación de objetos (instancias) de las clases derivadas
mi_perro = Perro("Bobby")
mi_gato = Gato("Misi")

print(mi_perro.hablar())  # Salida: Bobby dice ¡Guau!
print(mi_gato.hablar())   # Salida: Misi dice ¡Miau!
