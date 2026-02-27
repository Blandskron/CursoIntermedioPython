# DOCUMENTACIÓN TÉCNICA Y DIDÁCTICA

Este documento complementa el `README.md` y funciona como guía de referencia rápida para estudiar y reutilizar el contenido del curso.

## 1) Convenciones usadas en los ejemplos

- Código orientado al aprendizaje: se prioriza claridad sobre optimización extrema.
- Nombres en español para mantener consistencia pedagógica.
- Ejecución directa: la mayoría de scripts están preparados para correr como ejemplos auto-contenidos.
- Comentarios descriptivos: cada archivo ahora incluye contexto, y las clases/funciones cuentan con comentarios de intención.

## 2) Mapa por competencias

### Estructuras de datos (Lección 1)
- Implementación manual de `Pila`, `Cola` y `ListaEnlazada`.
- Útil para entrevistas y bases de complejidad algorítmica.

### Programación orientada a objetos (Lecciones 2 y 3)
- Definición de clases y atributos.
- Métodos de instancia y modelado simple.
- Herencia simple/múltiple y sobrescritura de comportamiento.

### Robustez y control de fallos (Lección 4)
- Bloques `try/except/else/finally`.
- Excepciones personalizadas para reglas de negocio.

### Iteración eficiente (Lección 5)
- Diferencia entre iterables e iteradores.
- Generadores finitos e infinitos.
- Patrones de generación bajo demanda con `yield`.

### Metaprogramación ligera (Lección 6)
- Decoradores para validación, medición y extensión de clases.

### Procesamiento de texto (Lección 7)
- Expresiones regulares para búsqueda, validación y extracción.

### Persistencia de datos (Lección 8)
- Lectura/escritura de CSV y JSON.
- Serialización binaria con Pickle.

### Modularidad y distribución (Lección 9)
- Construcción de módulos y paquetes.
- Introducción a `setup.py` y punto de entrada CLI.

### Concurrencia (Lección 10)
- `threading` para tareas simultáneas con bloqueos temporales.
- `asyncio` para concurrencia cooperativa.

### Integración con APIs (Lección 11)
- Operaciones HTTP básicas (GET/POST/PUT/DELETE) con `requests`.

### Proyecto práctico (Lección 12)
- Gestión de tareas en memoria.
- API REST simple con Flask para CRUD de entradas.

## 3) Recomendaciones para practicar

1. Ejecuta cada script y observa salida esperada.
2. Cambia datos de entrada para provocar comportamientos alternativos.
3. Agrega validaciones o pruebas unitarias como ejercicio adicional.
4. En Flask/API, prueba endpoints con Postman o `curl`.

## 4) Evolución sugerida del repositorio

- Añadir carpeta `tests/` con `pytest` por lección.
- Incorporar `requirements.txt` global o por módulo.
- Agregar ejemplos con tipado (`typing`) y `dataclasses`.
- Incluir pipeline CI para lint + pruebas.

## 5) Comandos útiles

```bash
# Ejecutar comprobación de sintaxis de todo el repo
python -m compileall .

# Ejecutar ejemplo concreto
python Leccion6/01_DecoradorparaMedirTiempodeEjecucion.py

# Levantar API Flask de la lección 12
python Leccion12/app.py
```
