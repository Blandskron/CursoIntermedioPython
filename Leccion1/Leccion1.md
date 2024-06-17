## Lección 1: Estructuras de Datos Avanzadas

### 1. Pilas y Colas

#### Objetivos
- Comprender el concepto de estructuras de datos LIFO (Last In, First Out) y FIFO (First In, First Out).
- Aprender cómo implementar pilas y colas en Python y cuándo utilizar cada una.

#### Pilas (Stacks)
- Una pila es una estructura de datos donde el último elemento agregado es el primero en ser retirado.
- Operaciones principales:
  - **Push:** Agregar un elemento al tope de la pila.
  - **Pop:** Retirar el elemento del tope de la pila.

```python
# Implementación de una pila en Python usando listas
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

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

#### Colas (Queues)
- Una cola es una estructura de datos donde el primer elemento agregado es el primero en ser retirado.
- Operaciones principales:
  - **Enqueue:** Agregar un elemento al final de la cola.
  - **Dequeue:** Retirar el elemento del principio de la cola.

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

### 2. Listas Enlazadas

#### Objetivos
- Entender el concepto de listas enlazadas como estructuras de datos dinámicas.
- Aprender cómo funcionan las listas enlazadas simples y dobles, y sus aplicaciones en programación.

#### Listas Enlazadas Simples
- Una lista enlazada es una colección de nodos donde cada nodo contiene un valor y una referencia al siguiente nodo.
- Operaciones principales:
  - **Inserción:** Agregar un nodo en cualquier posición.
  - **Eliminación:** Eliminar un nodo de cualquier posición.

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

### Resumen y Tareas

- En esta lección, exploramos las estructuras de datos avanzadas como pilas, colas y listas enlazadas.
- Practicaste la implementación de pilas y colas utilizando listas y la implementación de una lista enlazada simple.
- **Tarea:** Implementa una lista enlazada doble que permita inserciones y eliminaciones desde el inicio y el final de la lista.
