from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from NominaDAO import NominaDAO

class NominasWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Nominas")
        self.setGeometry(100, 100, 1280, 720)  # Ajustar el tamaño de la ventana

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.table.setColumnCount(15)  # Número de columnas basado en tu tabla de base de datos, más una para acciones
        self.table.setHorizontalHeaderLabels([
            "Código", "Empleado Código", "Cargo", "Nombre Empleado", "Año", "Mes",
            "Fecha Inicial", "Fecha Final", "Total Horas", "Subtotal", "Total Bonificaciones",
            "Total Descuentos", "Total", "Status", "Acciones"
        ])
        self.populate_table()

        self.setLayout(self.layout)

    def populate_table(self):
        nominas = NominaDAO.seleccionar()
        self.table.setRowCount(len(nominas))
        for row, nomina in enumerate(nominas):
            self.table.setItem(row, 0, QTableWidgetItem(nomina.nom_codigo))
            self.table.setItem(row, 1, QTableWidgetItem(nomina.emp_codigo))
            self.table.setItem(row, 2, QTableWidgetItem(nomina.emp_cargo))
            self.table.setItem(row, 3, QTableWidgetItem(nomina.nom_nombre_empleado))
            self.table.setItem(row, 4, QTableWidgetItem(nomina.nom_anio))
            self.table.setItem(row, 5, QTableWidgetItem(nomina.nom_mes))
            self.table.setItem(row, 6, QTableWidgetItem(str(nomina.nom_fecha_inicial)))
            self.table.setItem(row, 7, QTableWidgetItem(str(nomina.nom_fecha_final)))
            self.table.setItem(row, 8, QTableWidgetItem(str(nomina.nom_total_horas)))
            self.table.setItem(row, 9, QTableWidgetItem(str(nomina.nom_subtotal)))
            self.table.setItem(row, 10, QTableWidgetItem(str(nomina.nom_total_bonificaciones)))
            self.table.setItem(row, 11, QTableWidgetItem(str(nomina.nom_total_descuentos)))
            self.table.setItem(row, 12, QTableWidgetItem(str(nomina.nom_total)))
            self.table.setItem(row, 13, QTableWidgetItem(nomina.nom_status))

            # Crear el botón de cancelar
            cancel_button = QPushButton()
            cancel_button.setIcon(QIcon(r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\Imagenes\iconos\cancel.png'))
            cancel_button.setIconSize(QSize(16, 16))
            cancel_button.setToolTip("Cancelar")
            cancel_button.clicked.connect(lambda _, n=nomina.nom_codigo: self.confirmar_cancelar_nomina(n))

            # Crear el botón de editar
            edit_button = QPushButton()
            edit_button.setIcon(QIcon(r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\Imagenes\iconos\pencil.png'))
            edit_button.setIconSize(QSize(16, 16))
            edit_button.setToolTip("Editar")
            edit_button.clicked.connect(lambda _, n=nomina.nom_codigo: self.editar_nomina(n))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.addWidget(cancel_button)
            action_layout.addWidget(edit_button)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_layout.setSpacing(10)

            self.table.setCellWidget(row, 14, action_widget)  # Ajustar el índice para la columna de acciones

    def confirmar_cancelar_nomina(self, nom_codigo):
        reply = QMessageBox.question(self, 'Confirmar', '¿Está seguro de que desea desactivar esta nómina?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cancelar_nomina(nom_codigo)

    def cancelar_nomina(self, nom_codigo):
        try:
            NominaDAO.eliminar(nom_codigo)
            QMessageBox.information(self, "Información", "Nómina desactivada exitosamente")
            self.populate_table()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al desactivar la nómina: {str(e)}")

    def editar_nomina(self, nom_codigo):
        nomina = NominaDAO.buscar(nom_codigo)
        descuentos = NominaDAO.buscar_descuentos(nom_codigo)
        bonificaciones = NominaDAO.buscar_bonificaciones(nom_codigo)
        self.parent.cargar_nomina(nomina)
        self.parent.cargar_desc_bon(descuentos, bonificaciones)
        self.accept()  # Aceptar la edición y cerrar la ventana de manera controlada

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = NominasWindow()
    window.show()
    sys.exit(app.exec())
