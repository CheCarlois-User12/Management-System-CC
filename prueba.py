import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import QLocale
from NominaMasterForm import NominaMasterForm
from NominasWindow import NominasWindow
from EmpleadoDAO import EmpleadoDAO
from DescuentoDAO import DescuentoDAO
from BonificacionDAO import BonificacionDAO
from NominaDAO import NominaDAO
from Nomina import Nomina
from BXNDAO import BXNDAO
from DXNDAO import DXNDAO


class NominaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Nóminas")
        self.setGeometry(100, 100, 1280, 720)

        self.form = NominaMasterForm()
        self.form.setupUi(self)

        self.entries = {}
        self.create_entries()
        self.create_buttons()
        self.create_table()

        self.populate_emp_combo_box()
        self.populate_desbon_combo_box()
        self.populate_year_month_combo_box()

        self.form.boton_Confirmar_DesBon.clicked.connect(self.confirmar_desbon)
        self.form.boton_GenerarNom_Nom.clicked.connect(self.guardar_nomina)
        self.form.boton_VisualizarNom_Nom.clicked.connect(self.abrir_ventana_nominas)
        self.form.boton_CancelarNom_Nom.clicked.connect(self.cancelar_nomina)
        self.form.boton_BuscarCodigo_Emp.clicked.connect(self.buscar_empleado)
        self.form.boton_Buscar_DesBon.clicked.connect(self.buscar_desbon)

        self.nomina_desc_bon = []

    def create_entries(self):
        self.entries["empCodigo"] = self.form.cBox_empCodigo_Emp
        self.entries["empCargo"] = self.form.lEdit_empCargo_Nom
        self.entries["empNombre"] = self.form.lEdit_empNombre_Nom
        self.entries["nomFechaInicial"] = self.form.dateEdit_nomFechaInicial_Nom
        self.entries["nomFechaFinal"] = self.form.dateEdit_nomFechaFinal_Nom
        self.entries["nomTotalHoras"] = self.form.lEdit_nomTotalHoras_Nom
        self.entries["nomCodigo"] = self.form.lEdit_nomCodigo_Nom
        self.entries["nomAnio"] = self.form.cBox_nomAnio_Nom
        self.entries["nomMes"] = self.form.cBox_nomMes_Nom
        self.entries["nomSubTotal"] = self.form.lEdit_nomSubTotal_Nom
        self.entries["nomTotalBon"] = self.form.lEdit_nomTotalBon_Nom
        self.entries["nomTotalDes"] = self.form.lEdit_nomTotalDes_Nom
        self.entries["nomTotal"] = self.form.lEdit_nomTotal_Nom
        self.entries["desBonCodigo"] = self.form.cBox_desBonCodigo_DesBon
        self.entries["desBonDescripcion"] = self.form.lEdit_desBonDescripcion_DesBon
        self.entries["desBonValor"] = self.form.lEdit_desBonValor_DesBon
        self.entries["empIdentificacion"] = self.form.lEdit_empIdentificacion_Emp  # Corregido

    def create_buttons(self):
        self.form.boton_Confirmar_DesBon.clicked.connect(self.confirmar_desbon)
        self.form.boton_GenerarNom_Nom.clicked.connect(self.guardar_nomina)
        self.form.boton_VisualizarNom_Nom.clicked.connect(self.abrir_ventana_nominas)
        self.form.boton_CancelarNom_Nom.clicked.connect(self.cancelar_nomina)
        self.form.boton_BuscarCodigo_Emp.clicked.connect(self.buscar_empleado)
        self.form.boton_Buscar_DesBon.clicked.connect(self.buscar_desbon)

    def create_table(self):
        self.table = QTableWidget(self.form.frame_tabla_1_1_Nom)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Código", "Descripción", "Valor", "Tipo"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setGeometry(10, 10, 800, 300)

    def populate_emp_combo_box(self):
        empleados = EmpleadoDAO.seleccionar()
        self.entries["empCodigo"].clear()
        for emp in empleados:
            self.entries["empCodigo"].addItem(emp.emp_codigo)

    def populate_desbon_combo_box(self):
        bonificaciones = BonificacionDAO.seleccionar()
        descuentos = DescuentoDAO.seleccionar()
        self.entries["desBonCodigo"].clear()
        for bon in bonificaciones:
            self.entries["desBonCodigo"].addItem(f"Bonificación - {bon.bon_codigo}")
        for des in descuentos:
            self.entries["desBonCodigo"].addItem(f"Descuento - {des.des_codigo}")

    def populate_year_month_combo_box(self):
        years = [str(year) for year in range(2000, 2051)]
        self.entries["nomAnio"].addItems(years)

        months = [QLocale().monthName(i) for i in range(1, 13)]
        self.entries["nomMes"].addItems(months)

    def month_name_to_number(self, month_name):
        month_mapping = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        return month_mapping.get(month_name, "00")  # Default to "00" if not found

    def buscar_empleado(self):
        emp_codigo = self.entries["empCodigo"].currentText()
        empleado = EmpleadoDAO.buscar(emp_codigo)
        if empleado:
            self.entries["empCargo"].setText(empleado.emp_cargo)
            self.entries["empNombre"].setText(f"{empleado.emp_nombre1} {empleado.emp_apellido1}")
            self.entries["empIdentificacion"].setText(empleado.emp_identificacion)
            self.entries["nomCodigo"].clear()  # Clear the nomCodigo entry

    def buscar_desbon(self):
        desbon_codigo = self.entries["desBonCodigo"].currentText()
        tipo, codigo = desbon_codigo.split(" - ")
        if tipo == "Bonificación":
            bonificacion = BonificacionDAO.buscar(codigo)
            if bonificacion:
                self.entries["desBonDescripcion"].setText(bonificacion.bon_descripcion)
                self.entries["desBonValor"].setText(str(bonificacion.bon_valor))
        else:
            descuento = DescuentoDAO.buscar(codigo)
            if descuento:
                self.entries["desBonDescripcion"].setText(descuento.des_descripcion)
                self.entries["desBonValor"].setText(str(descuento.des_valor))

        self.entries["desBonDescripcion"].setReadOnly(True)
        self.entries["desBonValor"].setReadOnly(True)

    def confirmar_desbon(self):
        desbon_codigo = self.entries["desBonCodigo"].currentText()
        tipo, codigo = desbon_codigo.split(" - ")
        descripcion = self.entries["desBonDescripcion"].text()
        valor = float(self.entries["desBonValor"].text())
        if (codigo, descripcion, valor, tipo) not in self.nomina_desc_bon:
            self.nomina_desc_bon.append((codigo, descripcion, valor, tipo))
        self.update_desbon_table()

    def update_desbon_table(self):
        self.table.setRowCount(len(self.nomina_desc_bon))
        for row, (codigo, descripcion, valor, tipo) in enumerate(self.nomina_desc_bon):
            self.table.setItem(row, 0, QTableWidgetItem(codigo))
            self.table.setItem(row, 1, QTableWidgetItem(descripcion))
            self.table.setItem(row, 2, QTableWidgetItem(str(valor)))
            self.table.setItem(row, 3, QTableWidgetItem(tipo))
        self.calculate_totals()

    def calculate_totals(self):
        subtotal = 0
        total_bon = 0
        total_des = 0
        for _, _, valor, tipo in self.nomina_desc_bon:
            if tipo == "Bonificación":
                total_bon += valor
            else:
                total_des += valor
        subtotal = total_bon - total_des
        self.entries["nomSubTotal"].setText(str(subtotal))
        self.entries["nomTotalBon"].setText(str(total_bon))
        self.entries["nomTotalDes"].setText(str(total_des))
        self.entries["nomTotal"].setText(str(subtotal))

    def guardar_nomina(self):
        nom_mes = self.month_name_to_number(self.entries["nomMes"].currentText())
        nomina = Nomina(
            nom_codigo=self.entries["nomCodigo"].text(),
            emp_codigo=self.entries["empCodigo"].currentText(),
            emp_cargo=self.entries["empCargo"].text(),
            nom_nombre_empleado=self.entries["empNombre"].text(),
            nom_anio=self.entries["nomAnio"].currentText(),
            nom_mes=nom_mes,
            nom_fecha_inicial=self.entries["nomFechaInicial"].date().toString("yyyy-MM-dd"),
            nom_fecha_final=self.entries["nomFechaFinal"].date().toString("yyyy-MM-dd"),
            nom_total_horas=int(self.entries["nomTotalHoras"].text()),
            nom_subtotal=float(self.entries["nomSubTotal"].text()),
            nom_total_bonificaciones=float(self.entries["nomTotalBon"].text()),
            nom_total_descuentos=float(self.entries["nomTotalDes"].text()),
            nom_total=float(self.entries["nomTotal"].text()),
            nom_status="ACT"
        )
        descuentos = [item for item in self.nomina_desc_bon if item[3] == "Descuento"]
        bonificaciones = [item for item in self.nomina_desc_bon if item[3] == "Bonificación"]

        try:
            NominaDAO.insertar(nomina, descuentos, bonificaciones)
            QMessageBox.information(self, "Información", "Nómina generada exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al insertar la nómina: {str(e)}")

    def abrir_ventana_nominas(self):
        self.nominas_window = NominasWindow()
        self.nominas_window.show()

    def cancelar_nomina(self):
        nom_codigo = self.entries["nomCodigo"].text()
        try:
            NominaDAO.eliminar_logico(nom_codigo)
            QMessageBox.information(self, "Información", "Nómina cancelada exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cancelar la nómina: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = NominaGUI()
    gui.show()
    sys.exit(app.exec())
