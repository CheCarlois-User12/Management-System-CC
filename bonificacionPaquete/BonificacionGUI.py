import sys
import functools
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView)
from bonificacionPaquete.Bonificacion import Bonificacion
from bonificacionPaquete.BonificacionDAO import BonificacionDAO

class BonificacionGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRUD BONIFICACIONES")
        self.main_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.button_layout = QVBoxLayout()
        self.table_layout = QVBoxLayout()

        self.entries = {}
        self.create_entries()
        self.create_buttons()
        self.create_table()

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.table_layout)
        self.setLayout(self.main_layout)

        self.visualizar_bonificaciones()

    def create_entries(self):
        text_fields = [
            ("BonCodigo", "Código de Bonificación", 7),
            ("BonDescripcion", "Descripción de Bonificación", 150),
            ("BonValor", "Valor de Bonificación", 9)
        ]

        for label, placeholder, char_width in text_fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            entry.setFixedWidth(char_width * 10)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

    def create_buttons(self):
        self.add_button = QPushButton("Guardar")
        self.add_button.clicked.connect(self.guardar_bonificacion)
        self.button_layout.addWidget(self.add_button)

        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.buscar_bonificacion)
        self.button_layout.addWidget(self.search_button)

        self.new_button = QPushButton("Añadir")
        self.new_button.clicked.connect(self.limpiar_campos)
        self.button_layout.addWidget(self.new_button)

    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Código", "Descripción", "Valor", "Editar", "Eliminar"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_layout.addWidget(self.table)

    def limpiar_campos(self):
        self.entries["BonCodigo"].clear()
        self.entries["BonDescripcion"].clear()
        self.entries["BonValor"].clear()

    def actualizar_campos_bonificacion(self, bonificacion):
        self.entries["BonCodigo"].setText(bonificacion.bon_codigo)
        self.entries["BonDescripcion"].setText(bonificacion.bon_descripcion)
        self.entries["BonValor"].setText(str(bonificacion.bon_valor))

    def guardar_bonificacion(self):
        bon_codigo = self.entries["BonCodigo"].text()
        bonificaciones = BonificacionDAO.seleccionar()
        bon_existente = any(bon.bon_codigo == bon_codigo for bon in bonificaciones)

        try:
            bonificacion = Bonificacion(
                bon_codigo=self.entries["BonCodigo"].text(),
                bon_descripcion=self.entries["BonDescripcion"].text(),
                bon_valor=float(self.entries["BonValor"].text())
            )

            if bon_existente:
                BonificacionDAO.actualizar(bonificacion)
                QMessageBox.information(self, "Información", "Bonificación actualizada exitosamente")
            else:
                BonificacionDAO.insertar(bonificacion)
                QMessageBox.information(self, "Información", "Bonificación agregada exitosamente")

            self.visualizar_bonificaciones()  # Refresh table
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo guardar la Bonificación: {e}')

    def buscar_bonificacion(self):
        bon_codigo = self.entries["BonCodigo"].text()
        bonificacion = BonificacionDAO.buscar(bon_codigo)
        if bonificacion:
            self.actualizar_campos_bonificacion(bonificacion)
        else:
            QMessageBox.warning(self, "Advertencia", "Bonificación no encontrada")

    def editar_bonificacion(self, row):
        bon_codigo = self.table.item(row, 0).text()
        bonificacion = BonificacionDAO.buscar(bon_codigo)
        if bonificacion:
            self.actualizar_campos_bonificacion(bonificacion)

    def visualizar_bonificaciones(self):
        bonificaciones = BonificacionDAO.seleccionar()
        self.table.setRowCount(len(bonificaciones))

        for row, bonificacion in enumerate(bonificaciones):
            self.table.setItem(row, 0, QTableWidgetItem(bonificacion.bon_codigo))
            self.table.setItem(row, 1, QTableWidgetItem(bonificacion.bon_descripcion))
            self.table.setItem(row, 2, QTableWidgetItem(str(bonificacion.bon_valor)))

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(functools.partial(self.editar_bonificacion, row))
            self.table.setCellWidget(row, 3, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(functools.partial(self.eliminar_bonificacion_desde_tabla, row))
            self.table.setCellWidget(row, 4, delete_button)

    def eliminar_bonificacion_desde_tabla(self, row):
        bon_codigo = self.table.item(row, 0).text()
        bonificacion = Bonificacion(bon_codigo=bon_codigo)
        BonificacionDAO.eliminar(bonificacion)
        QMessageBox.information(self, "Información", "Bonificación eliminada exitosamente")
        self.visualizar_bonificaciones()  # Refresh table

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BonificacionGUI()
    gui.show()
    sys.exit(app.exec())
