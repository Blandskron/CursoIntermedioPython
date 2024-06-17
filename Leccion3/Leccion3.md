## Lección: Herencia y Polimorfismo

### 1. Herencia

#### Objetivos
- Entender el concepto de herencia en Programación Orientada a Objetos (POO).
- Aprender cómo se implementa la herencia en Python y sus beneficios.
- Comprender la relación entre clases base (padre) y clases derivadas (hija).

#### Herencia Simple
- La herencia simple permite que una clase (hija) herede atributos y métodos de otra clase (padre).
- Sintaxis para definir una clase que hereda de otra en Python:

```python
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
```

#### Herencia Múltiple
- Python soporta herencia múltiple, lo que significa que una clase puede heredar de múltiples clases base.
- Sintaxis para herencia múltiple:

```python
# Ejemplo de herencia múltiple en Python
class A:
    def metodo_a(self):
        print("Método de clase A")

class B:
    def metodo_b(self):
        print("Método de clase B")

class C(A, B):
    def metodo_c(self):
        print("Método de clase C")

# Creación de objeto (instancia) de la clase derivada
objeto_c = C()

# Accediendo a métodos de las clases base
objeto_c.metodo_a()  # Salida: Método de clase A
objeto_c.metodo_b()  # Salida: Método de clase B
objeto_c.metodo_c()  # Salida: Método de clase C
```

### 2. Sobrescritura de Métodos

#### Sobrescritura en Herencia
- La sobrescritura de métodos permite que una clase hija redefina un método que hereda de su clase padre.
- Permite personalizar el comportamiento de los métodos según las necesidades de la clase hija.

```python
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
```

### Resumen y Tareas

- En esta lección, exploraste los conceptos de herencia simple y múltiple en Python, así como la sobrescritura de métodos.
- Aprendiste cómo una clase puede heredar atributos y métodos de otra clase, y cómo modificar el comportamiento de los métodos en la clase hija.
- **Tarea:** Diseña una jerarquía de clases para modelar entidades relacionadas con tu área de interés o proyecto personal, aplicando los conceptos de herencia y sobrescritura de métodos.
