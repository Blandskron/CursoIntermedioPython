## Lección: Iteradores y Generadores

### 1. Uso de Iteradores

#### Objetivos
- Comprender el concepto de iteradores en Python y su importancia en la iteración de secuencias de datos.
- Aprender cómo utilizar iteradores para recorrer objetos iterables como listas, tuplas y diccionarios.
- Explorar funciones y métodos integrados que facilitan el uso de iteradores.

#### ¿Qué son los Iteradores?
- Un iterador es un objeto que permite recorrer secuencialmente los elementos de un contenedor o secuencia de datos.
- Implementan los métodos `__iter__()` y `__next__()` para proporcionar acceso a los elementos uno por uno.

#### Uso de Iteradores Integrados

```python
# Ejemplo de uso de iteradores en Python
iterable = [1, 2, 3, 4, 5]
iterador = iter(iterable)

print(next(iterador))  # Salida: 1
print(next(iterador))  # Salida: 2
print(next(iterador))  # Salida: 3

# Iteración completa usando un bucle for
for elemento in iterador:
    print(elemento)  # Salida: 4 y 5
```

### 2. Creación y Uso de Generadores

#### Objetivos
- Entender qué son los generadores y cómo se diferencian de las funciones normales.
- Aprender a crear generadores utilizando la sintaxis especial de funciones generadoras.
- Explorar las ventajas de usar generadores en términos de eficiencia de memoria y rendimiento.

#### ¿Qué son los Generadores?
- Los generadores son funciones que devuelven un iterador implícito (iterable) mediante el uso de la palabra clave `yield`.
- Permiten generar valores sobre la marcha, en lugar de calcular y almacenar todos los valores de antemano.

#### Creación de Generadores

```python
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
```

#### Ventajas de los Generadores
- **Eficiencia de memoria:** Generan elementos sobre la marcha, ocupando menos espacio en memoria.
- **Rendimiento:** Adecuados para secuencias grandes de datos, evitando la sobrecarga de cálculo anticipado.

### Resumen y Tareas

- En esta lección, exploraste cómo utilizar iteradores para recorrer secuencias de datos y cómo crear generadores para generar valores de manera eficiente.
- Aprendiste sobre las diferencias clave entre funciones normales y funciones generadoras, y cómo aprovechar las ventajas de los generadores en términos de rendimiento y uso de memoria.
- **Tarea:** Diseña un programa que utilice generadores para manejar grandes volúmenes de datos de manera eficiente, aplicando los conceptos aprendidos en la lección.
