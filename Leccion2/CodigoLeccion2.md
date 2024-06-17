### Ejemplo 1: Clases y Objetos

```python
# Definición de una clase en Python
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

### Ejemplo 2: Métodos en una Clase

```python
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
```

### Ejemplo 3: Atributos en una Clase

```python
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
```
