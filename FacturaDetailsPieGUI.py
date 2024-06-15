import sys
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from FacturaDetailsPieForm import FacturaDetailsPieForm
from Factura import Factura
from FacturaDAO import FacturaDAO
from ClienteDAO import ClienteDAO
from ProductosDetails import ProductosDetails

class FacturaDetailsPieGUI(QWidget):
    def __init__(self):
        super(FacturaDetailsPieGUI, self).__init__()
        self.ui = FacturaDetailsPieForm()
        self.ui.setupUi(self)
        self.initUI()
        self.product_details = []  # This should be populated with ProductosDetails instances elsewhere in your program

    def initUI(self):
        self.ui.botonGenerarFactura.clicked.connect(self.generar_factura)
        self.ui.botonCancelarFactura.clicked.connect(self.cancelar_factura)
        self.load_forma_pago_options()
        self.load_cliente_codes()

    def load_forma_pago_options(self):
        # Add options to the comboBoxFormaPago
        self.ui.comboBoxFormaPago.addItems(["Efectivo", "Tarjeta", "Transferencia"])

    def load_cliente_codes(self):
        clientes = ClienteDAO.seleccionar()
        self.ui.comboBoxFormaPago.clear()
        for cliente in clientes:
            self.ui.comboBoxFormaPago.addItem(cliente.cli_codigo)

    def generar_factura(self):
        try:
            # Obtener los valores de los campos de entrada
            cliente_codigo = self.ui.comboBoxFormaPago.currentText()
            fecha = self.ui.dateEditFecha_Fact.date().toString("yyyy-MM-dd")
            hora = self.ui.lEHora_Fact.text()
            codigo_factura = self.ui.lECodigo_Fact.text()
            forma_pago = self.ui.comboBoxFormaPago.currentText()

            # Calcular los totales usando las instancias de ProductosDetails
            subtotal = sum([detalle.get_prodxdetSubtotal() for detalle in self.product_details])
            total_descuento = sum([detalle.get_prodxdetSubtotal() * detalle.get_prodxdetDescuento() / 100 for detalle in self.product_details])
            total_iva = sum([detalle.get_prodxdetDescuentoSubtotal() * (detalle.get_prodxdetIVA() / 100) for detalle in self.product_details])
            total = sum([detalle.get_prodxdetIVASubtotal() for detalle in self.product_details])

            # Crear la instancia de Factura
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
                facStatus="ACT"  # Asumiendo que el estado por defecto es "ACT"
            )

            # Insertar la factura en la base de datos
            FacturaDAO.insertar(factura)

            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Éxito", "Factura generada correctamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al generar la factura: {str(e)}")

    def cancelar_factura(self):
        # Limpiar los campos del formulario
        self.ui.comboBoxFormaPago.setCurrentIndex(0)
        self.ui.lEHora_Fact.clear()
        self.ui.lECodigo_Fact.clear()
        self.ui.comboBoxFormaPago.setCurrentIndex(0)
        self.ui.lESubTotal_FACT.clear()
        self.ui.lETotalDes_Fact.clear()
        self.ui.lETotalIva_Fact.clear()
        self.ui.lETotal_Fact.clear()
        self.ui.dateEditFecha_Fact.setDate(QDate.currentDate())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacturaDetailsPieGUI()
    window.show()
    sys.exit(app.exec())
