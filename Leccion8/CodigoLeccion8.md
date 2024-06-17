### Ejemplo 1: Manejo de Archivos CSV

```python
import csv

# Ejemplo de escritura de datos en un archivo CSV
datos = [
    ["Nombre", "Edad", "Email"],
    ["Alice", 30, "alice@example.com"],
    ["Bob", 25, "bob@example.com"],
    ["Charlie", 35, "charlie@example.com"]
]

# Escribir datos en un archivo CSV
with open('datos.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos:
        escritor_csv.writerow(fila)

print("Archivo CSV creado exitosamente.")

# Ejemplo de lectura de datos desde un archivo CSV
with open('datos.csv', mode='r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
```

En este ejemplo:
- Se utiliza el módulo `csv` para escribir datos en un archivo CSV (`datos.csv`) y luego leerlos de nuevo.
- `csv.writer()` se utiliza para escribir filas en el archivo CSV.
- `csv.reader()` se utiliza para leer las filas del archivo CSV.

### Ejemplo 2: Manejo de Archivos JSON

```python
import json

# Ejemplo de escritura de datos en un archivo JSON
datos = {
    "empleados": [
        {"nombre": "Alice", "edad": 30, "email": "alice@example.com"},
        {"nombre": "Bob", "edad": 25, "email": "bob@example.com"},
        {"nombre": "Charlie", "edad": 35, "email": "charlie@example.com"}
    ]
}

# Escribir datos en un archivo JSON
with open('datos.json', 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)

print("Archivo JSON creado exitosamente.")

# Ejemplo de lectura de datos desde un archivo JSON
with open('datos.json', 'r') as archivo_json:
    datos_cargados = json.load(archivo_json)
    for empleado in datos_cargados['empleados']:
        print(empleado)
```

En este ejemplo:
- Se utiliza el módulo `json` para escribir datos en un archivo JSON (`datos.json`) y luego leerlos de nuevo.
- `json.dump()` se utiliza para escribir datos en el archivo JSON con formato legible.
- `json.load()` se utiliza para cargar datos desde el archivo JSON y trabajar con ellos como estructuras de datos de Python.

### Ejemplo 3: Serialización con Pickle

```python
import pickle

# Ejemplo de serialización de un objeto Python con Pickle
datos = {
    "nombre": "Alice",
    "edad": 30,
    "email": "alice@example.com"
}

# Serializar datos y guardar en un archivo binario
with open('datos.pickle', 'wb') as archivo_pickle:
    pickle.dump(datos, archivo_pickle)

print("Objeto serializado y guardado exitosamente como datos.pickle.")

# Ejemplo de deserialización de un archivo Pickle
with open('datos.pickle', 'rb') as archivo_pickle:
    datos_cargados = pickle.load(archivo_pickle)
    print("Datos cargados desde Pickle:", datos_cargados)
```

En este ejemplo:
- Se utiliza el módulo `pickle` para serializar un diccionario (`datos`) en un archivo binario (`datos.pickle`).
- `pickle.dump()` se utiliza para escribir el objeto en el archivo binario.
- `pickle.load()` se utiliza para cargar el objeto desde el archivo binario y trabajar con él como un diccionario de Python.

Estos ejemplos demuestran cómo puedes utilizar Python para manejar archivos CSV y JSON, así como realizar serialización y deserialización de objetos utilizando Pickle. Cada uno de estos métodos es útil para diferentes tipos de datos y necesidades de almacenamiento y recuperación en aplicaciones Python.