import datetime
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox, QVBoxLayout, \
    QHeaderView, QTableWidget, QWidget
from PySide6.QtCore import QDate, QTime, Qt
from FacturasMasterForm import FacturasMasterForm
from ProductosDetails import ProductosDetails
from ProductoDAO import ProductoDAO
from ClienteDAO import ClienteDAO
from FacturaDAO import FacturaDAO
from Factura import Factura
import re

class FacturasMasterGUI(QMainWindow):
    def __init__(self):
        super(FacturasMasterGUI, self).__init__()
        self.ui = FacturasMasterForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.boton_Buscar_PDetail.clicked.connect(self.search_product)
        self.ui.boton_Confirmar_PDetail.clicked.connect(self.add_product_detail)
        self.ui.boton_GenerarFact_Fact.clicked.connect(self.generar_factura)
        self.ui.boton_Cancelar_Fact.clicked.connect(self.cancelar_factura)
        self.ui.boton_BuscarCodigo_Cli.clicked.connect(self.search_client)
        self.ui.boton_VisualizarFact_Fact.clicked.connect(self.visualizar_facturas)  # Conectar el nuevo botón
        self.load_product_codes()
        self.load_forma_pago_options()
        self.load_cliente_codes()
        self.load_iva_options()
        self.product_details = []

        self.setup_table()

    def setup_table(self):
        self.ui.tableWidget.setColumnCount(12)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "Código", "Descripción", "Unidad de Medida", "Valor Unitario",
            "Cantidad", "Descuento", "Subtotal", "Desc. Subtotal",
            "IVA", "IVA Subtotal", "Editar", "Eliminar"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_product_codes(self):
        productos = ProductoDAO.seleccionar()
        self.ui.cBox_proCodigo_PDetail.clear()
        for producto in productos:
            self.ui.cBox_proCodigo_PDetail.addItem(producto.prod_codigo)

    def load_forma_pago_options(self):
        self.ui.cBox_FormaPago_Fact.addItems(["EFECT", "TARJE", "TRANS"])

    def load_cliente_codes(self):
        clientes = ClienteDAO.seleccionar()
        self.ui.cBox_CodigoClientes_Cli.clear()
        for cliente in clientes:
            self.ui.cBox_CodigoClientes_Cli.addItem(cliente.cli_codigo)

    def load_iva_options(self):
        self.ui.cBox_IVA_PDetail.addItems(["0", "8", "12", "15"])

    def search_client(self):
        cli_codigo = self.ui.cBox_CodigoClientes_Cli.currentText()
        cliente = ClienteDAO.buscar(cli_codigo)
        if cliente:
            self.ui.lineEdit_cliIdentificacion_Cli.setText(cliente.cli_identificacion)
            self.ui.lineEdit_NombreCli_Fact.setText(cliente.cli_nombre)
        else:
            QMessageBox.warning(self, "Advertencia", "Cliente no encontrado")

    def search_product(self):
        prod_codigo = self.ui.cBox_proCodigo_PDetail.currentText()
        producto = ProductoDAO.buscar(prod_codigo)
        if producto:
            self.ui.lineEdit_Descripcion_PDetail.setText(producto.prod_descripcion)
            self.ui.lineEdit_UMedida_PDetail.setText(producto.prod_unidad_medida)
            self.ui.lineEdit_VUnitario_PDetail.setText(str(producto.prod_costo_x_unidad))
        else:
            QMessageBox.warning(self, "Advertencia", "Producto no encontrado")

    def add_product_detail(self):
        try:
            prod_codigo = self.ui.cBox_proCodigo_PDetail.currentText()
            prod_descipcion = self.ui.lineEdit_Descripcion_PDetail.text()
            prod_unidad_medida = self.ui.lineEdit_UMedida_PDetail.text()
            prod_costo_x_unidad = float(self.ui.lineEdit_VUnitario_PDetail.text())
            prodxdet_cantidad = float(self.ui.lineEdit_Cantidad_PDetail.text())
            prodxdet_descuento = float(self.ui.lineEdit_Descuento_PDetail.text())
            prodxdet_iva = float(self.ui.cBox_IVA_PDetail.currentText())

            if prodxdet_cantidad < 0 or prodxdet_descuento < 0:
                raise ValueError("Cantidad y Descuento no pueden ser negativos.")

            product_detail = ProductosDetails(
                prodCodigo=prod_codigo,
                prodDescipcion=prod_descipcion,
                prodUnidadMedida=prod_unidad_medida,
                prodCostoxUnidad=prod_costo_x_unidad,
                prodxdetCantidad=prodxdet_cantidad,
                prodxdetDescuento=prodxdet_descuento,
                prodxdetIVA=prodxdet_iva
            )

            self.product_details.append(product_detail)
            self.update_table()
            self.update_totals()
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_table(self):
        self.ui.tableWidget.setRowCount(len(self.product_details))
        for row, detail in enumerate(self.product_details):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(detail.get_prodCodigo()))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(detail.get_prodDescipcion()))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(detail.get_prodUnidadMedida()))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(detail.get_prodCostoxUnidad())))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(detail.get_prodxdetCantidad())))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(detail.get_prodxdetDescuento())))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(detail.get_prodxdetSubtotal())))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(detail.get_prodxdetDescuentoSubtotal())))
            self.ui.tableWidget.setItem(row, 8, QTableWidgetItem(str(detail.get_prodxdetIVA())))
            self.ui.tableWidget.setItem(row, 9, QTableWidgetItem(str(detail.get_prodxdetIVASubtotal())))

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.create_edit_function(row))

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.create_delete_function(row))

            self.ui.tableWidget.setCellWidget(row, 10, edit_button)
            self.ui.tableWidget.setCellWidget(row, 11, delete_button)

    def create_edit_function(self, row):
        def edit():
            detail = self.product_details[row]
            self.ui.cBox_proCodigo_PDetail.setCurrentText(detail.get_prodCodigo())
            self.ui.lineEdit_Descripcion_PDetail.setText(detail.get_prodDescipcion())
            self.ui.lineEdit_UMedida_PDetail.setText(detail.get_prodUnidadMedida())
            self.ui.lineEdit_VUnitario_PDetail.setText(str(detail.get_prodCostoxUnidad()))
            self.ui.lineEdit_Cantidad_PDetail.setText(str(detail.get_prodxdetCantidad()))
            self.ui.lineEdit_Descuento_PDetail.setText(str(detail.get_prodxdetDescuento()))
            self.ui.cBox_IVA_PDetail.setCurrentText(str(detail.get_prodxdetIVA()))
            self.editing_row = row
        return edit

    def create_delete_function(self, row):
        def delete():
            del self.product_details[row]
            self.update_table()
            self.update_totals()
        return delete

    def update_totals(self):
        subtotal = sum([detail.get_prodxdetSubtotal() for detail in self.product_details])
        total_descuento = sum([detail.get_prodxdetSubtotal() * detail.get_prodxdetDescuento() / 100 for detail in self.product_details])
        total_iva = sum([detail.get_prodxdetDescuentoSubtotal() * (detail.get_prodxdetIVA() / 100) for detail in self.product_details])
        total = sum([detail.get_prodxdetIVASubtotal() for detail in self.product_details])

        self.ui.lineEdit_SubTotal_Fact.setText(str(subtotal))
        self.ui.lineEdit_totalDesc.setText(str(total_descuento))
        self.ui.lineEdit_TotalIva_Fact.setText(str(total_iva))
        self.ui.lineEdit_Total_Fact.setText(str(total))

    def generar_factura(self):
        try:
            cliente_codigo = self.ui.cBox_CodigoClientes_Cli.currentText()
            fecha = self.ui.dateEdit_Fecha_Fact.date().toString("yyyy-MM-dd")
            hora = QTime.currentTime().toString()
            codigo_factura = self.ui.lineEdit_CodigoFact_Fact.text()
            forma_pago = self.ui.cBox_FormaPago_Fact.currentText()

            if not re.match(r"^FAC-\d{5}$", codigo_factura):
                raise ValueError("El código de la factura debe tener el formato 'FAC-#####'.")

            if QDate.fromString(fecha, "yyyy-MM-dd") > QDate.currentDate():
                raise ValueError("La fecha de la factura no puede ser mayor a la fecha actual.")

            subtotal = float(self.ui.lineEdit_SubTotal_Fact.text())
            total_descuento = float(self.ui.lineEdit_totalDesc.text())
            total_iva = float(self.ui.lineEdit_TotalIva_Fact.text())
            total = float(self.ui.lineEdit_Total_Fact.text())

            factura = Factura(
                facCodigo=codigo_factura,
                cliCodigo=cliente_codigo,
                facFecha=fecha,
                facHora=hora,
                facSubtotal=subtotal,
                facDescuento=total_descuento,
                facIva=total_iva,
                facTotal=total,
                facFormaPago=forma_pago,
                facStatus="ACT"
            )

            FacturaDAO.insertar(factura)
            QMessageBox.information(self, "Éxito", "Factura generada correctamente")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al generar la factura: {str(e)}")

    def cancelar_factura(self):
        self.ui.cBox_CodigoClientes_Cli.setCurrentIndex(0)
        self.ui.lineEdit_Hora_Fact.clear()
        self.ui.lineEdit_CodigoFact_Fact.clear()
        self.ui.cBox_FormaPago_Fact.setCurrentIndex(0)
        self.ui.lineEdit_SubTotal_Fact.clear()
        self.ui.lineEdit_totalDesc.clear()
        self.ui.lineEdit_TotalIva_Fact.clear()
        self.ui.lineEdit_Total_Fact.clear()
        self.ui.dateEdit_Fecha_Fact.setDate(QDate.currentDate())

    def visualizar_facturas(self):
        self.visualizar_facturas_window = VisualizarFacturasWindow()
        self.visualizar_facturas_window.show()

class VisualizarFacturasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizar Facturas")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels([
            "Código", "Cliente", "Fecha", "Hora",
            "Subtotal", "Descuento", "IVA", "Total"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tableWidget)

        self.load_facturas()

    def load_facturas(self):
        facturas = FacturaDAO.seleccionar()  # Asegúrate de que este método existe en FacturaDAO
        self.tableWidget.setRowCount(len(facturas))
        for row, factura in enumerate(facturas):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(factura.facCodigo))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(factura.cliCodigo))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(factura.facFecha)))  # Convertir fecha a cadena
            self.tableWidget.setItem(row, 3, QTableWidgetItem(self.format_time(factura.facHora)))  # Convertir hora a cadena
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(factura.facSubtotal)))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(factura.facDescuento)))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(factura.facIva)))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(str(factura.facTotal)))

    def format_time(self, time_value):
        """Formato de la hora para manejar diferentes tipos de valores de tiempo."""
        if isinstance(time_value, (datetime.time, datetime.datetime)):
            return time_value.strftime("%H:%M:%S")
        elif isinstance(time_value, datetime.timedelta):
            total_seconds = int(time_value.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            return str(time_value)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacturasMasterGUI()
    window.show()
    sys.exit(app.exec())
