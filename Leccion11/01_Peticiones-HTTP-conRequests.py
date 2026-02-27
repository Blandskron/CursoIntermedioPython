"""
01 Peticiones-HTTP-conRequests.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

import requests

# Ejemplo de petición GET a una API pública (JSONPlaceholder)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Mostrar el contenido de la respuesta (en formato JSON en este caso)
    print(response.json())
else:
    print(f'Error al realizar la petición: {response.status_code}')
