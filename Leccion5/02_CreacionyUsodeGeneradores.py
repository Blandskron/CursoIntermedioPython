# Ejemplo de creación de un generador en Python
def generador_pares(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 2

# Uso del generador para obtener números pares menores que 10
gen = generador_pares(10)

for numero in gen:
    print(numero)  # Salida: 0, 2, 4, 6, 8
