# Ejemplo de herencia múltiple en Python
class A:
    def metodo_a(self):
        print("Método de clase A")

class B:
    def metodo_b(self):
        print("Método de clase B")

class C(A, B):
    def metodo_c(self):
        print("Método de clase C")

# Creación de objeto (instancia) de la clase derivada
objeto_c = C()

# Accediendo a métodos de las clases base
objeto_c.metodo_a()  # Salida: Método de clase A
objeto_c.metodo_b()  # Salida: Método de clase B
objeto_c.metodo_c()  # Salida: Método de clase C
