"""
02 HerenciaMultiple.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Ejemplo de herencia múltiple en Python
class A:
    # Función metodo_a: implementa una parte específica del flujo de ejemplo.
    def metodo_a(self):
        print("Método de clase A")

# Clase B: encapsula el ejemplo principal de este archivo.
class B:
    # Función metodo_b: implementa una parte específica del flujo de ejemplo.
    def metodo_b(self):
        print("Método de clase B")

# Clase C: encapsula el ejemplo principal de este archivo.
class C(A, B):
    # Función metodo_c: implementa una parte específica del flujo de ejemplo.
    def metodo_c(self):
        print("Método de clase C")

# Creación de objeto (instancia) de la clase derivada
objeto_c = C()

# Accediendo a métodos de las clases base
objeto_c.metodo_a()  # Salida: Método de clase A
objeto_c.metodo_b()  # Salida: Método de clase B
objeto_c.metodo_c()  # Salida: Método de clase C
