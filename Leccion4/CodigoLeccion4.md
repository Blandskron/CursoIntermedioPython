### Ejemplo 1: Captura Básica de Excepciones

```python
# Ejemplo de captura básica de excepciones en Python
try:
    num = int(input("Ingrese un número entero: "))
    resultado = 10 / num
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Ingrese un valor entero válido.")
except Exception as e:
    print(f"Error desconocido: {e}")
```

En este ejemplo:
- Se intenta dividir 10 por el número ingresado por el usuario.
- Se capturan excepciones específicas (`ZeroDivisionError` y `ValueError`) para manejar casos como división por cero o entrada no válida.
- La cláusula `except Exception as e` captura cualquier otra excepción no prevista, mostrando un mensaje genérico de error.

### Ejemplo 2: Uso de `else` y `finally`

```python
# Ejemplo de uso de cláusulas else y finally en Python
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
else:
    print("Lectura exitosa del archivo:")
    print(contenido)
finally:
    if 'archivo' in locals():
        archivo.close()
```

En este ejemplo:
- Se intenta abrir y leer el contenido de un archivo llamado "archivo.txt".
- La cláusula `else` se ejecuta si no se produce ninguna excepción durante la lectura del archivo.
- La cláusula `finally` garantiza que el archivo se cierre correctamente, incluso si se produce una excepción durante la lectura.

### Ejemplo 3: Creación de Excepciones Personalizadas

```python
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
```

En este ejemplo:
- Se define una clase `MiError` que hereda de `Exception`, permitiendo crear excepciones personalizadas con un mensaje específico.
- Se utiliza un bloque `try` para capturar la entrada de la edad, y se lanza la excepción `MiError` si la edad está fuera del rango válido (0 a 120 años).
- Se captura y maneja la excepción `MiError` en el bloque `except`, imprimiendo el mensaje de error personalizado.
