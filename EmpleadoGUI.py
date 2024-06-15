import sys
import functools
import os
import json
import re
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit, QPushButton,
                               QVBoxLayout, QMessageBox, QComboBox, QDateEdit, QTableWidget, QTableWidgetItem,
                               QHeaderView, QFileDialog, QLabel, QHBoxLayout, QGridLayout, QTabWidget)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap
from Empleado import Empleado
from EmpleadoDAO import EmpleadoDAO

PHOTO_DIR = r'C:\Users\Carlos\Desktop\Universidad\4to Semestre\Bases de Datos 1\Unidad 4\Proyectos\Python\EmpleadosExoneracion\Imagenes'
PHOTO_PATH_FILE = os.path.join(PHOTO_DIR, 'photo_paths.json')
DEFAULT_PHOTO = os.path.join(PHOTO_DIR, 'desconocido.jpg')


class EmpleadoGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()

        self.entries = {}
        self.photo_path = None

        self.form_layout = QFormLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()

        self.create_entries()
        self.create_buttons()
        self.create_table()

        self.grid_layout.addLayout(self.form_layout, 0, 0)
        self.grid_layout.addLayout(self.button_layout, 1, 0)
        self.grid_layout.addLayout(self.table_layout, 0, 1, 2, 1)  # Span 2 rows
        self.setLayout(self.grid_layout)

        self.visualizar_empleados()

    def create_entries(self):
        text_fields = [
            ("EmpCodigo", "Código del Empleado", 14),
            ("EmpApellido1", "Apellido del Empleado 1", 30),
            ("EmpApellido2", "Apellido del Empleado 2", 30),
            ("EmpNombre1", "Nombre del Empleado 1", 30),
            ("EmpNombre2", "Nombre del Empleado 2", 30),
            ("EmpEmail", "Email", 30),
            ("EmpDireccion", "Dirección", 30),
            ("EmpSueldo", "Sueldo", 10),
            ("EmpBanco", "Banco", 30),
            ("EmpCuenta", "Cuenta Bancaria", 20),
        ]

        for label, placeholder, char_width in text_fields:
            entry = QLineEdit()
            entry.setPlaceholderText(placeholder)
            entry.setFixedWidth(char_width * 10)
            self.form_layout.addRow(label, entry)
            self.entries[label] = entry

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(100)
        self.form_layout.addRow("EmpFechaNacimiento", self.date_edit)
        self.entries["EmpFechaNacimiento"] = self.date_edit

        self.sexo_combo = QComboBox()
        self.sexo_combo.addItems(["M", "F"])
        self.sexo_combo.setFixedWidth(50)
        self.form_layout.addRow("EmpSexo", self.sexo_combo)
        self.entries["EmpSexo"] = self.sexo_combo

        self.tipo_sangre_combo = QComboBox()
        self.tipo_sangre_combo.addItems(["A+ ", "A- ", "B+ ", "B- ", "O+ ", "O- ", "AB+", "AB-"])
        self.tipo_sangre_combo.setFixedWidth(50)
        self.form_layout.addRow("EmpTipoSangre", self.tipo_sangre_combo)
        self.entries["EmpTipoSangre"] = self.tipo_sangre_combo

        self.status_combo = QComboBox()
        self.status_combo.addItems(["ACT", "INA", "RET"])
        self.status_combo.setFixedWidth(50)
        self.form_layout.addRow("EmpStatus", self.status_combo)
        self.entries["EmpStatus"] = self.status_combo

        self.photo_label = QLabel()
        self.photo_label.setFixedSize(150, 150)
        self.photo_label.setStyleSheet("border: 1px solid black;")
        self.form_layout.addRow("Foto", self.photo_label)

        self.photo_button = QPushButton("Seleccionar Foto")
        self.photo_button.clicked.connect(self.seleccionar_foto)
        self.form_layout.addRow(self.photo_button)

    def create_buttons(self):
        self.add_button = QPushButton("Guardar")
        self.add_button.clicked.connect(self.guardar_empleado)
        self.button_layout.addWidget(self.add_button)

        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.buscar_empleado)
        self.button_layout.addWidget(self.search_button)

        self.new_button = QPushButton("Añadir")
        self.new_button.clicked.connect(self.limpiar_campos)
        self.button_layout.addWidget(self.new_button)

    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(17)
        self.table.setHorizontalHeaderLabels([
            "Código", "Apellido1", "Apellido2", "Nombre1", "Nombre2",
            "Fecha Nacimiento", "Sexo", "Email", "Dirección", "Tipo de Sangre",
            "Sueldo", "Banco", "Cuenta", "Estado", "Foto", "Editar", "Eliminar"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_layout.addWidget(self.table)

    def seleccionar_foto(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Foto", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.photo_label.setPixmap(pixmap.scaled(self.photo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def limpiar_campos(self):
        """
        Limpia todos los campos de entrada.
        """
        self.entries["EmpCodigo"].clear()
        self.entries["EmpApellido1"].clear()
        self.entries["EmpApellido2"].clear()
        self.entries["EmpNombre1"].clear()
        self.entries["EmpNombre2"].clear()
        self.entries["EmpEmail"].clear()
        self.entries["EmpDireccion"].clear()
        self.entries["EmpSueldo"].clear()
        self.entries["EmpBanco"].clear()
        self.entries["EmpCuenta"].clear()
        self.entries["EmpFechaNacimiento"].setDate(QDate.currentDate())
        self.entries["EmpSexo"].setCurrentIndex(0)
        self.entries["EmpTipoSangre"].setCurrentIndex(0)
        self.entries["EmpStatus"].setCurrentIndex(0)
        self.photo_label.clear()
        self.photo_label.setStyleSheet("border: 1px solid black;")
        self.photo_path = None

    def actualizar_campos_empleado(self, empleado):
        """
        Actualiza los campos de entrada con los datos del empleado.
        """
        self.entries["EmpCodigo"].setText(empleado.emp_codigo.rstrip())
        self.entries["EmpApellido1"].setText(empleado.emp_apellido1.rstrip())
        self.entries["EmpApellido2"].setText(empleado.emp_apellido2.rstrip())
        self.entries["EmpNombre1"].setText(empleado.emp_nombre1.rstrip())
        self.entries["EmpNombre2"].setText(empleado.emp_nombre2.rstrip())
        self.entries["EmpEmail"].setText(empleado.emp_email.rstrip())
        self.entries["EmpDireccion"].setText(empleado.emp_direccion.rstrip())
        self.entries["EmpSueldo"].setText(str(empleado.emp_sueldo).rstrip())
        self.entries["EmpBanco"].setText(empleado.emp_banco.rstrip())
        self.entries["EmpCuenta"].setText(empleado.emp_cuenta.rstrip())

        # Convert the date from string to QDate
        fecha_nacimiento_str = empleado.emp_fecha_nacimiento.strftime("%Y-%m-%d")
        self.entries["EmpFechaNacimiento"].setDate(QDate.fromString(fecha_nacimiento_str, "yyyy-MM-dd"))
        self.entries["EmpSexo"].setCurrentText(empleado.emp_sexo)
        self.entries["EmpTipoSangre"].setCurrentText(empleado.emp_tipo_sangre)
        self.entries["EmpStatus"].setCurrentText(empleado.emp_status)

        self.photo_path = self.load_photo_path(empleado.emp_codigo)
        if self.photo_path:
            pixmap = QPixmap(self.photo_path)
            self.photo_label.setPixmap(pixmap.scaled(self.photo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.warning(self, "Advertencia", "No se pudo cargar la foto del empleado. Usando foto predeterminada.")
            self.photo_label.setPixmap(QPixmap(DEFAULT_PHOTO).scaled(self.photo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def guardar_empleado(self):
        emp_codigo = self.entries["EmpCodigo"].text()
        emp_cuenta = self.entries["EmpCuenta"].text()

        # Verificar formato de EmpCodigo
        if not re.match(r"^EMP-\d{3}$", emp_codigo):
            QMessageBox.warning(self, "Advertencia", "El formato del código de empleado debe ser 'EMP-###'")
            return

        # Verificar formato de EmpCuenta
        if not re.match(r"^CUE-\d{1}\d{5}\d{5}\d{5}$", emp_cuenta):
            QMessageBox.warning(self, "Advertencia", "El formato de la cuenta bancaria debe ser 'CUE-################'")
            return

        # Verificar que el sueldo no sea negativo
        emp_sueldo = float(self.entries["EmpSueldo"].text())
        if emp_sueldo < 0:
            QMessageBox.warning(self, "Advertencia", "El sueldo no puede ser negativo")
            return

        empleados = EmpleadoDAO.seleccionar()
        emp_existente = any(emp.emp_codigo == emp_codigo for emp in empleados)
        try:
            empleado = Empleado(
                emp_codigo=self.entries["EmpCodigo"].text(),
                emp_apellido1=self.entries["EmpApellido1"].text(),
                emp_apellido2=self.entries["EmpApellido2"].text(),
                emp_nombre1=self.entries["EmpNombre1"].text(),
                emp_nombre2=self.entries["EmpNombre2"].text(),
                emp_fecha_nacimiento=self.entries["EmpFechaNacimiento"].date().toString("yyyy-MM-dd"),
                emp_sexo=self.entries["EmpSexo"].currentText(),
                emp_email=self.entries["EmpEmail"].text(),
                emp_direccion=self.entries["EmpDireccion"].text(),
                emp_tipo_sangre=self.entries["EmpTipoSangre"].currentText(),
                emp_sueldo=emp_sueldo,
                emp_banco=self.entries["EmpBanco"].text(),
                emp_cuenta=self.entries["EmpCuenta"].text(),
                emp_status=self.entries["EmpStatus"].currentText()
            )

            if emp_existente:
                EmpleadoDAO.actualizar(empleado)
                QMessageBox.information(self, "Información", "Empleado actualizado exitosamente")
            else:
                EmpleadoDAO.insertar(empleado)
                QMessageBox.information(self, "Información", "Empleado agregado exitosamente")

            self.guardar_foto_path(emp_codigo, self.photo_path)
            self.visualizar_empleados()  # Refresh table
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo guardar el Empleado: {e}')

    def buscar_empleado(self):
        emp_codigo = self.entries["EmpCodigo"].text()
        empleado = EmpleadoDAO.buscar(emp_codigo)
        if empleado:
            self.photo_path = self.cargar_foto_path(emp_codigo) or DEFAULT_PHOTO
            self.actualizar_campos_empleado(empleado)
        else:
            QMessageBox.warning(self, "Advertencia", "Empleado no encontrado")

    def editar_empleado(self, row):
        emp_codigo = self.table.item(row, 0).text()
        empleado = EmpleadoDAO.buscar(emp_codigo)
        if empleado:
            self.photo_path = self.cargar_foto_path(emp_codigo) or DEFAULT_PHOTO
            self.actualizar_campos_empleado(empleado)

    def visualizar_empleados(self):
        empleados = EmpleadoDAO.seleccionar()
        self.table.setRowCount(len(empleados))

        for row, empleado in enumerate(empleados):
            self.table.setItem(row, 0, QTableWidgetItem(empleado.emp_codigo))
            self.table.setItem(row, 1, QTableWidgetItem(empleado.emp_apellido1))
            self.table.setItem(row, 2, QTableWidgetItem(empleado.emp_apellido2))
            self.table.setItem(row, 3, QTableWidgetItem(empleado.emp_nombre1))
            self.table.setItem(row, 4, QTableWidgetItem(empleado.emp_nombre2))
            self.table.setItem(row, 5, QTableWidgetItem(str(empleado.emp_fecha_nacimiento)))
            self.table.setItem(row, 6, QTableWidgetItem(empleado.emp_sexo))
            self.table.setItem(row, 7, QTableWidgetItem(empleado.emp_email))
            self.table.setItem(row, 8, QTableWidgetItem(empleado.emp_direccion))
            self.table.setItem(row, 9, QTableWidgetItem(empleado.emp_tipo_sangre))
            self.table.setItem(row, 10, QTableWidgetItem(str(empleado.emp_sueldo)))
            self.table.setItem(row, 11, QTableWidgetItem(empleado.emp_banco))
            self.table.setItem(row, 12, QTableWidgetItem(empleado.emp_cuenta))
            self.table.setItem(row, 13, QTableWidgetItem(empleado.emp_status))

            foto_path = self.cargar_foto_path(empleado.emp_codigo) or DEFAULT_PHOTO
            if not os.path.exists(foto_path):
                foto_path = DEFAULT_PHOTO

            label = QLabel()
            pixmap = QPixmap(foto_path)
            label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.table.setCellWidget(row, 14, label)

            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(functools.partial(self.editar_empleado, row))
            self.table.setCellWidget(row, 15, edit_button)

            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(functools.partial(self.eliminar_empleado_desde_tabla, row))
            self.table.setCellWidget(row, 16, delete_button)

    def eliminar_empleado_desde_tabla(self, row):
        emp_codigo = self.table.item(row, 0).text()
        empleado = Empleado(emp_codigo=emp_codigo)
        EmpleadoDAO.eliminar(empleado)
        QMessageBox.information(self, "Información", "Empleado eliminado exitosamente")
        self.eliminar_foto_path(emp_codigo)
        self.visualizar_empleados()  # Refresh table

    def guardar_foto_path(self, emp_codigo, photo_path):
        if not photo_path:
            return
        photo_data = self.load_photo_data()
        photo_data[emp_codigo] = photo_path
        self.save_photo_data(photo_data)

    def cargar_foto_path(self, emp_codigo):
        photo_data = self.load_photo_data()
        return photo_data.get(emp_codigo, None)

    def eliminar_foto_path(self, emp_codigo):
        photo_data = self.load_photo_data()
        if emp_codigo in photo_data:
            del photo_data[emp_codigo]
            self.save_photo_data(photo_data)

    def load_photo_data(self):
        if not os.path.exists(PHOTO_PATH_FILE):
            return {}
        with open(PHOTO_PATH_FILE, 'r') as file:
            return json.load(file)

    def save_photo_data(self, data):
        with open(PHOTO_PATH_FILE, 'w') as file:
            json.dump(data, file)

    def load_photo_path(self, emp_codigo):
        photo_path = self.cargar_foto_path(emp_codigo)
        if photo_path and os.path.exists(photo_path) and photo_path != 'NULL':
            return photo_path
        return DEFAULT_PHOTO


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = EmpleadoGUI()
    gui.show()
    sys.exit(app.exec())