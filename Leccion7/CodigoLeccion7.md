### Ejemplo 1: Búsqueda de Números de Teléfono

```python
import re

# Texto de ejemplo que contiene un número de teléfono
texto = "Mi número de teléfono es 123-456-7890. Llámame pronto."

# Patrón para buscar números de teléfono en formato ###-###-####
patron_telefono = r'\d{3}-\d{3}-\d{4}'

# Búsqueda de coincidencias utilizando re.search()
resultado = re.search(patron_telefono, texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("Número de teléfono no encontrado.")
```

En este ejemplo:
- Se utiliza `re.search()` para encontrar un número de teléfono en el texto utilizando el patrón `\d{3}-\d{3}-\d{4}`, que busca un número en formato ###-###-####.
- Si se encuentra un número de teléfono, se imprime. Si no, se muestra un mensaje indicando que no se encontró.

### Ejemplo 2: Validación de Correos Electrónicos

```python
import re

# Lista de correos electrónicos de ejemplo
correos = ["usuario1@example.com", "usuario2@gmail.com", "usuario3@example"]

# Patrón para validar direcciones de correo electrónico
patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Validación de cada correo electrónico en la lista
for correo in correos:
    if re.match(patron_correo, correo):
        print(f"{correo} es una dirección de correo válida.")
    else:
        print(f"{correo} no es una dirección de correo válida.")
```

En este ejemplo:
- Se utiliza `re.match()` para validar si cada dirección de correo electrónico en la lista `correos` coincide con el patrón especificado `^[\w\.-]+@[\w\.-]+\.\w+$`.
- Cada dirección se imprime junto con un mensaje indicando si es válida o no según el patrón.

### Ejemplo 3: Extracción de Palabras Clave de un Texto

```python
import re

# Texto de ejemplo que contiene palabras clave entre paréntesis
texto = "Este es un texto (con palabras clave) que debe ser analizado."

# Patrón para extraer palabras clave entre paréntesis
patron_palabras_clave = r'\((.*?)\)'

# Búsqueda y extracción de palabras clave utilizando re.findall()
palabras_clave = re.findall(patron_palabras_clave, texto)
if palabras_clave:
    print("Palabras clave encontradas:", palabras_clave)
else:
    print("No se encontraron palabras clave en el texto.")
```

En este ejemplo:
- Se utiliza `re.findall()` con el patrón `\((.*?)\)` para encontrar y extraer todas las palabras clave que están entre paréntesis en el texto.
- Si se encuentran palabras clave, se imprimen. Si no, se muestra un mensaje indicando que no se encontraron.

Estos ejemplos demuestran cómo puedes utilizar expresiones regulares en Python para realizar diversas operaciones como búsqueda, validación y extracción de patrones específicos en cadenas de texto.