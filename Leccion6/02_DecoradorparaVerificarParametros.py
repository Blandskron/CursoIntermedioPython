# Definición del decorador
def verificar_enteros(funcion):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            resultado = funcion(*args, **kwargs)
            return resultado
        else:
            raise TypeError("Todos los argumentos deben ser enteros.")
    return wrapper

# Uso del decorador
@verificar_enteros
def sumar(a, b):
    return a + b

# Llamada a la función decorada
print(sumar(3, 5))  # Salida: 8

# Si se intenta llamar sumar con un argumento no entero, generará un error
# print(sumar(3, "5"))  # Generará un TypeError
