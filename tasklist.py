class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion  # Inicializa la descripción de la tarea
        self.completada = False  # Inicializa el estado de la tarea como no completada

    def completar(self):
        self.completada = True  # Marca la tarea como completada

    def __str__(self):
        # Define cómo se representa la tarea como una cadena de texto
        return self.descripcion + " [Completada]" if self.completada else self.descripcion + " [Pendiente]"


class ListaDeTareas:
    def __init__(self):
        self.tareas = []  # Inicializa la lista de tareas como vacía

    def agregar_tarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))  # Crea una nueva tarea y la agrega a la lista

    def completar_tarea(self, posicion):
        # Marca la tarea en la posición dada como completada
        # Lanza una excepción si la posición no es válida
        if posicion < 0 or posicion >= len(self.tareas):
            raise Exception("Posición no válida")
        self.tareas[posicion].completar()

    def eliminar_tarea(self, posicion):
        # Elimina la tarea en la posición dada
        # Lanza una excepción si la posición no es válida
        if posicion < 0 or posicion >= len(self.tareas):
            raise Exception("Posición no válida")
        del self.tareas[posicion]

    def mostrar_tareas(self):
        # Imprime todas las tareas en la lista o un mensaje si no hay tareas pendientes
        if not self.tareas:
            print("No tienes tareas pendientes")
        else:
            for i, tarea in enumerate(self.tareas):
                print(str(i) + ". " + str(tarea))
print("El script se ejecutó correctamente.")

# Ejemplo de uso
# lista = ListaDeTareas()
# lista.agregar_tarea("Poner lavadora")
# lista.agregar_tarea("Comprar comida gato")
# lista.mostrar_tareas()
# lista.completar_tarea(0)
# lista.mostrar_tareas()
# lista.eliminar_tarea(0)
# lista.mostrar_tareas()