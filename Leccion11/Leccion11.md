## Lección: Trabajando con APIs

### 1. Peticiones HTTP con requests

#### Objetivos
- Comprender el concepto de API (Interfaz de Programación de Aplicaciones) y su importancia en el desarrollo de software.
- Aprender a realizar peticiones HTTP utilizando la biblioteca `requests` de Python.
- Explorar los métodos HTTP comunes (GET, POST, PUT, DELETE) y cómo utilizarlos para interactuar con recursos en la web.

#### Introducción a las APIs

##### ¿Qué es una API?
- Una API (Interfaz de Programación de Aplicaciones) define un conjunto de reglas y protocolos que permiten que una aplicación se comunique con otra aplicación o servicio.
- Las APIs son fundamentales para la integración de sistemas, la automatización de procesos y el intercambio de datos entre aplicaciones.

#### Peticiones HTTP con `requests`

##### Instalación de requests

Antes de usar `requests`, asegúrate de tenerlo instalado:

```bash
pip install requests
```

##### Ejemplo de petición GET con requests

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
- Se utiliza `requests.get()` para enviar una solicitud GET a la URL especificada (`https://jsonplaceholder.typicode.com/posts/1`).
- `response.status_code` verifica el estado de la respuesta HTTP.
- `response.json()` convierte la respuesta JSON en un objeto de Python (en este caso, datos de un post).

##### Otros métodos HTTP con requests

```python
# Ejemplo de petición POST con requests
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)

# Ejemplo de petición PUT con requests
response = requests.put('https://httpbin.org/put', data={'key': 'value'})

# Ejemplo de petición DELETE con requests
response = requests.delete('https://httpbin.org/delete')
```

Estos ejemplos muestran cómo realizar peticiones POST, PUT y DELETE utilizando `requests`, proporcionando datos a través de los parámetros `data`.

### 2. Consumo de APIs RESTful

#### Objetivos
- Entender los principios de las APIs RESTful y cómo están estructuradas.
- Aprender a consumir APIs RESTful utilizando `requests` y manipular recursos como JSON.
- Explorar ejemplos prácticos de interacción con APIs RESTful populares.

#### Conceptos Básicos de APIs RESTful

##### ¿Qué es una API RESTful?
- Una API RESTful sigue los principios del estilo arquitectónico REST (Representational State Transfer), que utiliza métodos HTTP estándar para manipular recursos a través de URLs.
- Las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) se mapean a los métodos HTTP (GET, POST, PUT, DELETE) para interactuar con recursos.

##### Ejemplo de Consumo de API RESTful con requests

```python
# Ejemplo de consumo de una API RESTful con requests

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
- Se realizan diversas operaciones CRUD con una API RESTful ficticia (`https://jsonplaceholder.typicode.com`).
- Se utiliza `requests.get()` para obtener datos, `requests.post()` para crear nuevos recursos, `requests.put()` para actualizar recursos y `requests.delete()` para eliminar recursos.

### Resumen y Tareas

- En esta lección, exploraste cómo realizar peticiones HTTP utilizando `requests` y cómo consumir APIs RESTful para manipular recursos en la web.
- Aprendiste sobre los métodos HTTP (GET, POST, PUT, DELETE) y cómo utilizarlos con `requests` para interactuar con APIs.
- Practicaste con ejemplos que cubren desde la recuperación de datos hasta la creación, actualización y eliminación de recursos utilizando APIs RESTful.
- **Tarea:** Elije una API pública de tu interés (puedes explorar en `https://public-apis.xyz/`), y crea un programa en Python que interactúe con ella utilizando `requests` para realizar diversas operaciones.
