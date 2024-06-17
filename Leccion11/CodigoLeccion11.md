### Ejemplo 1: Peticiones HTTP con `requests`

```python
import requests

# Ejemplo de petición GET a una API pública (JSONPlaceholder)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Mostrar el contenido de la respuesta (en formato JSON en este caso)
    print(response.json())
else:
    print(f'Error al realizar la petición: {response.status_code}')
```

En este ejemplo:
- Se utiliza `requests.get()` para realizar una petición GET a la API JSONPlaceholder para obtener un post específico.
- `response.status_code` verifica el estado de la respuesta HTTP (200 indica éxito).
- `response.json()` convierte la respuesta JSON en un diccionario de Python.

### Ejemplo 2: Consumo de API RESTful con `requests`

```python
import requests

# GET request para obtener información de un recurso
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    post = response.json()
    print(f'ID del post: {post["id"]}, Título: {post["title"]}')

# POST request para crear un nuevo recurso
new_post = {'title': 'Nuevo post', 'body': 'Contenido del nuevo post', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
if response.status_code == 201:
    created_post = response.json()
    print(f'Nuevo post creado con ID: {created_post["id"]}')

# PUT request para actualizar un recurso existente
updated_post = {'title': 'Título actualizado'}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
if response.status_code == 200:
    print('Post actualizado exitosamente.')

# DELETE request para eliminar un recurso
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print('Post eliminado exitosamente.')
```

En este ejemplo:
- Se realizan varias operaciones CRUD utilizando `requests` con la API JSONPlaceholder.
- `requests.post()` se utiliza para crear un nuevo post.
- `requests.put()` actualiza el título de un post existente.
- `requests.delete()` elimina un post basado en su ID.

Estos ejemplos te permiten entender cómo usar `requests` para interactuar con APIs RESTful, realizar diversas operaciones HTTP (GET, POST, PUT, DELETE) y manipular datos en formato JSON de manera eficiente en Python.