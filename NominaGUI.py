import sys
from datetime import datetime

from PySide6.QtCore import QLocale, QDate, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QWidget
)

from BonificacionDAO import BonificacionDAO
from DescuentoDAO import DescuentoDAO
from EmpleadoDAO import EmpleadoDAO
from LiquidacionGUI import LiquidacionGUI
from Nomina import Nomina
from NominaDAO import NominaDAO
from NominaMasterForm import NominaMasterForm
from NominasWindow import NominasWindow
from Bonificacion_Nom import Bonificacion_Nom

ICON_DELETE_PATH = r"C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\Imagenes\iconos\cancel.png"


class Descuento_Nom:
    def __init__(self, nom_codigo=None, des_codigo=None, des_descripcion=None, des_valor=None, des_status='ACT'):
        self.nom_codigo = nom_codigo
        self.des_codigo = des_codigo
        self.des_descripcion = des_descripcion
        self.des_valor = des_valor
        self.des_status = des_status

    @property
    def codigo(self):
        return self.des_codigo

    @property
    def descripcion(self):
        return self.des_descripcion

    @property
    def valor(self):
        return self.des_valor

    @property
    def tipo(self):
        return "Descuento"

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

        self.nomina_desc_bon = []

        # Connect the total hours edit to recalculate subtotal
        self.entries["nomTotalHoras"].textChanged.connect(self.calculate_subtotal)
        self.recommend_nom_codigo()

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
        self.entries["empIdentificacion"] = self.form.lEdit_empIdentificacion_Emp

        # Set non-editable entries
        self.entries["nomSubTotal"].setReadOnly(True)
        self.entries["nomTotalBon"].setReadOnly(True)
        self.entries["nomTotalDes"].setReadOnly(True)
        self.entries["nomTotal"].setReadOnly(True)
        self.entries["desBonDescripcion"].setReadOnly(True)
        self.entries["desBonValor"].setReadOnly(True)

    def create_buttons(self):
        self.form.boton_Confirmar_DesBon.clicked.connect(self.confirmar_desbon)
        self.form.boton_GenerarNom_Nom.clicked.connect(self.guardar_nomina)
        self.form.boton_VisualizarNom_Nom.clicked.connect(self.abrir_ventana_nominas)
        self.form.boton_CancelarNom_Nom.clicked.connect(self.cancelar_nomina)
        self.form.boton_BuscarCodigo_Emp.clicked.connect(self.buscar_empleado)
        self.form.boton_Buscar_DesBon.clicked.connect(self.buscar_desbon)
        self.form.boton_VisualizarLiq_Liq.clicked.connect(self.abrir_ventana_liquidaciones)

    def abrir_ventana_liquidaciones(self):
        self.liquidacion_window = LiquidacionGUI()
        self.liquidacion_window.show()
    def create_table(self):
        self.table = QTableWidget(self.form.frame_tabla_1_1_Nom)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Código", "Descripción", "Valor", "Tipo", "Eliminar"])
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

    def buscar_empleado(self):
        emp_codigo = self.entries["empCodigo"].currentText()
        empleado = EmpleadoDAO.buscar(emp_codigo)
        if empleado:
            self.entries["empCargo"].setText(empleado.emp_cargo)
            self.entries["empNombre"].setText(f"{empleado.emp_nombre1} {empleado.emp_apellido1}")
            self.entries["empIdentificacion"].setText(empleado.emp_identificacion)
            self.calculate_subtotal()  # Recalculate subtotal when employee is found

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

    def confirmar_desbon(self):
        desbon_codigo = self.entries["desBonCodigo"].currentText()
        tipo, codigo = desbon_codigo.split(" - ")
        descripcion = self.entries["desBonDescripcion"].text()
        valor = float(self.entries["desBonValor"].text())
        if tipo == "Bonificación":
            desbon = Bonificacion_Nom(bon_codigo=codigo, bon_descripcion=descripcion, bon_valor=valor,
                                      nom_codigo=self.entries["nomCodigo"].text())
        else:
            desbon = Descuento_Nom(des_codigo=codigo, des_descripcion=descripcion, des_valor=valor,
                                   nom_codigo=self.entries["nomCodigo"].text())
        self.nomina_desc_bon = [item for item in self.nomina_desc_bon if item.codigo != codigo]
        self.nomina_desc_bon.append(desbon)
        self.update_desbon_table()
        self.calculate_totals()

    def update_desbon_table(self):
        self.table.setRowCount(len(self.nomina_desc_bon))
        for row, desbon in enumerate(self.nomina_desc_bon):
            self.table.setItem(row, 0, QTableWidgetItem(desbon.codigo))
            self.table.setItem(row, 1, QTableWidgetItem(desbon.descripcion))
            self.table.setItem(row, 2, QTableWidgetItem(str(desbon.valor)))
            self.table.setItem(row, 3, QTableWidgetItem("Bonificación" if isinstance(desbon, Bonificacion_Nom) else "Descuento"))

            # Add delete button to each row
            btn_delete = QPushButton()
            btn_delete.setIcon(QIcon(ICON_DELETE_PATH))
            btn_delete.setIconSize(QSize(16, 16))
            btn_delete.clicked.connect(lambda _, r=row: self.eliminar_fila(r))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.addWidget(btn_delete)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_layout.setSpacing(10)

            self.table.setCellWidget(row, 4, action_widget)

    def eliminar_fila(self, row):
        desbon = self.nomina_desc_bon[row]
        if isinstance(desbon, Bonificacion_Nom):
            desbon.bon_status = 'INA'
        else:
            desbon.des_status = 'INA'
        self.nomina_desc_bon.pop(row)
        self.update_desbon_table()
        self.calculate_totals()

    def calculate_totals(self):
        total_bon = 0.0
        total_des = 0.0

        for desbon in self.nomina_desc_bon:
            if isinstance(desbon, Bonificacion_Nom) and desbon.bon_status == 'ACT':
                total_bon += float(desbon.bon_valor)
            elif isinstance(desbon, Descuento_Nom) and desbon.des_status == 'ACT':
                total_des += float(desbon.des_valor)

        subtotal = float(self.entries["nomSubTotal"].text())

        total = subtotal + total_bon - total_des
        self.entries["nomTotalBon"].setText(str(total_bon))
        self.entries["nomTotalDes"].setText(str(total_des))
        self.entries["nomTotal"].setText(str(total))

    def validate_total_hours(self):
        total_horas = self.entries["nomTotalHoras"].text()
        if not total_horas.isdigit() or not (1 <= int(total_horas) <= 160):
            QMessageBox.warning(self, "Advertencia", "El total de horas debe estar entre 1 y 160.")
            self.entries["nomTotalHoras"].setFocus()
            return False
        return True

    def validate_nom_codigo(self):
        nom_codigo = self.entries["nomCodigo"].text()
        if not nom_codigo.startswith("NOM-") or not nom_codigo[4:].isdigit() or len(nom_codigo[4:]) != 3:
            QMessageBox.warning(self, "Advertencia", "El código de nómina debe seguir el patrón NOM-###.")
            self.entries["nomCodigo"].setFocus()
            return False
        return True

    def recommend_nom_codigo(self):
        nominas = NominaDAO.seleccionar()
        max_codigo = 0
        for nomina in nominas:
            if nomina.nom_codigo.startswith("NOM-") and nomina.nom_codigo[4:].isdigit():
                codigo = int(nomina.nom_codigo[4:])
                if codigo > max_codigo:
                    max_codigo = codigo
        recommended_codigo = f"NOM-{max_codigo + 1:03d}"
        self.entries["nomCodigo"].setPlaceholderText(f"Recomendado: {recommended_codigo}")

    def validate_dates(self):
        fecha_inicial = self.entries["nomFechaInicial"].date()
        fecha_final = self.entries["nomFechaFinal"].date()
        if fecha_inicial > fecha_final:
            QMessageBox.warning(self, "Advertencia", "La fecha inicial no puede ser mayor que la fecha final.")
            self.entries["nomFechaInicial"].setFocus()
            return False
        return True

    def validate_form(self):
        if not self.validate_total_hours():
            return False
        if not self.validate_nom_codigo():
            return False
        if not self.validate_dates():
            return False
        return True

    def guardar_nomina(self):
        if not self.validate_form():
            return

        nomina = Nomina(
            nom_codigo=self.entries["nomCodigo"].text(),
            emp_codigo=self.entries["empCodigo"].currentText(),
            emp_cargo=self.entries["empCargo"].text(),
            nom_nombre_empleado=self.entries["empNombre"].text(),
            nom_anio=self.entries["nomAnio"].currentText(),
            nom_mes=self.transform_month(self.entries["nomMes"].currentText()),
            nom_fecha_inicial=self.entries["nomFechaInicial"].date().toString("yyyy-MM-dd"),
            nom_fecha_final=self.entries["nomFechaFinal"].date().toString("yyyy-MM-dd"),
            nom_total_horas=int(self.entries["nomTotalHoras"].text()),
            nom_subtotal=float(self.entries["nomSubTotal"].text()),
            nom_total_bonificaciones=float(self.entries["nomTotalBon"].text()),
            nom_total_descuentos=float(self.entries["nomTotalDes"].text()) * -1,
            nom_total=float(self.entries["nomTotal"].text()),
            nom_status="ACT"
        )
        bonificaciones = [item for item in self.nomina_desc_bon if isinstance(item, Bonificacion_Nom) and item.bon_status == 'ACT']
        descuentos = [item for item in self.nomina_desc_bon if isinstance(item, Descuento_Nom) and item.des_status == 'ACT']

        try:
            if NominaDAO.buscar(nomina.nom_codigo):
                NominaDAO.actualizar(nomina, descuentos, bonificaciones)
                QMessageBox.information(self, "Información", "Nómina actualizada exitosamente")
            else:
                NominaDAO.insertar(nomina, descuentos, bonificaciones)
                QMessageBox.information(self, "Información", "Nómina generada exitosamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al insertar la nómina: {str(e)}")

    def abrir_ventana_nominas(self):
        self.nominas_window = NominasWindow(self)
        self.nominas_window.table.itemDoubleClicked.connect(self.cargar_datos_edicion)
        self.nominas_window.show()

    def cancelar_nomina(self):
        nom_codigo = self.entries["nomCodigo"].text()
        NominaDAO.eliminar(nom_codigo)
        QMessageBox.information(self, "Información", "Nómina cancelada exitosamente")

    def cargar_datos_edicion(self, item):
        row = item.row()
        nom_codigo = self.nominas_window.table.item(row, 0).text()
        nomina = NominaDAO.buscar(nom_codigo)
        if nomina:
            self.cargar_nomina(nomina)
            self.cargar_desc_bon(
                DescuentoDAO.seleccionar_por_nomina(nom_codigo),
                BonificacionDAO.seleccionar_por_nomina(nom_codigo)
            )
            self.nominas_window.close()


    def cargar_nomina(self, nomina):
        self.entries["nomCodigo"].setText(nomina.nom_codigo)
        self.entries["empCodigo"].setCurrentText(nomina.emp_codigo)
        self.entries["empCargo"].setText(nomina.emp_cargo)
        self.entries["empNombre"].setText(nomina.nom_nombre_empleado)
        self.entries["empIdentificacion"].setText(EmpleadoDAO.buscar(nomina.emp_codigo).emp_identificacion)
        self.entries["nomAnio"].setCurrentText(nomina.nom_anio)
        self.entries["nomMes"].setCurrentText(self.reverse_transform_month(nomina.nom_mes))

        # Convert start and end dates to datetime objects if they are not
        if isinstance(nomina.nom_fecha_inicial, str):
            fecha_inicial = datetime.strptime(nomina.nom_fecha_inicial, "%Y-%m-%d").date()
        else:
            fecha_inicial = nomina.nom_fecha_inicial

        if isinstance(nomina.nom_fecha_final, str):
            fecha_final = datetime.strptime(nomina.nom_fecha_final, "%Y-%m-%d").date()
        else:
            fecha_final = nomina.nom_fecha_final

        self.entries["nomFechaInicial"].setDate(QDate.fromString(fecha_inicial.strftime("%Y-%m-%d"), "yyyy-MM-dd"))
        self.entries["nomFechaFinal"].setDate(QDate.fromString(fecha_final.strftime("%Y-%m-%d"), "yyyy-MM-dd"))

        self.entries["nomTotalHoras"].setText(str(nomina.nom_total_horas))
        self.entries["nomSubTotal"].setText(str(nomina.nom_subtotal))
        self.entries["nomTotalBon"].setText(str(nomina.nom_total_bonificaciones))
        self.entries["nomTotalDes"].setText(str(nomina.nom_total_descuentos))
        self.entries["nomTotal"].setText(str(nomina.nom_total))


    def cargar_desc_bon(self, descuentos, bonificaciones):
        self.nomina_desc_bon = []
        for bon in bonificaciones:
            self.nomina_desc_bon.append(
                Bonificacion_Nom(bon_codigo=bon[0], nom_codigo=bon[1], bon_valor=bon[2], bon_descripcion=bon[3])
            )
        for des in descuentos:
            self.nomina_desc_bon.append(
                Descuento_Nom(des_codigo=des[0], nom_codigo=des[1], des_valor=des[2], des_descripcion=des[3])
            )

        self.update_desbon_table()


    def calculate_subtotal(self):
        try:
            total_horas = float(self.entries["nomTotalHoras"].text())
            emp_codigo = self.entries["empCodigo"].currentText()
            empleado = EmpleadoDAO.buscar(emp_codigo)
            if empleado:
                sueldo = float(empleado.emp_sueldo)  # Convert sueldo to float
                subtotal = (sueldo / 160) * total_horas
                self.entries["nomSubTotal"].setText(str(subtotal))
                self.calculate_totals()  # Recalculate totals whenever the subtotal is recalculated
        except ValueError:
            self.entries["nomSubTotal"].setText("0")


    def transform_month(self, month_name):
        months = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        return months.get(month_name, "01")


    def reverse_transform_month(self, month_number):
        months = {
            "01": "January", "02": "February", "03": "March", "04": "April",
            "05": "May", "06": "June", "07": "July", "08": "August",
            "09": "September", "10": "October", "11": "November", "12": "December"
        }
        return months.get(month_number, "January")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = NominaGUI()
    gui.show()
    sys.exit(app.exec())
