# Ejemplo de creación de excepción personalizada en Python
class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0 or edad > 120:
        raise MiError("La edad ingresada no es válida.")
    else:
        print(f"Edad ingresada: {edad}")
except MiError as e:
    print(e)
except ValueError:
    print("Error: Ingrese un número entero válido para la edad.")
