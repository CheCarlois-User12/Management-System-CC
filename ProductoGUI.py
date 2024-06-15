import sys
import os
import json
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QComboBox, QFileDialog, QFrame, QAbstractItemView)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from Producto import Producto
from ProductoDAO import ProductoDAO

PHOTO_DIR = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes_Productos'
PHOTO_PATH_FILE = os.path.join(PHOTO_DIR, 'photo_paths_productos.json')
DEFAULT_PHOTO = os.path.join(PHOTO_DIR, 'desconocido.jpg')
PENCIL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\pencil.png'
CANCEL_ICON_PATH = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes\iconos\cancel.png'

class ProductoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")
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
            ("PRODCODIGO", "Código"),
            ("PRODDESCRIPCION", "Descripción"),
            ("PRODSALDOINICIAL", "Saldo Inicial"),
            ("PRODINGRESOS", "Ingresos"),
            ("PRODEGRESOS", "Egresos"),
            ("PRODAJUSTES", "Ajustes"),
            ("PRODSALDOFINAL", "Saldo Final"),
            ("PRODCOSTOXUNIDAD", "Costo por Unidad")
        ]

        for label, placeholder in fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

        self.entries["PRODUNIDADMEDIDA"] = QComboBox()
        self.entries["PRODUNIDADMEDIDA"].addItems(["kg", "gr", "lt", "ml", "un", "m", "cm", "mm"])
        self.form_layout.addRow("Unidad de Medida", self.entries["PRODUNIDADMEDIDA"])

        self.entries["PRODSTATUS"] = QComboBox()
        self.entries["PRODSTATUS"].addItems(["DES", "EXP", "RET", "SUS", "ESC", "ACT"])
        self.form_layout.addRow("Estado", self.entries["PRODSTATUS"])

        self.labelFoto = QLabel("No hay foto seleccionada")
        self.btnSubirFoto = QPushButton("Subir Foto")
        self.btnSubirFoto.clicked.connect(self.subir_foto)
        self.form_layout.addRow("Foto", self.labelFoto)
        self.form_layout.addRow(self.btnSubirFoto)

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

    def insert_action(self):
        try:
            producto = Producto(
                self.entries["PRODCODIGO"].text(),
                self.entries["PRODDESCRIPCION"].text(),
                self.entries["PRODUNIDADMEDIDA"].currentText(),
                float(self.entries["PRODSALDOINICIAL"].text()),
                float(self.entries["PRODINGRESOS"].text()),
                float(self.entries["PRODEGRESOS"].text()),
                float(self.entries["PRODAJUSTES"].text()),
                float(self.entries["PRODSALDOFINAL"].text()),
                float(self.entries["PRODCOSTOXUNIDAD"].text()),
                self.entries["PRODSTATUS"].currentText()
            )
            ProductoDAO.insertar(producto)
            self.guardar_foto_path(producto.prod_codigo, self.photo_path)
            QMessageBox.information(self, "Información", "Registro guardado exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el registro: {e}")

    def update_action(self):
        try:
            producto = Producto(
                self.entries["PRODCODIGO"].text(),
                self.entries["PRODDESCRIPCION"].text(),
                self.entries["PRODUNIDADMEDIDA"].currentText(),
                float(self.entries["PRODSALDOINICIAL"].text()),
                float(self.entries["PRODINGRESOS"].text()),
                float(self.entries["PRODEGRESOS"].text()),
                float(self.entries["PRODAJUSTES"].text()),
                float(self.entries["PRODSALDOFINAL"].text()),
                float(self.entries["PRODCOSTOXUNIDAD"].text()),
                self.entries["PRODSTATUS"].currentText()
            )
            ProductoDAO.actualizar(producto)
            self.guardar_foto_path(producto.prod_codigo, self.photo_path)
            QMessageBox.information(self, "Información", "Registro actualizado exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el registro: {e}")

    def delete_action(self):
        try:
            producto = Producto(prod_codigo=self.entries["PRODCODIGO"].text())
            ProductoDAO.eliminar(producto)
            self.eliminar_foto_path(producto.prod_codigo)
            QMessageBox.information(self, "Información", "Registro eliminado exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el registro: {e}")

    def read_action(self):
        try:
            producto = ProductoDAO.buscar(self.entries["PRODCODIGO"].text())
            if producto:
                self.entries["PRODDESCRIPCION"].setText(producto.prod_descripcion)
                self.entries["PRODUNIDADMEDIDA"].setCurrentText(producto.prod_unidad_medida)
                self.entries["PRODSALDOINICIAL"].setText(str(producto.prod_saldo_inicial))
                self.entries["PRODINGRESOS"].setText(str(producto.prod_ingresos))
                self.entries["PRODEGRESOS"].setText(str(producto.prod_egresos))
                self.entries["PRODAJUSTES"].setText(str(producto.prod_ajustes))
                self.entries["PRODSALDOFINAL"].setText(str(producto.prod_saldo_final))
                self.entries["PRODCOSTOXUNIDAD"].setText(str(producto.prod_costo_x_unidad))
                self.entries["PRODSTATUS"].setCurrentText(producto.prod_status)
                self.photo_path = self.cargar_foto_path(self.entries["PRODCODIGO"].text())
                if self.photo_path:
                    pixmap = QPixmap(self.photo_path)
                    self.labelFoto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    self.labelFoto.setPixmap(QPixmap(DEFAULT_PHOTO).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                QMessageBox.information(self, "Información", "Producto encontrado")
            else:
                QMessageBox.warning(self, "Advertencia", "Producto no encontrado")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo leer el registro: {e}")

    def mostrar_tabla(self):
        self.table_window = TablaProductos(self)
        self.table_window.setWindowModality(Qt.NonModal)
        self.table_window.setWindowFlags(Qt.Window)  # Ensure the table window is a top-level window
        self.table_window.show()

    def guardar_foto_path(self, prod_codigo, photo_path):
        if not photo_path:
            return
        photo_data = self.load_photo_data()
        photo_data[prod_codigo] = photo_path
        self.save_photo_data(photo_data)

    def cargar_foto_path(self, prod_codigo):
        photo_data = self.load_photo_data()
        return photo_data.get(prod_codigo, None)

    def eliminar_foto_path(self, prod_codigo):
        photo_data = self.load_photo_data()
        if prod_codigo in photo_data:
            del photo_data[prod_codigo]
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

class TablaProductos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tabla de Productos")
        self.setGeometry(100, 100, 1000, 600)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(["Modificar", "Código", "Descripción", "Unidad de Medida", "Saldo Inicial", "Ingresos", "Egresos", "Ajustes", "Saldo Final", "Costo por Unidad", "Imagen", "Eliminar"])

        # Configurar las cabeceras
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #1b1717; color: white; padding: 4px; border: 1px solid #6c6c6c; }")

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.cargar_datos()

    def cargar_datos(self):
        records = ProductoDAO.seleccionar()
        self.table.setRowCount(len(records))

        for row, record in enumerate(records):
            modify_button = QPushButton()
            modify_button.setIcon(QIcon(PENCIL_ICON_PATH))
            modify_button.clicked.connect(lambda _, r=record: self.modificar_producto(r))
            self.table.setCellWidget(row, 0, modify_button)

            self.table.setItem(row, 1, QTableWidgetItem(record.prod_codigo))
            self.table.setItem(row, 2, QTableWidgetItem(record.prod_descripcion))
            self.table.setItem(row, 3, QTableWidgetItem(record.prod_unidad_medida))
            self.table.setItem(row, 4, QTableWidgetItem(str(record.prod_saldo_inicial)))
            self.table.setItem(row, 5, QTableWidgetItem(str(record.prod_ingresos)))
            self.table.setItem(row, 6, QTableWidgetItem(str(record.prod_egresos)))
            self.table.setItem(row, 7, QTableWidgetItem(str(record.prod_ajustes)))
            self.table.setItem(row, 8, QTableWidgetItem(str(record.prod_saldo_final)))
            self.table.setItem(row, 9, QTableWidgetItem(str(record.prod_costo_x_unidad)))

            photo_path = self.cargar_foto_path(record.prod_codigo)
            if photo_path:
                photo_label = QLabel()
                pixmap = QPixmap(photo_path)
                photo_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                self.table.setCellWidget(row, 10, photo_label)
            else:
                self.table.setItem(row, 10, QTableWidgetItem("Sin imagen"))

            delete_button = QPushButton()
            delete_button.setIcon(QIcon(CANCEL_ICON_PATH))
            delete_button.clicked.connect(lambda _, r=record: self.eliminar_producto(r))
            self.table.setCellWidget(row, 11, delete_button)

    def modificar_producto(self, producto):
        parent_gui = self.parent()
        parent_gui.entries["PRODCODIGO"].setText(producto.prod_codigo)
        parent_gui.entries["PRODDESCRIPCION"].setText(producto.prod_descripcion)
        parent_gui.entries["PRODUNIDADMEDIDA"].setCurrentText(producto.prod_unidad_medida)
        parent_gui.entries["PRODSALDOINICIAL"].setText(str(producto.prod_saldo_inicial))
        parent_gui.entries["PRODINGRESOS"].setText(str(producto.prod_ingresos))
        parent_gui.entries["PRODEGRESOS"].setText(str(producto.prod_egresos))
        parent_gui.entries["PRODAJUSTES"].setText(str(producto.prod_ajustes))
        parent_gui.entries["PRODSALDOFINAL"].setText(str(producto.prod_saldo_final))
        parent_gui.entries["PRODCOSTOXUNIDAD"].setText(str(producto.prod_costo_x_unidad))
        parent_gui.entries["PRODSTATUS"].setCurrentText(producto.prod_status)
        parent_gui.photo_path = self.cargar_foto_path(producto.prod_codigo)
        if parent_gui.photo_path:
            pixmap = QPixmap(parent_gui.photo_path)
            parent_gui.labelFoto.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            parent_gui.labelFoto.setPixmap(QPixmap(DEFAULT_PHOTO).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.close()

    def eliminar_producto(self, producto):
        confirm = QMessageBox.question(self, "Confirmar eliminación", f"¿Estás seguro de eliminar el producto {producto.prod_codigo}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            ProductoDAO.eliminar(producto)
            self.eliminar_foto_path(producto.prod_codigo)
            self.cargar_datos()

    def cargar_foto_path(self, prod_codigo):
        photo_data = self.load_photo_data()
        return photo_data.get(prod_codigo, None)

    def eliminar_foto_path(self, prod_codigo):
        photo_data = self.load_photo_data()
        if prod_codigo in photo_data:
            del photo_data[prod_codigo]
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
    gui = ProductoGUI()
    gui.show()
    sys.exit(app.exec())
