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
