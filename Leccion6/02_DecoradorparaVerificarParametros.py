"""
02 DecoradorparaVerificarParametros.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Definición del decorador
def verificar_enteros(funcion):
    # Función wrapper: implementa una parte específica del flujo de ejemplo.
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            resultado = funcion(*args, **kwargs)
            return resultado
        else:
            raise TypeError("Todos los argumentos deben ser enteros.")
    return wrapper

# Uso del decorador
@verificar_enteros
# Función sumar: implementa una parte específica del flujo de ejemplo.
def sumar(a, b):
    return a + b

# Llamada a la función decorada
print(sumar(3, 5))  # Salida: 8

# Si se intenta llamar sumar con un argumento no entero, generará un error
# print(sumar(3, "5"))  # Generará un TypeError
