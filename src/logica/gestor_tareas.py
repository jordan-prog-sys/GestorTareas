from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLineEdit, QLabel, QListWidget, QPushButton, QGridLayout
)
from PyQt6.QtCore import Qt
import sys


class InterfazTareas(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de cambio")
        self.setFixedSize(400, 300)
        self.initUI()

    def initUI(self):
        # Crear layout principal
        layout = QGridLayout()

        # Label y QLineEdit para ingresar tarea
        self.label = QLabel("Ingresar tarea")
        self.input_tarea = QLineEdit()

        # Botón para agregar tarea
        self.btn_agregar = QPushButton("Agregar")

        # QListWidget para mostrar las tareas
        self.lista_tareas = QListWidget()

        # Botones de completar y eliminar
        self.btn_completar = QPushButton("Completar")
        self.btn_eliminar = QPushButton("Eliminar")

        # Agregar widgets al layout
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.input_tarea, 0, 1)
        layout.addWidget(self.btn_agregar, 0, 2)
        layout.addWidget(self.lista_tareas, 1, 0, 1, 3)
        layout.addWidget(self.btn_completar, 2, 1)
        layout.addWidget(self.btn_eliminar, 2, 2)

        # Configurar layout del diálogo
        self.setLayout(layout)


# Para ejecutar la interfaz
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = InterfazTareas()
    dialogo.show()
    sys.exit(app.exec())