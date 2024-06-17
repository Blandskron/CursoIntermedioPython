## Lección: Introducción a la Concurrencia

### 1. Hilos (Threads) en Python

#### Objetivos
- Comprender el concepto de concurrencia y cómo los hilos pueden utilizarse para lograr ejecución concurrente en Python.
- Aprender a crear y manejar hilos utilizando el módulo `threading` de Python.
- Explorar casos de uso y consideraciones al trabajar con hilos para mejorar el rendimiento de aplicaciones.

#### Concurrencia y Hilos

##### ¿Qué es la Concurrencia?
- La concurrencia se refiere a la capacidad de un sistema para ejecutar múltiples tareas al mismo tiempo.
- En Python, los hilos (threads) son una forma de lograr concurrencia, permitiendo que múltiples partes del programa se ejecuten simultáneamente.

##### Creación y Uso de Hilos en Python

```python
import threading
import time

# Ejemplo de uso de hilos en Python

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
- Se utilizan dos hilos (`t1` y `t2`) para contar hasta un número dado.
- `threading.Thread()` se utiliza para crear un nuevo hilo, especificando la función objetivo (`target`) y los argumentos (`args`) para esa función.
- `start()` se llama para iniciar la ejecución del hilo, y `join()` se llama para esperar a que el hilo termine su ejecución antes de continuar con el hilo principal.

### 2. Programación Asíncrona con asyncio

#### Objetivos
- Entender los fundamentos de la programación asíncrona y su diferencia con la programación síncrona y concurrente.
- Aprender a utilizar `asyncio`, el módulo incorporado de Python para escribir código asíncrono de manera eficiente.
- Explorar ejemplos prácticos de cómo utilizar `asyncio` para mejorar el rendimiento en operaciones de entrada/salida (I/O) intensivas.

#### Fundamentos de Programación Asíncrona

##### ¿Qué es la Programación Asíncrona?
- La programación asíncrona permite que un programa realice otras tareas mientras espera que una operación I/O (como leer/escribir en disco o red) se complete.
- Esto mejora la eficiencia al no bloquear el hilo principal de ejecución, permitiendo que se gestionen múltiples tareas de manera concurrente.

##### Uso de asyncio en Python

```python
import asyncio

# Ejemplo de uso de asyncio en Python

async def contar_hasta(nombre, n):
    for i in range(1, n+1):
        print(f"{nombre}: {i}")
        await asyncio.sleep(1)

# Correr tareas asíncronas
async def main():
    tarea1 = asyncio.create_task(contar_hasta('Tarea 1', 5))
    tarea2 = asyncio.create_task(contar_hasta('Tarea 2', 3))

    await tarea1
    await tarea2

asyncio.run(main())
```

En este ejemplo:
- `async def` define una función asíncrona (`contar_hasta`) que puede contener operaciones asíncronas utilizando `await`.
- `asyncio.create_task()` se utiliza para ejecutar tareas asíncronas concurrentemente.
- `asyncio.sleep()` se utiliza dentro de la función asíncrona para simular una operación que toma tiempo.

### Resumen y Tareas

- En esta lección, exploraste dos enfoques para lograr concurrencia en Python: hilos (`threading`) y programación asíncrona (`asyncio`).
- Aprendiste cómo crear y manejar hilos para ejecutar múltiples tareas simultáneamente, utilizando el módulo `threading`.
- Descubriste cómo la programación asíncrona con `asyncio` puede mejorar el rendimiento al gestionar operaciones I/O intensivas de manera eficiente.
- Practicaste con ejemplos que cubren desde la creación de hilos simples hasta la implementación de tareas asíncronas con `asyncio`.
- **Tarea:** Diseña un programa que utilice tanto hilos como programación asíncrona (`asyncio`) para realizar operaciones concurrentes y compara su rendimiento y eficiencia.
