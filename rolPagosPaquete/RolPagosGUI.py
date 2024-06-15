import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView)
from rolPagosPaquete.RolPagos import RolPagos
from rolPagosPaquete.RolPagosDAO import RolPagosDAO

class RolPagosGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD ROLPAGOS")

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
            ("ROLCODIGO", "ROL Codigo"),
            ("BONXDESCODIGO", "BONXDES Codigo"),
            ("DETCODIGO", "DET Codigo"),
            ("ROLTOTALBENEFICIOS", "Total Beneficios"),
            ("ROLTOTALDESCUENTOS", "Total Descuentos"),
            ("ROLSUBTOTAL", "Subtotal"),
            ("ROLTOTALPAGAR", "Total Pagar")
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
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ROLCODIGO", "BONXDESCODIGO", "DETCODIGO", "ROLTOTALBENEFICIOS",
                                              "ROLTOTALDESCUENTOS", "ROLSUBTOTAL", "ROLTOTALPAGAR"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_layout.addWidget(self.table)

    def refresh_table(self):
        records = RolPagosDAO.seleccionar()
        self.table.setRowCount(len(records))

        for row, record in enumerate(records):
            self.table.setItem(row, 0, QTableWidgetItem(record.rolcodigo))
            self.table.setItem(row, 1, QTableWidgetItem(record.bonxdescodigo))
            self.table.setItem(row, 2, QTableWidgetItem(record.detcodigo))
            self.table.setItem(row, 3, QTableWidgetItem(str(record.roltotalbeneficios)))
            self.table.setItem(row, 4, QTableWidgetItem(str(record.roltotaldescuentos)))
            self.table.setItem(row, 5, QTableWidgetItem(str(record.rolsubtotal)))
            self.table.setItem(row, 6, QTableWidgetItem(str(record.roltotalpagar)))

    def save_record(self):
        try:
            RolPagosDAO.insertar(
                RolPagos(
                    self.entries["ROLCODIGO"].text(),
                    self.entries["BONXDESCODIGO"].text(),
                    self.entries["DETCODIGO"].text(),
                    float(self.entries["ROLTOTALBENEFICIOS"].text()),
                    float(self.entries["ROLTOTALDESCUENTOS"].text()),
                    float(self.entries["ROLSUBTOTAL"].text()),
                    float(self.entries["ROLTOTALPAGAR"].text())
                )
            )
            QMessageBox.information(self, "Información", "Registro guardado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el registro: {e}")

    def update_record(self):
        try:
            RolPagosDAO.actualizar(
                RolPagos(
                    self.entries["ROLCODIGO"].text(),
                    self.entries["BONXDESCODIGO"].text(),
                    self.entries["DETCODIGO"].text(),
                    float(self.entries["ROLTOTALBENEFICIOS"].text()),
                    float(self.entries["ROLTOTALDESCUENTOS"].text()),
                    float(self.entries["ROLSUBTOTAL"].text()),
                    float(self.entries["ROLTOTALPAGAR"].text())
                )
            )
            QMessageBox.information(self, "Información", "Registro actualizado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el registro: {e}")

    def delete_record(self):
        try:
            RolPagosDAO.eliminar(RolPagos(rolcodigo=self.entries["ROLCODIGO"].text()))
            QMessageBox.information(self, "Información", "Registro eliminado exitosamente")
            self.refresh_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el registro: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = RolPagosGUI()
    gui.show()
    sys.exit(app.exec())
