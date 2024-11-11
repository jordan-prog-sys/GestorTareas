from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem


class GestorTareas:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.conectar_eventos()

    def conectar_eventos(self):
        self.interfaz.btn_agregar.clicked.connect(self.agregar_tarea)
        self.interfaz.btn_completar.clicked.connect(self.completar_tarea)
        self.interfaz.btn_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        tarea_texto = self.interfaz.input_tarea.text()
        if tarea_texto:
            tarea_item = QListWidgetItem(tarea_texto)
            self.interfaz.lista_tareas.addItem(tarea_item)
            self.interfaz.input_tarea.clear()

    def completar_tarea(self):
        tarea_item = self.interfaz.lista_tareas.currentItem()
        if tarea_item:
            # Marcar la tarea como completada (opcional: tachado o color gris)
            tarea_item.setFlags(tarea_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            tarea_item.setText(f"[Completada] {tarea_item.text()}")
            tarea_item.setForeground(Qt.GlobalColor.gray)

    def eliminar_tarea(self):
        tarea_item = self.interfaz.lista_tareas.currentItem()
        if tarea_item:
            row = self.interfaz.lista_tareas.row(tarea_item)
            self.interfaz.lista_tareas.takeItem(row)