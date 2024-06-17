## Lección: Módulos y Paquetes

### 1. Creación de Módulos y Paquetes en Python

#### Objetivos
- Comprender la importancia y la organización de código en módulos y paquetes en Python.
- Aprender cómo crear, estructurar y utilizar módulos y paquetes para organizar proyectos.
- Explorar las convenciones y prácticas recomendadas para la creación de módulos y paquetes en Python.

#### Módulos en Python

##### ¿Qué es un Módulo?
- Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, como funciones, clases y variables.
- Permite organizar el código de manera modular y reutilizable, facilitando el mantenimiento y la colaboración en proyectos.

##### Creación y Uso de Módulos

```python
# Ejemplo de creación de un módulo simple en Python

# Guardar este código en un archivo llamado mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def despedir(nombre):
    print(f"Adiós, {nombre}!")

# Utilización del módulo desde otro script
import mi_modulo

mi_modulo.saludar("Alice")
mi_modulo.despedir("Bob")
```

En este ejemplo:
- `mi_modulo.py` contiene dos funciones `saludar()` y `despedir()`.
- Desde otro script, se importa el módulo `mi_modulo` y se utilizan las funciones definidas en él.

#### Paquetes en Python

##### ¿Qué es un Paquete?
- Un paquete en Python es una colección de módulos organizados jerárquicamente en directorios.
- Permite estructurar proyectos grandes en sub-módulos más manejables y facilita la distribución y reutilización del código.

##### Creación y Estructura de Paquetes

```
mi_paquete/
│
├── __init__.py
├── modulo1.py
└── modulo2.py
```

- `__init__.py`: Este archivo indica que `mi_paquete` es un paquete Python y puede contener código de inicialización.
- `modulo1.py` y `modulo2.py`: Archivos que contienen funciones y clases relacionadas.

##### Uso de Paquetes en Python

```python
# Ejemplo de uso de un paquete en Python

# Desde otro script
from mi_paquete import modulo1, modulo2

modulo1.funcion_modulo1()
modulo2.funcion_modulo2()
```

En este ejemplo:
- Se importan los módulos `modulo1` y `modulo2` desde el paquete `mi_paquete` y se utilizan sus funciones.

### 2. Distribución de Paquetes con pip

#### Objetivos
- Entender cómo distribuir paquetes Python usando `pip`, el gestor de paquetes de Python.
- Aprender a preparar un paquete Python para su distribución en PyPI (Python Package Index).
- Explorar las mejores prácticas y herramientas para gestionar dependencias y versiones de paquetes.

#### Distribución de Paquetes con pip

##### ¿Qué es pip?
- `pip` es el gestor de paquetes de Python que facilita la instalación y gestión de paquetes y dependencias de Python.
- Permite instalar paquetes desde PyPI y otros repositorios, así como gestionar versiones y actualizar paquetes.

##### Creación de un Paquete Distribuible

Para distribuir un paquete, se necesita preparar adecuadamente la estructura y los archivos necesarios, incluyendo un archivo `setup.py` que describe cómo instalar el paquete.

```python
# setup.py
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

- `setup.py`: Define los metadatos del paquete como el nombre, versión, paquetes incluidos, dependencias requeridas, y puntos de entrada como scripts ejecutables.

##### Distribución en PyPI

Una vez preparado el paquete, se puede distribuir en PyPI para que otros puedan instalarlo fácilmente usando `pip`.

```bash
# Crear un paquete distribuible
python setup.py sdist

# Subir el paquete a PyPI (requiere cuenta en PyPI)
twine upload dist/mi_paquete-0.1.tar.gz
```

Esto permite que otros usuarios instalen el paquete con `pip install mi_paquete`.

### Resumen y Tareas

- En esta lección, exploraste cómo crear módulos y paquetes en Python para organizar y estructurar tu código de manera efectiva.
- Aprendiste cómo distribuir paquetes Python utilizando `pip` y PyPI, permitiendo a otros usuarios instalar y utilizar tu código.
- Practicaste con ejemplos que cubren desde la creación de módulos simples hasta la preparación y distribución de paquetes completos.
- **Tarea:** Crea un pequeño paquete Python que contenga al menos dos módulos y un archivo `setup.py` para prepararlo para su distribución en PyPI.
