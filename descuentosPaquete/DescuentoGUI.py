import sys
import functools
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView)
from descuentosPaquete.Descuento import Descuento
from descuentosPaquete.DescuentoDAO import DescuentoDAO

class DescuentoGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRUD DESCUENTOS")
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

        self.visualizar_descuentos()

    def create_entries(self):
        text_fields = [
            ("DesCodigo", "Código de Descuento", 7),
            ("DesDescripcion", "Descripción de Descuento", 150),
            ("DesValor", "Valor de Descuento", 9)
        ]

        for label, placeholder, char_width in text_fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            entry.setFixedWidth(char_width * 10)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

    def create_buttons(self):
        self.add_button = QPushButton("Guardar")
        self.add_button.clicked.connect(self.guardar_descuento)
        self.button_layout.addWidget(self.add_button)

        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.buscar_descuento)
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
        self.entries["DesCodigo"].clear()
        self.entries["DesDescripcion"].clear()
        self.entries["DesValor"].clear()

    def actualizar_campos_descuento(self, descuento):
        self.entries["DesCodigo"].setText(descuento.des_codigo)
        self.entries["DesDescripcion"].setText(descuento.des_descripcion)
        self.entries["DesValor"].setText(str(descuento.des_valor))

    def guardar_descuento(self):
        des_codigo = self.entries["DesCodigo"].text()
        descuentos = DescuentoDAO.seleccionar()
        des_existente = any(des.des_codigo == des_codigo for des in descuentos)

        try:
            descuento = Descuento(
                des_codigo=self.entries["DesCodigo"].text(),
                des_descripcion=self.entries["DesDescripcion"].text(),
                des_valor=float(self.entries["DesValor"].text())
            )

            if des_existente:
                DescuentoDAO.actualizar(descuento)
                QMessageBox.information(self, "Información", "Descuento actualizado exitosamente")
            else:
                DescuentoDAO.insertar(descuento)
                QMessageBox.information(self, "Información", "Descuento agregado exitosamente")

            self.visualizar_descuentos()  # Refresh table
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo guardar el Descuento: {e}')

    def buscar_descuento(self):
        des_codigo = self.entries["DesCodigo"].text()
        descuento = DescuentoDAO.buscar(des_codigo)
        if descuento:
            self.actualizar_campos_descuento(descuento)
        else:
            QMessageBox.warning(self, "Advertencia", "Descuento no encontrado")

    def editar_descuento(self, row):
        des_codigo = self.table.item(row, 0).text()
        descuento = DescuentoDAO.buscar(des_codigo)
        if descuento:
            self.actualizar_campos_descuento(descuento)

    def visualizar_descuentos(self):
        descuentos = DescuentoDAO.seleccionar()
        self.table.setRowCount(len(descuentos))

        for row, descuento in enumerate(descuentos):
            self.table.setItem(row, 0, QTableWidgetItem(descuento.des_codigo))
            self.table.setItem(row, 1, QTableWidgetItem(descuento.des_descripcion))
            self.table.setItem(row, 2, QTableWidgetItem(str(descuento.des_valor)))

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(functools.partial(self.editar_descuento, row))
            self.table.setCellWidget(row, 3, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(functools.partial(self.eliminar_descuento_desde_tabla, row))
            self.table.setCellWidget(row, 4, delete_button)

    def eliminar_descuento_desde_tabla(self, row):
        des_codigo = self.table.item(row, 0).text()
        descuento = Descuento(des_codigo=des_codigo)
        DescuentoDAO.eliminar(descuento)
        QMessageBox.information(self, "Información", "Descuento eliminado exitosamente")
        self.visualizar_descuentos()  # Refresh table

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DescuentoGUI()
    gui.show()
    sys.exit(app.exec())
