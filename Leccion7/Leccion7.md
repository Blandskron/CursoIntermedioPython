## Lección: Expresiones Regulares

### 1. Uso de Expresiones Regulares

#### Objetivos
- Comprender qué son las expresiones regulares y por qué son útiles para manipular cadenas de texto de manera eficiente.
- Aprender la sintaxis básica de las expresiones regulares en Python para la búsqueda y manipulación de patrones en texto.
- Explorar funciones y métodos integrados que facilitan el uso de expresiones regulares.

#### ¿Qué son las Expresiones Regulares?
- Las expresiones regulares (regex) son secuencias de caracteres que forman un patrón de búsqueda.
- Permiten realizar operaciones avanzadas de búsqueda, manipulación y validación de cadenas de texto de manera flexible y poderosa.

#### Sintaxis Básica de Expresiones Regulares

- **Metacaracteres básicos:**
  - `.` : Coincide con cualquier caracter excepto nueva línea.
  - `^` : Coincide con el inicio de una cadena.
  - `$` : Coincide con el final de una cadena.
  - `\d` : Coincide con cualquier dígito decimal (0-9).
  - `\w` : Coincide con cualquier carácter alfanumérico (a-z, A-Z, 0-9, _).
  - `\s` : Coincide con cualquier carácter de espacio en blanco (espacio, tabulación, nueva línea).

#### Ejemplo de Uso de Expresiones Regulares

```python
import re

# Ejemplo básico de uso de expresiones regulares en Python
texto = "Hola, mi número de teléfono es 123-456-7890. Llámame."
patron = r'\d{3}-\d{3}-\d{4}'

# Búsqueda de coincidencias
resultado = re.search(patron, texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("Número de teléfono no encontrado.")
```

En este ejemplo:
- Se importa el módulo `re` de Python para trabajar con expresiones regulares.
- Se define un texto y un patrón de búsqueda `'\d{3}-\d{3}-\d{4}'` que busca un número de teléfono en formato ###-###-####.
- `re.search()` se utiliza para buscar el patrón en el texto y `resultado.group()` devuelve la cadena coincidente encontrada.

### 2. Búsqueda y Manipulación de Textos

#### Objetivos
- Aprender técnicas avanzadas de búsqueda y manipulación de textos utilizando expresiones regulares.
- Explorar funciones adicionales como `findall()`, `sub()` y `split()` para realizar operaciones más complejas en texto.
- Aplicar expresiones regulares en diferentes contextos prácticos como la validación de formatos y la extracción de datos.

#### Funciones Avanzadas de Expresiones Regulares

- **`re.findall(patron, texto)`** : Encuentra todas las coincidencias del patrón en el texto y devuelve una lista.
- **`re.sub(patron, nuevo_texto, texto)`** : Sustituye todas las coincidencias del patrón por `nuevo_texto`.
- **`re.split(patron, texto)`** : Divide el texto en una lista utilizando el patrón como separador.

#### Ejemplo de Uso Avanzado de Expresiones Regulares

```python
# Ejemplo de uso avanzado de expresiones regulares en Python
texto = "Fecha de nacimiento: 25-12-1990, Dirección: Calle 123, Ciudad."
patron_fecha = r'\d{2}-\d{2}-\d{4}'

# Buscar todas las fechas en el texto
fechas = re.findall(patron_fecha, texto)
print("Fechas encontradas:", fechas)

# Sustituir fechas por 'DATE'
texto_modificado = re.sub(patron_fecha, 'DATE', texto)
print("Texto modificado:", texto_modificado)

# Dividir el texto por las fechas
segmentos = re.split(patron_fecha, texto)
print("Segmentos de texto:", segmentos)
```

En este ejemplo:
- Se define un texto con información que incluye una fecha de nacimiento en formato DD-MM-AAAA.
- Se utilizan las funciones `re.findall()`, `re.sub()` y `re.split()` para encontrar todas las fechas, reemplazarlas y dividir el texto según el patrón definido.

### Resumen y Tareas

- En esta lección, exploraste cómo utilizar expresiones regulares para buscar, manipular y validar cadenas de texto de manera eficiente.
- Aprendiste la sintaxis básica de las expresiones regulares y cómo aplicarlas en Python usando el módulo `re`.
- Practicaste con ejemplos prácticos que cubren desde la búsqueda simple de patrones hasta operaciones avanzadas como sustitución y división de texto.
- **Tarea:** Diseña un programa que utilice expresiones regulares para validar y extraer información específica de un conjunto de datos o texto relevante para tu área de interés.
