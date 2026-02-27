# Curso Intermedio de Python

Repositorio educativo con ejemplos progresivos para reforzar fundamentos intermedios de Python, desde estructuras de datos hasta consumo de APIs y un proyecto con Flask.

## Objetivos del repositorio

- Consolidar conceptos de nivel intermedio con código corto y directo.
- Mostrar patrones reutilizables (POO, manejo de errores, generadores, decoradores, concurrencia, etc.).
- Facilitar el autoestudio mediante ejemplos comentados y documentación navegable.

## Estructura del curso

| Lección | Tema | Archivos principales |
|---|---|---|
| 1 | Estructuras de datos (pilas, colas, lista enlazada) | `Leccion1/*.py`, `Leccion1/Leccion1.md` |
| 2 | POO: clases, métodos y atributos | `Leccion2/*.py`, `Leccion2/Leccion2.md` |
| 3 | Herencia y sobrescritura | `Leccion3/*.py`, `Leccion3/Leccion3.md` |
| 4 | Excepciones y errores personalizados | `Leccion4/*.py`, `Leccion4/Leccion4.md` |
| 5 | Iteradores y generadores | `Leccion5/*.py`, `Leccion5/Leccion5.md` |
| 6 | Decoradores en funciones y clases | `Leccion6/*.py`, `Leccion6/Leccion6.md` |
| 7 | Expresiones regulares | `Leccion7/*.py`, `Leccion7/Leccion7.md` |
| 8 | CSV, JSON y Pickle | `Leccion8/*.py`, `Leccion8/Leccion8.md` |
| 9 | Módulos, paquetes y distribución | `Leccion9/**/*.py`, `Leccion9/Leccion9.md` |
| 10 | Concurrencia: threads y asyncio | `Leccion10/*.py`, `Leccion10/Leccion10.md` |
| 11 | Requests y APIs REST | `Leccion11/*.py`, `Leccion11/Leccion11.md` |
| 12 | Proyecto: gestor y API con Flask | `Leccion12/*.py`, `Leccion12/Leccion12.md` |

## Requisitos recomendados

- Python 3.10+
- `pip` actualizado
- Entorno virtual (`venv`) para ejecutar ejemplos con dependencias externas

## Ejecución rápida

```bash
# Crear y activar entorno virtual (Linux/macOS)
python -m venv .venv
source .venv/bin/activate

# Dependencias habituales de ejemplos de red/API
pip install requests flask

# Ejecutar cualquier archivo de ejemplo
python Leccion1/01_Pilas-Stacks.py
python Leccion10/02_ProgramacionAsincronaconAsyncio.py
python Leccion12/app.py
```

## Mejora de documentación aplicada

Se realizó una mejora global de documentación para maximizar claridad:

- Se añadió encabezado explicativo en **todos los archivos Python**.
- Se agregaron comentarios guía sobre clases y funciones para facilitar el aprendizaje.
- Se incorporó una guía transversal adicional en `DOCUMENTACION.md` con recomendaciones por tema.

## Ruta de aprendizaje sugerida

1. Completa Lección 1 a 4 para bases sólidas (estructuras, POO, excepciones).
2. Continúa con Lección 5 a 8 (iteración, decoradores, regex, archivos).
3. Avanza a Lección 9 a 12 para modularidad, concurrencia y APIs reales.

## Contribuciones

Si deseas mejorar ejemplos o documentación:

1. Crea una rama.
2. Realiza cambios por lección (idealmente pequeños y enfocados).
3. Abre un PR con descripción de propósito, alcance y validación ejecutada.

---

Este repositorio prioriza código didáctico, legible y fácilmente extensible.
