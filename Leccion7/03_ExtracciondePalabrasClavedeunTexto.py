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
