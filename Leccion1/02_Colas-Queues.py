# Implementación de una cola en Python usando listas
from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.popleft()

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
