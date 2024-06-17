### Ejemplo 1: Hilos (Threads) en Python

```python
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
```

En este ejemplo:
- Se definió la función `contar_hasta()` que simula contar hasta un número `n` con un retraso de 1 segundo entre cada conteo.
- Se crearon dos hilos (`t1` y `t2`) que ejecutan la función `contar_hasta()` con diferentes argumentos.
- Los hilos se inician con `t1.start()` y `t2.start()`, y se espera a que ambos hilos terminen con `t1.join()` y `t2.join()` antes de imprimir "Ejecución de hilos finalizada".

### Ejemplo 2: Programación Asíncrona con asyncio

```python
import asyncio

# Función asíncrona que simula contar hasta un número
async def contar_hasta(nombre, n):
    for i in range(1, n+1):
        print(f"{nombre}: {i}")
        await asyncio.sleep(1)

# Función principal asíncrona
async def main():
    # Correr tareas asíncronas concurrentemente
    tarea1 = asyncio.create_task(contar_hasta('Tarea 1', 5))
    tarea2 = asyncio.create_task(contar_hasta('Tarea 2', 3))

    # Esperar a que ambas tareas terminen
    await tarea1
    await tarea2

# Ejecutar la función principal
asyncio.run(main())
```

En este ejemplo:
- Se definió la función `contar_hasta()` como una función asíncrona utilizando `async def`.
- Dentro de `contar_hasta()`, se utilizó `await asyncio.sleep(1)` para simular una operación que toma tiempo.
- En la función `main()`, se crearon y ejecutaron dos tareas asíncronas (`tarea1` y `tarea2`) utilizando `asyncio.create_task()`.
- `asyncio.run(main())` se utilizó para ejecutar la función principal de manera asíncrona.

Estos ejemplos muestran cómo puedes utilizar hilos para lograr concurrencia básica y cómo implementar programación asíncrona con `asyncio` para manejar tareas concurrentes de manera eficiente en Python.