## Lección: Archivos Avanzados

### 1. Manejo de Archivos CSV y JSON

#### Objetivos
- Aprender cómo leer y escribir datos en formatos estructurados como CSV y JSON en Python.
- Comprender las ventajas y usos de cada formato para almacenar y compartir datos.
- Explorar bibliotecas estándar de Python para el manejo eficiente de archivos CSV y JSON.

#### Archivos CSV

##### ¿Qué es CSV?
- CSV (Comma Separated Values) es un formato de archivo que se utiliza para almacenar datos tabulares en forma de texto plano.
- Cada línea del archivo representa una fila de datos, y los valores de cada fila están separados por comas u otro delimitador.

##### Ejemplo de Lectura y Escritura de Archivos CSV

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
- Se utiliza el módulo `csv` de Python para escribir datos en un archivo CSV (`datos.csv`) y leerlos de nuevo.
- `csv.writer()` se utiliza para escribir datos en el archivo CSV línea por línea.
- `csv.reader()` se utiliza para leer datos desde el archivo CSV línea por línea.

#### Archivos JSON

##### ¿Qué es JSON?
- JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero que se utiliza para almacenar y transferir datos estructurados entre sistemas.
- Es legible tanto para humanos como para máquinas, y soporta tipos de datos complejos como listas y diccionarios.

##### Ejemplo de Lectura y Escritura de Archivos JSON

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
- Se utiliza el módulo `json` de Python para escribir datos en un archivo JSON (`datos.json`) y leerlos de nuevo.
- `json.dump()` se utiliza para escribir datos en el archivo JSON con formato legible.
- `json.load()` se utiliza para cargar datos desde el archivo JSON y trabajar con ellos como estructuras de datos de Python.

### 2. Serialización con Pickle

#### Objetivos
- Entender qué es la serialización y por qué es útil para almacenar y recuperar objetos complejos en Python.
- Aprender a usar el módulo `pickle` de Python para serializar objetos en archivos binarios.
- Explorar casos de uso y consideraciones al trabajar con la serialización de objetos con `pickle`.

#### Serialización y Deserialización con Pickle

##### ¿Qué es Pickle?
- Pickle es un módulo de Python que permite la serialización de objetos Python en un formato binario.
- Permite guardar objetos complejos (como listas, diccionarios, clases) en archivos y luego recuperarlos para su uso posterior en la misma o en otra sesión de Python.

##### Ejemplo de Serialización y Deserialización con Pickle

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
- Se utiliza el módulo `pickle` de Python para serializar un diccionario (`datos`) en un archivo binario (`datos.pickle`).
- `pickle.dump()` se utiliza para escribir el objeto en el archivo binario.
- `pickle.load()` se utiliza para cargar el objeto desde el archivo binario y trabajar con él como un diccionario de Python.

### Resumen y Tareas

- En esta lección, exploraste técnicas avanzadas para el manejo de archivos en Python, incluyendo la lectura y escritura de archivos CSV y JSON, así como la serialización de objetos con `pickle`.
- Aprendiste a utilizar las bibliotecas estándar de Python (`csv`, `json`, `pickle`) para realizar estas tareas de manera eficiente y segura.
- Practicaste con ejemplos prácticos que cubren desde la manipulación de datos tabulares hasta la serialización de objetos complejos.
- **Tarea:** Diseña un programa que lea datos desde un archivo CSV, los procese y luego guarde el resultado en un archivo JSON utilizando las técnicas aprendidas.
