### Ejemplo 1: Creación y Uso de Módulos en Python

#### Archivo: mi_modulo.py

```python
# Contenido del archivo mi_modulo.py

def saludar(nombre):
    print(f"Hola, {nombre}!")

def despedir(nombre):
    print(f"Adiós, {nombre}!")
```

#### Uso del Módulo desde otro Script

```python
# Uso del módulo mi_modulo desde otro script

import mi_modulo

mi_modulo.saludar("Alice")
mi_modulo.despedir("Bob")
```

### Ejemplo 2: Creación y Uso de Paquetes en Python

#### Estructura del Paquete: mi_paquete

```
mi_paquete/
│
├── __init__.py
├── modulo1.py
└── modulo2.py
```

#### Archivo: __init__.py

```python
# Contenido del archivo __init__.py (puede estar vacío o contener código de inicialización)

```

#### Archivo: modulo1.py

```python
# Contenido del archivo modulo1.py

def funcion_modulo1():
    print("Función del módulo 1 ejecutada.")
```

#### Archivo: modulo2.py

```python
# Contenido del archivo modulo2.py

def funcion_modulo2():
    print("Función del módulo 2 ejecutada.")
```

#### Uso del Paquete desde otro Script

```python
# Uso del paquete mi_paquete desde otro script

from mi_paquete import modulo1, modulo2

modulo1.funcion_modulo1()
modulo2.funcion_modulo2()
```

### Ejemplo 3: Preparación y Distribución de un Paquete con `setup.py`

#### Archivo: setup.py

```python
from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'paquete_dependencia',
    ],
    entry_points={
        'console_scripts': [
            'mi_comando = mi_paquete.script:main',
        ],
    },
)
```

Este archivo `setup.py` describe cómo instalar el paquete `mi_paquete`, incluyendo la lista de paquetes que debe incluir, las dependencias necesarias (`paquete_dependencia` en este caso), y cómo configurar puntos de entrada como comandos de consola (`mi_comando` que ejecuta `mi_paquete.script.main`).

### Distribución del Paquete con `pip`

Para distribuir el paquete a través de PyPI, primero asegúrate de tener `twine` instalado:

```bash
pip install twine
```

Luego, puedes ejecutar los siguientes comandos:

```bash
# Crear un paquete distribuible
python setup.py sdist

# Subir el paquete a PyPI (requiere cuenta en PyPI)
twine upload dist/mi_paquete-0.1.tar.gz
```

Esto subirá el paquete `mi_paquete` con versión `0.1` al índice de paquetes Python (PyPI), permitiendo a otros usuarios instalarlo con `pip install mi_paquete`.

Estos ejemplos te proporcionan una base sólida para comenzar a trabajar con módulos, paquetes y distribución de paquetes en Python, facilitando la organización y compartición de tu código de manera efectiva.