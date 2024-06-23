import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from LiquidacionMasterForm import LiquidacionMasterForm
from LiquidacionDAO import LiquidacionDAO
from LiquidacionCalculoDAO import LiquidacionCalculoDAO
from Liquidacion import Liquidacion
from EmpleadoDAO import EmpleadoDAO
import logging

ICON_DELETE_PATH = r"path/to/your/icon/cancel.png"  # Ajusta esta ruta a la ubicación de tu icono de cancelación

logging.basicConfig(level=logging.DEBUG)

class LiquidacionGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LiquidacionMasterForm()
        self.ui.setupUi(self)

        # Conectar botones a funciones
        self.ui.boton_calcular_Liq.clicked.connect(self.calcular_liquidacion)
        self.ui.boton_visualizar_Liq.clicked.connect(self.visualizar_liquidaciones)

        # Inicializar combo boxes
        self.populate_emp_combo_box()
        self.populate_region_combo_box()
        self.populate_motivo_combo_box()
        self.populate_mensual_combo_boxes()

    def populate_emp_combo_box(self):
        empleados = EmpleadoDAO.seleccionar()
        self.ui.cBox_empCodigo_Emp.clear()
        for emp in empleados:
            self.ui.cBox_empCodigo_Emp.addItem(emp.emp_codigo)

    def populate_region_combo_box(self):
        regiones = ["Sierra", "Costa", "Amazonia", "Insular"]
        self.ui.cBox_liqRegion_Liq.clear()
        self.ui.cBox_liqRegion_Liq.addItems(regiones)

    def populate_motivo_combo_box(self):
        motivos = [
            "Por acuerdo de las partes",
            "Por la conclusión de la obra, periodo de labor o servicios objeto del contrato",
            "Por muerte o incapacidad del empleador o extinción de la persona jurídica",
            "Por muerte del trabajador o incapacidad permanente y total para el trabajo.",
            "Por caso fortuito o fuerza mayor que imposibiliten el trabajo, como incendio, terremoto",
            "Por voluntad del empleador previo visto bueno.",
            "Por voluntad del trabajador previo visto bueno",
            "Por desahucio",
            "Por despido intempestivo"
        ]
        self.ui.cBox_liqMotivo_Liq.clear()
        self.ui.cBox_liqMotivo_Liq.addItems(motivos)

    def populate_mensual_combo_boxes(self):
        opciones = ["Si", "No"]
        self.ui.cBox_liqMensualDTercera_Liq.clear()
        self.ui.cBox_liqMensualDTercera_Liq.addItems(opciones)
        self.ui.cBox_liqMensualDCuarta_Liq.clear()
        self.ui.cBox_liqMensualDCuarta_Liq.addItems(opciones)

    def calcular_liquidacion(self):
        try:
            liq_codigo = LiquidacionDAO.generar_nuevo_codigo()
            emp_codigo = self.ui.cBox_empCodigo_Emp.currentText()
            liq_fecha_inicial = self.ui.dateEdit_nomFechaInicio_Nom.date().toPython()
            liq_fecha_final = self.ui.dateEdit_nomFechaFinal_Nom.date().toPython()
            liq_motivo = self.ui.cBox_liqMotivo_Liq.currentText()
            liq_region = self.ui.cBox_liqRegion_Liq.currentText()
            liq_mensual_d_tercera = self.ui.cBox_liqMensualDTercera_Liq.currentText()
            liq_mensual_d_cuarta = self.ui.cBox_liqMensualDCuarta_Liq.currentText()
            liq_vacaciones = int(self.ui.lEdit_liqVacaciones_Liq.text())

            liquidacion = Liquidacion(liq_codigo, emp_codigo, liq_fecha_inicial, liq_fecha_final, liq_motivo, liq_region,
                                      liq_mensual_d_tercera, liq_mensual_d_cuarta, liq_vacaciones, 'ACT')

            LiquidacionDAO.insertar(liquidacion)
            LiquidacionCalculoDAO.calcular_liquidacion(liquidacion)
            QMessageBox.information(self, "Información", "Liquidación calculada y guardada exitosamente")
        except Exception as e:
            logging.error(f"Error al calcular la liquidación: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al calcular la liquidación: {str(e)}")

    def visualizar_liquidaciones(self):
        try:
            from LiquidacionWindow import LiquidacionWindow  # Importación diferida
            ventana_liquidaciones = LiquidacionWindow(self)
            ventana_liquidaciones.exec_()
        except Exception as e:
            logging.error(f"Error al visualizar las liquidaciones: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al visualizar las liquidaciones: {str(e)}")

    def cargar_liquidacion_por_codigo(self, liq_codigo):
        try:
            liquidacion = LiquidacionDAO.buscar(liq_codigo)
            if liquidacion:
                self.ui.cBox_empCodigo_Emp.setCurrentText(liquidacion.emp_codigo)
                self.ui.dateEdit_nomFechaInicio_Nom.setDate(liquidacion.liq_fecha_inicial)
                self.ui.dateEdit_nomFechaFinal_Nom.setDate(liquidacion.liq_fecha_final)
                self.ui.cBox_liqMotivo_Liq.setCurrentText(liquidacion.liq_motivo)
                self.ui.cBox_liqRegion_Liq.setCurrentText(liquidacion.liq_region)
                self.ui.cBox_liqMensualDTercera_Liq.setCurrentText(liquidacion.liq_mensual_d_tercera)
                self.ui.cBox_liqMensualDCuarta_Liq.setCurrentText(liquidacion.liq_mensual_d_cuarta)
                self.ui.lEdit_liqVacaciones_Liq.setText(str(liquidacion.liq_vacaciones))
                QMessageBox.information(self, "Información", "Liquidación cargada exitosamente")
            else:
                QMessageBox.warning(self, "Advertencia", "No se encontró la liquidación con el código proporcionado")
        except Exception as e:
            logging.error(f"Error al cargar la liquidación: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al cargar la liquidación: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = LiquidacionGUI()
    gui.show()
    sys.exit(app.exec())
