"""
02 Colas-Queues.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Implementación de una cola en Python usando listas
from collections import deque

# Clase Cola: encapsula el ejemplo principal de este archivo.
class Cola:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self):
        self.items = deque()

    # Función esta_vacia: implementa una parte específica del flujo de ejemplo.
    def esta_vacia(self):
        return len(self.items) == 0

    # Función enqueue: implementa una parte específica del flujo de ejemplo.
    def enqueue(self, item):
        self.items.append(item)

    # Función dequeue: implementa una parte específica del flujo de ejemplo.
    def dequeue(self):
        if not self.esta_vacia():
            return self.items.popleft()

    # Función peek: implementa una parte específica del flujo de ejemplo.
    def peek(self):
        if not self.esta_vacia():
            return self.items[0]

# Ejemplo de uso de la cola
cola = Cola()
cola.enqueue("a")
cola.enqueue("b")
cola.enqueue("c")

print("Elementos de la cola:")
while not cola.esta_vacia():
    print(cola.dequeue())
