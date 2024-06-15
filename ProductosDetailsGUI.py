import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton, QMessageBox
from PySide6.QtGui import QIcon
from ProductosDetailsForm import ProductosDetailsForm
from ProductosDetails import ProductosDetails
from ProductosDetailsDAO import ProductosDetailsDAO
from ProductoDAO import ProductoDAO

# Define the paths to your icons
PENCIL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\pencil.png'
CANCEL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\cancel.png'

class ProductosDetailsGUI(QWidget):
    def __init__(self):
        super(ProductosDetailsGUI, self).__init__()
        self.ui = ProductosDetailsForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.confirmarProductoDetails.clicked.connect(self.add_product_detail)
        self.ui.botonBuscarProducto.clicked.connect(self.search_product)
        self.load_product_codes()
        self.product_details = []

    def load_product_codes(self):
        productos = ProductoDAO.seleccionar()
        self.ui.lEIDentificador.clear()
        for producto in productos:
            self.ui.lEIDentificador.addItem(producto.prod_codigo)

    def search_product(self):
        prod_codigo = self.ui.lEIDentificador.currentText()
        producto = ProductoDAO.buscar(prod_codigo)
        if producto:
            self.ui.lEUDescripcion.setText(producto.prod_descripcion)
            self.ui.lEUMedida.setText(producto.prod_unidad_medida)
            self.ui.lEVUnitario.setText(str(producto.prod_costo_x_unidad))
        else:
            QMessageBox.warning(self, "Advertencia", "Producto no encontrado")

    def add_product_detail(self):
        try:
            prod_codigo = self.ui.lEIDentificador.currentText()
            prod_descipcion = self.ui.lEUDescripcion.text()
            prod_unidad_medida = self.ui.lEUMedida.text()
            prod_costo_x_unidad = float(self.ui.lEVUnitario.text())
            prodxdet_cantidad = float(self.ui.lECantidad.text())
            prodxdet_descuento = float(self.ui.lEDescuento.text())
            prodxdet_iva = float(self.ui.lEIva.currentText())

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
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor ingrese valores válidos")

    def update_table(self):

        self.ui.tableWidget.setRowCount(len(self.product_details))
        for row, detail in enumerate(self.product_details):
            # Adding edit and delete buttons
            edit_button = QPushButton()
            edit_button.setIcon(QIcon(PENCIL_ICON_PATH))
            edit_button.clicked.connect(self.create_edit_function(row))

            delete_button = QPushButton()
            delete_button.setIcon(QIcon(CANCEL_ICON_PATH))
            delete_button.clicked.connect(self.create_delete_function(row))

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
            self.ui.tableWidget.setCellWidget(row, 10, edit_button)
            self.ui.tableWidget.setCellWidget(row, 11, delete_button)

    def create_edit_function(self, row):
        def edit():
            detail = self.product_details[row]
            self.ui.lEIDentificador.setCurrentText(detail.get_prodCodigo())
            self.ui.lEUDescripcion.setText(detail.get_prodDescipcion())
            self.ui.lEUMedida.setText(detail.get_prodUnidadMedida())
            self.ui.lEVUnitario.setText(str(detail.get_prodCostoxUnidad()))
            self.ui.lECantidad.setText(str(detail.get_prodxdetCantidad()))
            self.ui.lEDescuento.setText(str(detail.get_prodxdetDescuento()))
            self.ui.lEIva.setCurrentText(str(detail.get_prodxdetIVA()))
            self.editing_row = row
        return edit

    def create_delete_function(self, row):
        def delete():
            del self.product_details[row]
            self.update_table()
        return delete

    def clear_form(self):
        self.ui.lEIDentificador.setCurrentText("")
        self.ui.lEUDescripcion.clear()
        self.ui.lEUMedida.clear()
        self.ui.lEVUnitario.clear()
        self.ui.lECantidad.clear()
        self.ui.lEDescuento.clear()
        self.ui.lEIva.setCurrentText("0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductosDetailsGUI()
    window.show()
    sys.exit(app.exec())
