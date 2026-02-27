"""
01 BusquedadeNumerosdeTelefono.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

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
