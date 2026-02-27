"""
setup.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

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
