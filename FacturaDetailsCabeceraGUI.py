import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from FacturaDetailsCabeceraForm import FacturaDetailsCabeceraForm
from ClienteDAO import ClienteDAO

class FacturaDetailsCabeceraGUI(QWidget):
    def __init__(self):
        super(FacturaDetailsCabeceraGUI, self).__init__()
        self.ui = FacturaDetailsCabeceraForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.botonBuscar_Cliente.clicked.connect(self.search_client)
        self.load_client_codes()

    def load_client_codes(self):
        clientes = ClienteDAO.seleccionar_codigos()
        self.ui.comboBoxCodigo_Cliente.clear()
        for cliente in clientes:
            self.ui.comboBoxCodigo_Cliente.addItem(cliente)

    def search_client(self):
        cli_codigo = self.ui.comboBoxCodigo_Cliente.currentText()
        cliente = ClienteDAO.buscar(cli_codigo)
        if cliente:
            self.ui.lERoC_Cliente.setText(cliente.cli_identificacion)
            self.ui.IECliente_Fact.setText(cliente.cli_nombre)
        else:
            QMessageBox.warning(self, "Advertencia", "Cliente no encontrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacturaDetailsCabeceraGUI()
    window.show()
    sys.exit(app.exec())
