# Ejemplo de uso de iteradores en Python
iterable = [1, 2, 3, 4, 5]
iterador = iter(iterable)

print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3

# Iteración completa usando un bucle for
for elemento in iterador:
    print(elemento)  # Salida: 4 y 5
