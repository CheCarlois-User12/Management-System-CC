import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView)
from detallePaquete.Detalle import Detalle
from detallePaquete.DetalleDAO import DetalleDAO

class DetalleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD DETALLE")

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.table_layout = QVBoxLayout()

        self.entries = {}
        self.create_entries()
        self.create_buttons()
        self.create_table()

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.table_layout)
        self.setLayout(self.layout)

        self.refresh_table()

    def create_entries(self):
        fields = [
            ("EMPCODIGO", "EMP Codigo"),
            ("DETCODIGO", "DET Codigo"),
            ("DETEMPNOMBRE1", "Nombre"),
            ("DETEMPAPELLIDO1", "Apellido"),
            ("DETEMPBANCO", "Banco"),
            ("DETEMPCUENTA", "Cuenta"),
            ("DETEMPSTATUS", "Status"),
            ("DETEMPSUELDO", "Sueldo")
        ]

        for label, placeholder in fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

    def create_buttons(self):
        self.add_button = QPushButton("Guardar")
        self.add_button.clicked.connect(self.save_record)
        self.form_layout.addRow(self.add_button)

        self.update_button = QPushButton("Actualizar")
        self.update_button.clicked.connect(self.update_record)
        self.form_layout.addRow(self.update_button)

        self.delete_button = QPushButton("Eliminar")
        self.delete_button.clicked.connect(self.delete_record)
        self.form_layout.addRow(self.delete_button)

    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["EMPCODIGO", "DETCODIGO", "DETEMPNOMBRE1", "DETEMPAPELLIDO1",
                                              "DETEMPBANCO", "DETEMPCUENTA", "DETEMPSTATUS", "DETEMPSUELDO"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_layout.addWidget(self.table)

    def refresh_table(self):
        records = DetalleDAO.seleccionar()
        self.table.setRowCount(len(records))

        for row, record in enumerate(records):
            self.table.setItem(row, 0, QTableWidgetItem(record.empcodigo))
            self.table.setItem(row, 1, QTableWidgetItem(record.detcodigo))
            self.table.setItem(row, 2, QTableWidgetItem(record.detempnombre1))
            self.table.setItem(row, 3, QTableWidgetItem(record.detempapellido1))
            self.table.setItem(row, 4, QTableWidgetItem(record.detempbanco))
            self.table.setItem(row, 5, QTableWidgetItem(record.detempcuenta))
            self.table.setItem(row, 6, QTableWidgetItem(record.detempstatus))
            self.table.setItem(row, 7, QTableWidgetItem(str(record.detempsueldo)))

    def save_record(self):
        try:
            DetalleDAO.insertar(
                Detalle(
                    self.entries["EMPCODIGO"].text(),
                    self.entries["DETCODIGO"].text(),
                    self.entries["DETEMPNOMBRE1"].text(),
                    self.entries["DETEMPAPELLIDO1"].text(),
                    self.entries["DETEMPBANCO"].text(),
                    self.entries["DETEMPCUENTA"].text(),
                    self.entries["DETEMPSTATUS"].text(),
                    float(self.entries["DETEMPSUELDO"].text())
                )
            )
            QMessageBox.information(self, "Información", "Registro guardado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el registro: {e}")

    def update_record(self):
        try:
            DetalleDAO.actualizar(
                Detalle(
                    self.entries["EMPCODIGO"].text(),
                    self.entries["DETCODIGO"].text(),
                    self.entries["DETEMPNOMBRE1"].text(),
                    self.entries["DETEMPAPELLIDO1"].text(),
                    self.entries["DETEMPBANCO"].text(),
                    self.entries["DETEMPCUENTA"].text(),
                    self.entries["DETEMPSTATUS"].text(),
                    float(self.entries["DETEMPSUELDO"].text())
                )
            )
            QMessageBox.information(self, "Información", "Registro actualizado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el registro: {e}")

    def delete_record(self):
        try:
            DetalleDAO.eliminar(Detalle(detcodigo=self.entries["DETCODIGO"].text()))
            QMessageBox.information(self, "Información", "Registro eliminado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el registro: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DetalleGUI()
    gui.show()
    sys.exit(app.exec())
