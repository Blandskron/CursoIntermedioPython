## Lección: Manejo de Excepciones

### 1. Captura y Manejo de Excepciones

#### Objetivos
- Entender qué son las excepciones y por qué son importantes en el manejo de errores.
- Aprender a capturar y manejar excepciones en Python.
- Explorar las cláusulas `try`, `except`, `else` y `finally` para controlar el flujo de ejecución ante excepciones.

#### ¿Qué son las Excepciones?
- Las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de instrucciones.
- Permiten manejar situaciones inesperadas, como errores de sintaxis, errores de tiempo de ejecución, entre otros.

#### Captura Básica de Excepciones

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

#### Cláusulas `else` y `finally`

- **`else`**: Se ejecuta si no se producen excepciones dentro del bloque `try`.
- **`finally`**: Se ejecuta siempre, independientemente de si se produce una excepción o no, útil para liberar recursos.

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

### 2. Creación de Excepciones Personalizadas

#### Excepciones Personalizadas
- Permite definir y lanzar excepciones personalizadas para situaciones específicas en tu programa.
- Derivar de la clase base `Exception` o alguna excepción específica según el contexto.

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

### Resumen y Tareas

- En esta lección, exploraste cómo capturar y manejar excepciones en Python utilizando las cláusulas `try`, `except`, `else` y `finally`.
- Aprendiste a crear excepciones personalizadas para manejar errores específicos según los requisitos de tu programa.
- **Tarea:** Diseña un programa que involucre el manejo de excepciones para situaciones comunes en tu dominio de aplicación, utilizando tanto excepciones integradas como personalizadas cuando sea necesario.
