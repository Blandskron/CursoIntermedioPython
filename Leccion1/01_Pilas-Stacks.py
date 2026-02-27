"""
01 Pilas-Stacks.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Implementación de una pila en Python usando listas
class Pila:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self):
        self.items = []

    # Función esta_vacia: implementa una parte específica del flujo de ejemplo.
    def esta_vacia(self):
        return len(self.items) == 0

    # Función push: implementa una parte específica del flujo de ejemplo.
    def push(self, item):
        self.items.append(item)

    # Función pop: implementa una parte específica del flujo de ejemplo.
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

    # Función peek: implementa una parte específica del flujo de ejemplo.
    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]

# Ejemplo de uso de la pila
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print("Elementos de la pila:")
while not pila.esta_vacia():
    print(pila.pop())
