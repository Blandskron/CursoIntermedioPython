"""
01 GestordeTareas.

Archivo didáctico del curso intermedio de Python.
Incluye comentarios y ejemplos para facilitar su estudio paso a paso.
"""

# Clase Tarea: encapsula el ejemplo principal de este archivo.
class Tarea:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self, descripcion, vencimiento=None):
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.completada = False
    
    # Función completar: implementa una parte específica del flujo de ejemplo.
    def completar(self):
        self.completada = True

# Clase GestorTareas: encapsula el ejemplo principal de este archivo.
class GestorTareas:
    # Función __init__: implementa una parte específica del flujo de ejemplo.
    def __init__(self):
        self.tareas = []
    
    # Función agregar_tarea: implementa una parte específica del flujo de ejemplo.
    def agregar_tarea(self, descripcion, vencimiento=None):
        tarea = Tarea(descripcion, vencimiento)
        self.tareas.append(tarea)
    
    # Función eliminar_tarea: implementa una parte específica del flujo de ejemplo.
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
    
    # Función listar_tareas: implementa una parte específica del flujo de ejemplo.
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                vencimiento = f" (Vence el {tarea.vencimiento})" if tarea.vencimiento else ""
                print(f"{i+1}. {tarea.descripcion} - {estado}{vencimiento}")

# Ejemplo de uso del Gestor de Tareas
gestor = GestorTareas()
gestor.agregar_tarea("Estudiar para el examen de Python")
gestor.agregar_tarea("Comprar ingredientes para la cena", "2024-06-20")
gestor.listar_tareas()

# Marcar la primera tarea como completada
gestor.tareas[0].completar()
gestor.listar_tareas()

# Eliminar la segunda tarea
gestor.eliminar_tarea(1)
gestor.listar_tareas()
