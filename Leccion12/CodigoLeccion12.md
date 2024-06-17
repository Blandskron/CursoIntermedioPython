### Ejemplo 1: Gestor de Tareas

```python
class Tarea:
    def __init__(self, descripcion, vencimiento=None):
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.completada = False
    
    def completar(self):
        self.completada = True

class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, descripcion, vencimiento=None):
        tarea = Tarea(descripcion, vencimiento)
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
    
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                vencimiento = f" (Vence el {tarea.vencimiento})" if tarea.vencimiento else ""
                print(f"{i+1}. {tarea.descripcion} - {estado}{vencimiento}")

# Ejemplo de uso del Gestor de Tareas
gestor = GestorTareas()
gestor.agregar_tarea("Estudiar para el examen de Python")
gestor.agregar_tarea("Comprar ingredientes para la cena", "2024-06-20")
gestor.listar_tareas()

# Marcar la primera tarea como completada
gestor.tareas[0].completar()
gestor.listar_tareas()

# Eliminar la segunda tarea
gestor.eliminar_tarea(1)
gestor.listar_tareas()
```

### Ejemplo 2: API para un Blog Simple con Flask

Primero, asegúrate de tener instalado Flask:

```bash
pip install Flask
```

Luego, crea el archivo `app.py` con el siguiente código:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos iniciales para simular una base de datos simple
entradas = [
    {"id": 1, "titulo": "Mi primer entrada", "contenido": "Este es el contenido de mi primer entrada."},
    {"id": 2, "titulo": "Segunda entrada", "contenido": "Contenido de la segunda entrada."},
]

# Ruta para obtener todas las entradas de blog
@app.route('/api/entradas', methods=['GET'])
def obtener_entradas():
    return jsonify(entradas)

# Ruta para obtener una entrada específica por su ID
@app.route('/api/entradas/<int:entrada_id>', methods=['GET'])
def obtener_entrada(entrada_id):
    entrada = next((e for e in entradas if e["id"] == entrada_id), None)
    if entrada:
        return jsonify(entrada)
    else:
        return jsonify({"mensaje": "Entrada no encontrada"}), 404

# Ruta para crear una nueva entrada de blog
@app.route('/api/entradas', methods=['POST'])
def crear_entrada():
    nueva_entrada = {
        "id": len(entradas) + 1,
        "titulo": request.json['titulo'],
        "contenido": request.json['contenido']
    }
    entradas.append(nueva_entrada)
    return jsonify(nueva_entrada), 201

# Ruta para actualizar una entrada de blog existente por su ID
@app.route('/api/entradas/<int:entrada_id>', methods=['PUT'])
def actualizar_entrada(entrada_id):
    entrada = next((e for e in entradas if e["id"] == entrada_id), None)
    if entrada:
        entrada['titulo'] = request.json.get('titulo', entrada['titulo'])
        entrada['contenido'] = request.json.get('contenido', entrada['contenido'])
        return jsonify(entrada), 200
    else:
        return jsonify({"mensaje": "Entrada no encontrada"}), 404

# Ruta para eliminar una entrada de blog por su ID
@app.route('/api/entradas/<int:entrada_id>', methods=['DELETE'])
def eliminar_entrada(entrada_id):
    global entradas
    entradas = [e for e in entradas if e['id'] != entrada_id]
    return jsonify({"mensaje": "Entrada eliminada"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Instrucciones de Uso

1. Ejecuta `python app.py` para iniciar el servidor Flask.
2. Usa herramientas como Postman o `requests` en Python para probar las diferentes rutas y métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`) de la API.

Estos ejemplos te permitirán implementar un Gestor de Tareas simple y una API básica para un blog utilizando Python, aplicando tus conocimientos intermedios en programación.