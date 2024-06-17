# Implementación de una pila en Python usando listas
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()

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
