### Ejemplo 1: Herencia Simple

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

### Ejemplo 2: Herencia Múltiple

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

### Ejemplo 3: Sobrescritura de Métodos

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

Estos ejemplos demuestran cómo usar la herencia en Python para compartir y especializar comportamientos entre clases relacionadas. En el primer ejemplo, `Perro` y `Gato` heredan de `Animal`, y cada una implementa su propio método `hablar`. En el segundo ejemplo, `C` hereda de las clases `A` y `B`, aprovechando los métodos definidos en ambas. En el tercer ejemplo, `Coche` sobrescribe el método `descripcion` de la clase base `Vehiculo` para agregar información específica de un coche.