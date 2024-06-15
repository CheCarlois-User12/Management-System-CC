import sys
import os
import json
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QComboBox, QFileDialog, QFrame, QAbstractItemView)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from Cliente import Cliente
from ClienteDAO import ClienteDAO

PHOTO_DIR = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes_Clientes'
PHOTO_PATH_FILE = os.path.join(PHOTO_DIR, 'photo_paths_clientes.json')
DEFAULT_PHOTO = os.path.join(PHOTO_DIR, 'desconocido.jpg')
PENCIL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\pencil.png'
CANCEL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\cancel.png'

class ClienteGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes")
        self.setGeometry(100, 100, 800, 700)

        self.main_layout = QHBoxLayout()

        self.form_frame = QFrame()
        self.button_frame = QFrame()

        self.form_layout = QFormLayout()
        self.button_layout = QVBoxLayout()

        self.entries = {}
        self.create_entries()
        self.create_buttons()

        self.form_frame.setLayout(self.form_layout)
        self.button_frame.setLayout(self.button_layout)

        self.main_layout.addWidget(self.form_frame)
        self.main_layout.addWidget(self.button_frame, alignment=Qt.AlignTop)

        self.setLayout(self.main_layout)

        self.photo_path = None

    def create_entries(self):
        fields = [
            ("CLICODIGO", "Código"),
            ("CLINOMBRE", "Nombre"),
            ("CLIIDENTIFICACION", "Identificación"),
            ("CLIDIRECCION", "Dirección"),
            ("CLITELEFONO", "Teléfono"),
            ("CLICELULAR", "Celular"),
            ("CLIEMAIL", "Email")
        ]

        for label, placeholder in fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

        self.entries["CLITIPO"] = QComboBox()
        self.entries["CLITIPO"].addItems(["NAT", "JUR"])
        self.form_layout.addRow("Tipo", self.entries["CLITIPO"])

        self.entries["CLISTATUS"] = QComboBox()
        self.entries["CLISTATUS"].addItems(["ACT", "INA"])
        self.form_layout.addRow("Estado", self.entries["CLISTATUS"])

        self.labelFoto = QLabel("No hay foto seleccionada")
        self.btnSubirFoto = QPushButton("Subir Foto")
        self.btnSubirFoto.clicked.connect(self.subir_foto)
        self.btnCancelarFoto = QPushButton("Cancelar Foto")
        self.btnCancelarFoto.clicked.connect(self.cancelar_foto)
        self.form_layout.addRow("Foto", self.labelFoto)
        self.form_layout.addRow(self.btnSubirFoto)
        self.form_layout.addRow(self.btnCancelarFoto)

    def create_buttons(self):
        self.btnInsertar = QPushButton("Guardar")
        self.btnInsertar.clicked.connect(self.insert_action)
        self.button_layout.addWidget(self.btnInsertar)

        self.btnActualizar = QPushButton("Actualizar")
        self.btnActualizar.clicked.connect(self.update_action)
        self.button_layout.addWidget(self.btnActualizar)

        self.btnEliminar = QPushButton("Eliminar")
        self.btnEliminar.clicked.connect(self.delete_action)
        self.button_layout.addWidget(self.btnEliminar)

        self.btnSeleccionar = QPushButton("Buscar")
        self.btnSeleccionar.clicked.connect(self.read_action)
        self.button_layout.addWidget(self.btnSeleccionar)

        self.btnMostrarTabla = QPushButton("Vista amplia")
        self.btnMostrarTabla.clicked.connect(self.mostrar_tabla)
        self.button_layout.addWidget(self.btnMostrarTabla)

        self.button_layout.addStretch()

    def subir_foto(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Foto", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.labelFoto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def cancelar_foto(self):
        self.photo_path = None
        self.labelFoto.setText("No hay foto seleccionada")

    def insert_action(self):
        try:
            cliente = Cliente(
                self.entries["CLICODIGO"].text(),
                self.entries["CLINOMBRE"].text(),
                self.entries["CLIIDENTIFICACION"].text(),
                self.entries["CLIDIRECCION"].text(),
                self.entries["CLITELEFONO"].text(),
                self.entries["CLICELULAR"].text(),
                self.entries["CLIEMAIL"].text(),
                self.entries["CLITIPO"].currentText(),
                self.entries["CLISTATUS"].currentText()
            )
            ClienteDAO.insertar(cliente)
            self.guardar_foto_path(cliente.cli_codigo, self.photo_path)
            QMessageBox.information(self, "Información", "Registro guardado exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el registro: {e}")

    def update_action(self):
        try:
            cliente = Cliente(
                self.entries["CLICODIGO"].text(),
                self.entries["CLINOMBRE"].text(),
                self.entries["CLIIDENTIFICACION"].text(),
                self.entries["CLIDIRECCION"].text(),
                self.entries["CLITELEFONO"].text(),
                self.entries["CLICELULAR"].text(),
                self.entries["CLIEMAIL"].text(),
                self.entries["CLITIPO"].currentText(),
                self.entries["CLISTATUS"].currentText()
            )
            ClienteDAO.actualizar(cliente)
            self.guardar_foto_path(cliente.cli_codigo, self.photo_path)
            QMessageBox.information(self, "Información", "Registro actualizado exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el registro: {e}")

    def delete_action(self):
        try:
            cli_codigo = self.entries["CLICODIGO"].text()
            ClienteDAO.eliminar(cli_codigo)
            self.eliminar_foto_path(cli_codigo)
            QMessageBox.information(self, "Información", "Registro eliminado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el registro: {e}")

    def read_action(self):
        try:
            cliente = ClienteDAO.buscar(self.entries["CLICODIGO"].text())
            if cliente:
                self.entries["CLINOMBRE"].setText(cliente.cli_nombre)
                self.entries["CLIIDENTIFICACION"].setText(cliente.cli_identificacion)
                self.entries["CLIDIRECCION"].setText(cliente.cli_direccion)
                self.entries["CLITELEFONO"].setText(cliente.cli_telefono)
                self.entries["CLICELULAR"].setText(cliente.cli_celular)
                self.entries["CLIEMAIL"].setText(cliente.cli_email)
                self.entries["CLITIPO"].setCurrentText(cliente.cli_tipo)
                self.entries["CLISTATUS"].setCurrentText(cliente.cli_status)
                self.photo_path = self.cargar_foto_path(self.entries["CLICODIGO"].text())
                if self.photo_path:
                    pixmap = QPixmap(self.photo_path)
                    self.labelFoto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    self.labelFoto.setPixmap(QPixmap(DEFAULT_PHOTO).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                QMessageBox.information(self, "Información", "Cliente encontrado")
            else:
                QMessageBox.warning(self, "Advertencia", "Cliente no encontrado")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo leer el registro: {e}")

    def mostrar_tabla(self):
        self.table_window = TablaClientes(self)
        self.table_window.setWindowModality(Qt.NonModal)
        self.table_window.setWindowFlags(Qt.Window)  # Ensure the table window is a top-level window
        self.table_window.show()

    def guardar_foto_path(self, cli_codigo, photo_path):
        if not photo_path:
            return
        photo_data = self.load_photo_data()
        photo_data[cli_codigo] = photo_path
        self.save_photo_data(photo_data)

    def cargar_foto_path(self, cli_codigo):
        photo_data = self.load_photo_data()
        return photo_data.get(cli_codigo, None)

    def eliminar_foto_path(self, cli_codigo):
        photo_data = self.load_photo_data()
        if cli_codigo in photo_data:
            del photo_data[cli_codigo]
            self.save_photo_data(photo_data)

    def load_photo_data(self):
        if not os.path.exists(PHOTO_PATH_FILE):
            return {}
        with open(PHOTO_PATH_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}

    def save_photo_data(self, data):
        with open(PHOTO_PATH_FILE, 'w') as file:
            json.dump(data, file)

    def limpiar_campos(self):
        for entry in self.entries.values():
            if isinstance(entry, QLineEdit):
                entry.clear()
            elif isinstance(entry, QComboBox):
                entry.setCurrentIndex(0)
        self.labelFoto.setText("No hay foto seleccionada")
        self.photo_path = None

class TablaClientes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tabla de Clientes")
        self.setGeometry(100, 100, 1000, 600)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(["Modificar", "Código", "Nombre", "Identificación", "Dirección", "Teléfono", "Celular", "Email", "Tipo", "Estado", "Imagen", "Eliminar"])

        # Configurar las cabeceras
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #1b1717; color: white; padding: 4px; border: 1px solid #6c6c6c; }")

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.cargar_datos()

    def cargar_datos(self):
        records = ClienteDAO.seleccionar()
        self.table.setRowCount(len(records))

        for row, record in enumerate(records):
            modify_button = QPushButton()
            modify_button.setIcon(QIcon(PENCIL_ICON_PATH))
            modify_button.clicked.connect(lambda _, r=record: self.modificar_cliente(r))
            self.table.setCellWidget(row, 0, modify_button)

            self.table.setItem(row, 1, QTableWidgetItem(record.cli_codigo))
            self.table.setItem(row, 2, QTableWidgetItem(record.cli_nombre))
            self.table.setItem(row, 3, QTableWidgetItem(record.cli_identificacion))
            self.table.setItem(row, 4, QTableWidgetItem(record.cli_direccion))
            self.table.setItem(row, 5, QTableWidgetItem(record.cli_telefono))
            self.table.setItem(row, 6, QTableWidgetItem(record.cli_celular))
            self.table.setItem(row, 7, QTableWidgetItem(record.cli_email))
            self.table.setItem(row, 8, QTableWidgetItem(record.cli_tipo))
            self.table.setItem(row, 9, QTableWidgetItem(record.cli_status))

            photo_path = self.cargar_foto_path(record.cli_codigo)
            if photo_path:
                photo_label = QLabel()
                pixmap = QPixmap(photo_path)
                photo_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                self.table.setCellWidget(row, 10, photo_label)
            else:
                self.table.setItem(row, 10, QTableWidgetItem("Sin imagen"))

            delete_button = QPushButton()
            delete_button.setIcon(QIcon(CANCEL_ICON_PATH))
            delete_button.clicked.connect(lambda _, r=record: self.eliminar_cliente(r))
            self.table.setCellWidget(row, 11, delete_button)

    def modificar_cliente(self, cliente):
        parent_gui = self.parent()
        parent_gui.entries["CLICODIGO"].setText(cliente.cli_codigo)
        parent_gui.entries["CLINOMBRE"].setText(cliente.cli_nombre)
        parent_gui.entries["CLIIDENTIFICACION"].setText(cliente.cli_identificacion)
        parent_gui.entries["CLIDIRECCION"].setText(cliente.cli_direccion)
        parent_gui.entries["CLITELEFONO"].setText(cliente.cli_telefono)
        parent_gui.entries["CLICELULAR"].setText(cliente.cli_celular)
        parent_gui.entries["CLIEMAIL"].setText(cliente.cli_email)
        parent_gui.entries["CLITIPO"].setCurrentText(cliente.cli_tipo)
        parent_gui.entries["CLISTATUS"].setCurrentText(cliente.cli_status)
        parent_gui.photo_path = self.cargar_foto_path(cliente.cli_codigo)
        if parent_gui.photo_path:
            pixmap = QPixmap(parent_gui.photo_path)
            parent_gui.labelFoto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            parent_gui.labelFoto.setPixmap(QPixmap(DEFAULT_PHOTO).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.close()

    def eliminar_cliente(self, cliente):
        confirm = QMessageBox.question(self, "Confirmar eliminación", f"¿Estás seguro de eliminar el cliente {cliente.cli_codigo}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                ClienteDAO.eliminar(cliente.cli_codigo)
                self.eliminar_foto_path(cliente.cli_codigo)
                self.cargar_datos()
                QMessageBox.information(self, "Información", "Registro eliminado exitosamente")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el registro: {e}")

    def cargar_foto_path(self, cli_codigo):
        photo_data = self.load_photo_data()
        return photo_data.get(cli_codigo, None)

    def eliminar_foto_path(self, cli_codigo):
        photo_data = self.load_photo_data()
        if cli_codigo in photo_data:
            del photo_data[cli_codigo]
            self.save_photo_data(photo_data)

    def load_photo_data(self):
        if not os.path.exists(PHOTO_PATH_FILE):
            return {}
        with open(PHOTO_PATH_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}

    def save_photo_data(self, data):
        with open(PHOTO_PATH_FILE, 'w') as file:
            json.dump(data, file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ClienteGUI()
    gui.show()
    sys.exit(app.exec())
