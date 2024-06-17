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
