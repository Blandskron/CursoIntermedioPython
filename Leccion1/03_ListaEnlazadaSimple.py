"""
03 ListaEnlazadaSimple.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Implementación de una lista enlazada simple en Python
class Nodo:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Clase ListaEnlazada: encapsula el ejemplo principal de este archivo.
class ListaEnlazada:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self):
        self.cabeza = None

    # Función esta_vacia: implementa una parte específica del flujo de ejemplo.
    def esta_vacia(self):
        return self.cabeza is None

    # Función insertar_inicio: implementa una parte específica del flujo de ejemplo.
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Función eliminar_inicio: implementa una parte específica del flujo de ejemplo.
    def eliminar_inicio(self):
        if not self.esta_vacia():
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            nodo_eliminado.siguiente = None
            return nodo_eliminado.dato

    # Función imprimir_lista: implementa una parte específica del flujo de ejemplo.
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
