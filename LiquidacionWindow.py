import sys
from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QMessageBox, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from LiquidacionDAO import LiquidacionDAO
from Liquidacion import Liquidacion
import logging

ICON_DELETE_PATH = r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\Imagenes\iconos\cancel.png'  # Ajusta esta ruta a la ubicación de tu icono de eliminar

class LiquidacionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Liquidaciones")
        self.setGeometry(100, 100, 1280, 720)  # Ajustar el tamaño de la ventana

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.table.setColumnCount(11)  # Número de columnas basado en tu tabla de base de datos, más una para acciones
        self.table.setHorizontalHeaderLabels([
            "Código", "Empleado Código", "Fecha Inicial", "Fecha Final", "Motivo", "Región",
            "Mensualiza Decimotercera", "Mensualiza Decimocuarta", "Vacaciones", "Status", "Acciones"
        ])
        self.populate_table()

        self.setLayout(self.layout)

    def populate_table(self):
        try:
            liquidaciones = LiquidacionDAO.seleccionar()
            self.table.setRowCount(len(liquidaciones))
            for row, liquidacion in enumerate(liquidaciones):
                self.table.setItem(row, 0, QTableWidgetItem(liquidacion.liq_codigo))
                self.table.setItem(row, 1, QTableWidgetItem(liquidacion.emp_codigo))
                self.table.setItem(row, 2, QTableWidgetItem(str(liquidacion.liq_fecha_inicial)))
                self.table.setItem(row, 3, QTableWidgetItem(str(liquidacion.liq_fecha_final)))
                self.table.setItem(row, 4, QTableWidgetItem(liquidacion.liq_motivo))
                self.table.setItem(row, 5, QTableWidgetItem(liquidacion.liq_region))
                self.table.setItem(row, 6, QTableWidgetItem(liquidacion.liq_mensual_d_tercera))
                self.table.setItem(row, 7, QTableWidgetItem(liquidacion.liq_mensual_d_cuarta))
                self.table.setItem(row, 8, QTableWidgetItem(str(liquidacion.liq_vacaciones)))
                self.table.setItem(row, 9, QTableWidgetItem(liquidacion.liq_status))

                # Crear el botón de cancelar
                cancel_button = QPushButton()
                cancel_button.setIcon(QIcon(ICON_DELETE_PATH))
                cancel_button.setIconSize(QSize(16, 16))
                cancel_button.setToolTip("Cancelar")
                cancel_button.clicked.connect(lambda _, n=liquidacion.liq_codigo: self.confirmar_cancelar_liquidacion(n))

                # Crear el botón de editar
                edit_button = QPushButton()
                edit_button.setIcon(QIcon(r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\Imagenes\iconos\pencil.png'))  # Ajusta esta ruta a la ubicación de tu icono de lápiz
                edit_button.setIconSize(QSize(16, 16))
                edit_button.setToolTip("Editar")
                edit_button.clicked.connect(lambda _, n=liquidacion.liq_codigo: self.editar_liquidacion(n))

                action_widget = QWidget()
                action_layout = QHBoxLayout(action_widget)
                action_layout.addWidget(cancel_button)
                action_layout.addWidget(edit_button)
                action_layout.setContentsMargins(0, 0, 0, 0)
                action_layout.setSpacing(10)

                self.table.setCellWidget(row, 10, action_widget)  # Ajustar el índice para la columna de acciones
        except Exception as e:
            logging.error(f"Error al poblar la tabla de liquidaciones: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al poblar la tabla de liquidaciones: {str(e)}")

    def confirmar_cancelar_liquidacion(self, liqCodigo):
        reply = QMessageBox.question(self, 'Confirmar', '¿Está seguro de que desea desactivar esta liquidación?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cancelar_liquidacion(liqCodigo)

    def cancelar_liquidacion(self, liqCodigo):
        try:
            LiquidacionDAO.eliminar(liqCodigo)
            QMessageBox.information(self, "Información", "Liquidación desactivada exitosamente")
            self.populate_table()
        except Exception as e:
            logging.error(f"Error al desactivar la liquidación: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al desactivar la liquidación: {str(e)}")

    def editar_liquidacion(self, liqCodigo):
        try:
            liquidacion = LiquidacionDAO.buscar(liqCodigo)
            self.parent.cargar_liquidacion_por_codigo(liquidacion.liq_codigo)
            self.accept()  # Aceptar la edición y cerrar la ventana de manera controlada
        except Exception as e:
            logging.error(f"Error al editar la liquidación: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al editar la liquidación: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LiquidacionWindow()
    window.show()
    sys.exit(app.exec())
