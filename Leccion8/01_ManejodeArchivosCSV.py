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
