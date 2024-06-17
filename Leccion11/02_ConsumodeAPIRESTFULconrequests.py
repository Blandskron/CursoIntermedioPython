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
