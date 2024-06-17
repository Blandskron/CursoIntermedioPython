# Ejemplo de generador infinito en Python
def generador_infinito():
    num = 1
    while True:
        yield num
        num += 1

# Uso del generador infinito para obtener los primeros 5 números naturales
gen = generador_infinito()

for _ in range(5):
    print(next(gen))  # Salida: 1, 2, 3, 4, 5
