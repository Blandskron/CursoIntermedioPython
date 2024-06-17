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

# Ejecutar // python app.py