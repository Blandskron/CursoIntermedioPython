"""
01 Hilos-Threads.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

import threading
import time

# Función que será ejecutada por el hilo
def contar_hasta(nombre, n):
    for i in range(1, n+1):
        print(f"{nombre}: {i}")
        time.sleep(1)

# Crear hilos
t1 = threading.Thread(target=contar_hasta, args=('Hilo 1', 5))
t2 = threading.Thread(target=contar_hasta, args=('Hilo 2', 3))

# Iniciar hilos
t1.start()
t2.start()

# Esperar a que los hilos terminen
t1.join()
t2.join()

print("Ejecución de hilos finalizada.")
