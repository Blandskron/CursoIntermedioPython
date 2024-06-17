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
