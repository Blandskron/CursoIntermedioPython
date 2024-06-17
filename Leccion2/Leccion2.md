## Lección: Programación Orientada a Objetos (POO)

### 1. Clases y Objetos

#### Objetivos
- Comprender los conceptos fundamentales de la Programación Orientada a Objetos (POO).
- Aprender cómo definir clases y crear objetos en Python.
- Entender la relación entre clases, objetos y atributos.

#### Clases
- Una clase es una plantilla para crear objetos que define el comportamiento de esos objetos.
- Definición de una clase en Python:

```python
# Ejemplo de definición de una clase en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Accediendo a los atributos y métodos de los objetos
print(persona1.nombre)  # Salida: Juan
persona2.saludar()  # Salida: Hola, soy María y tengo 25 años.
```

#### Objetos
- Un objeto es una instancia específica de una clase que tiene sus propios valores para los atributos definidos en la clase.
- Cada objeto puede tener métodos (funciones asociadas) que pueden acceder y modificar sus atributos.

### 2. Métodos y Atributos

#### Métodos
- Los métodos son funciones definidas dentro de una clase que realizan operaciones específicas en los objetos de esa clase.
- Pueden acceder a los datos de la instancia a través del parámetro `self`.

```python
# Ejemplo de métodos en una clase
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
```

#### Atributos
- Los atributos son variables asociadas a objetos creados a partir de una clase.
- Pueden ser variables de instancia (asociadas a cada objeto) o variables de clase (compartidas entre todos los objetos de la misma clase).

```python
# Ejemplo de atributos en una clase
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
```

### Resumen y Tareas

- En esta lección, aprendiste los conceptos fundamentales de la Programación Orientada a Objetos (POO), incluyendo clases, objetos, métodos y atributos.
- Practicaste cómo definir clases y crear objetos en Python, así como utilizar métodos para interactuar con los objetos.
- **Tarea:** Diseña una clase nueva que modele un objeto relevante para tu área de interés o proyecto personal, definiendo sus atributos y métodos para representar su comportamiento.
