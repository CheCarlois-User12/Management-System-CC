import sys
import json
import base64

import mysql
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QLineEdit
from PySide6.QtGui import QIcon
from EmpleadoGUI import EmpleadoGUI
from bonificacionPaquete.BonificacionGUI import BonificacionGUI
from descuentosPaquete.DescuentoGUI import DescuentoGUI
from detallePaquete.DetalleGUI import DetalleGUI
from bonxdesxoPaquete.BonxdesxoGUI import BonxdesxoGUI
from rolPagosPaquete.RolPagosGUI import RolPagosGUI
from ClienteGUI import ClienteGUI
from ProductoGUI import ProductoGUI
from FacturaMasterGUI import FacturasMasterGUI
from form_ui import Ui_MainWindow
from conexion import Conexion
from RSAProteccion import RSAProteccion

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("EMPLEADOS MANAGEMENT SYSTEM")
        self.show_welcome_message()
        self.inicializar_Botones()
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, False)
        self.update_tab_icons(False)
        self.is_logged_in = False
        self.fVTablasTalentoHumano_1.setLayout(QVBoxLayout())
        self.fVTablasVentas_1.setLayout(QVBoxLayout())
        self.entryClave_1.setEchoMode(QLineEdit.Password)

        self.rsa_proteccion = RSAProteccion()
        self.rsa_proteccion.load_keys('private_key.pem', 'public_key.pem')

    def inicializar_Botones(self):
        self.botonEmpleados.clicked.connect(self.show_empleados)
        self.botonBonificaciones.clicked.connect(self.show_bonificaciones)
        self.botonDescuentos.clicked.connect(self.show_descuentos)
        self.botonDetalle.clicked.connect(self.show_detalle)
        self.botonRolPagos.clicked.connect(self.show_rolpagos)
        self.botonBonxDes.clicked.connect(self.show_bonxdes)
        self.botonIniciarSesion_1.clicked.connect(self.login)
        self.botonCerrarSesion_1.clicked.connect(self.logout)
        self.botonClientes.clicked.connect(self.show_clientes)
        self.botonFACTxDETAILS.clicked.connect(self.show_factxdetails)
        self.botonProductos.clicked.connect(self.show_productos)

    def show_welcome_message(self):
        QMessageBox.information(self, "Bienvenido", "Bienvenido al sistema")

    def actualizar_configuracion(self, usuario, clave):
        config_path = r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\conexiones_base_datos.json'
        encrypted_user = base64.b64encode(self.rsa_proteccion.encrypt(usuario)).decode('utf-8')
        encrypted_password = base64.b64encode(self.rsa_proteccion.encrypt(clave)).decode('utf-8')
        config = {
            'user': encrypted_user,
            'password': encrypted_password
        }
        with open(config_path, 'w') as file:
            json.dump(config, file)

    def login(self):
        usuario = self.entryUsuario_1.text()
        clave = self.entryClave_1.text()
        self.actualizar_configuracion(usuario, clave)
        try:
            conexion = Conexion.obtenerConexion()
            self.is_logged_in = True
            if usuario == "adminUser":
                self.tabWidget.setTabEnabled(0, True)
                self.tabWidget.setTabEnabled(1, True)
                self.update_tab_icons(True)
                self.tabWidget.setCurrentIndex(0)
                self.initialize_guis("admin")
            elif usuario == "MasterFacturacionUser":
                self.tabWidget.setTabEnabled(0, False)
                self.tabWidget.setTabEnabled(1, True)
                self.update_tab_icons(True)
                self.tabWidget.setCurrentIndex(1)
                self.initialize_guis("facturacion")
            elif usuario == "MasterTalentoHumanoUser":
                self.tabWidget.setTabEnabled(0, True)
                self.tabWidget.setTabEnabled(1, False)
                self.update_tab_icons(True)
                self.tabWidget.setCurrentIndex(0)
                self.initialize_guis("talento_humano")
            else:
                QMessageBox.warning(self, "Login fallido", "Usuario o clave incorrectos")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error de conexión: {err.errno} ({err.sqlstate}): {err.msg}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error desconocido: {str(e)}")

    def logout(self):
        self.is_logged_in = False
        self.entryUsuario_1.clear()
        self.entryClave_1.clear()
        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, False)
        self.update_tab_icons(False)
        self.tabWidget.setCurrentIndex(2)
        Conexion.limpiar_configuracion()

    def closeEvent(self, event):
        if self.is_logged_in:
            Conexion.limpiar_configuracion()
        event.accept()

    def update_tab_icons(self, logged_in):
        if logged_in:
            self.tabWidget.setTabIcon(0, QIcon("C:/Users/Carlos/Desktop/Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/Talento_Humano_Verde.png"))
            self.tabWidget.setTabIcon(1, QIcon("C:/Users/Carlos/Desktop/Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/ventas_verde-render.png"))
        else:
            self.tabWidget.setTabIcon(0, QIcon("C:/Users/Carlos/Desktop/Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/Talento_Humano_Rojo.png"))
            self.tabWidget.setTabIcon(1, QIcon("C:/Users/Carlos/Desktop/Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/ventas_rojo-render.png"))

    def clear_frameVisualizarTablas(self, frame):
        layout = frame.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def show_empleados(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.empleado_gui = EmpleadoGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.empleado_gui)

    def show_bonificaciones(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.bonificacion_gui = BonificacionGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.bonificacion_gui)

    def show_descuentos(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.descuento_gui = DescuentoGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.descuento_gui)

    def show_detalle(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.detalle_gui = DetalleGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.detalle_gui)

    def show_rolpagos(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.rolpagos_gui = RolPagosGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.rolpagos_gui)

    def show_bonxdes(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasTalentoHumano_1)
            self.bonxdes_gui = BonxdesxoGUI()
            self.fVTablasTalentoHumano_1.layout().addWidget(self.bonxdes_gui)

    def show_clientes(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasVentas_1)
            self.cliente_gui = ClienteGUI()
            self.fVTablasVentas_1.layout().addWidget(self.cliente_gui)

    def show_factxdetails(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasVentas_1)
            self.factxdetails_gui = FacturasMasterGUI()
            self.fVTablasVentas_1.layout().addWidget(self.factxdetails_gui)

    def show_productos(self):
        if self.is_logged_in:
            self.clear_frameVisualizarTablas(self.fVTablasVentas_1)
            self.producto_gui = ProductoGUI()
            self.fVTablasVentas_1.layout().addWidget(self.producto_gui)

    def initialize_guis(self, role):
        if role == "admin":
            self.empleado_gui = EmpleadoGUI()
            self.bonificacion_gui = BonificacionGUI()
            self.descuento_gui = DescuentoGUI()
            self.detalle_gui = DetalleGUI()
            self.bonxdes_gui = BonxdesxoGUI()
            self.rolpagos_gui = RolPagosGUI()
            self.cliente_gui = ClienteGUI()
            self.producto_gui = ProductoGUI()
            self.factxdetails_gui = FacturasMasterGUI()
        elif role == "facturacion":
            self.cliente_gui = ClienteGUI()
            self.producto_gui = ProductoGUI()
            self.factxdetails_gui = FacturasMasterGUI()
        elif role == "talento_humano":
            self.empleado_gui = EmpleadoGUI()
            self.bonificacion_gui = BonificacionGUI()
            self.descuento_gui = DescuentoGUI()
            self.detalle_gui = DetalleGUI()
            self.bonxdes_gui = BonxdesxoGUI()
            self.rolpagos_gui = RolPagosGUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.logout)
    window.show()
    sys.exit(app.exec())
