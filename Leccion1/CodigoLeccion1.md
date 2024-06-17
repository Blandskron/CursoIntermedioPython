### Ejemplo de Pilas (Stacks)

```python
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
```

### Ejemplo de Colas (Queues)

```python
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
```

### Ejemplo de Lista Enlazada Simple

```python
# Implementación de una lista enlazada simple en Python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_inicio(self):
        if not self.esta_vacia():
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            nodo_eliminado.siguiente = None
            return nodo_eliminado.dato

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso de una lista enlazada simple
lista = ListaEnlazada()
lista.insertar_inicio(1)
lista.insertar_inicio(2)
lista.insertar_inicio(3)

print("Lista enlazada:")
lista.imprimir_lista()

print("Eliminando nodo del inicio:")
lista.eliminar_inicio()
lista.imprimir_lista()
```
