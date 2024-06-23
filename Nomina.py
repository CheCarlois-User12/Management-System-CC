class Nomina:
    def __init__(self, nom_codigo=None, emp_codigo=None, emp_cargo=None, nom_nombre_empleado=None, nom_anio=None,
                 nom_mes=None, nom_fecha_inicial=None, nom_fecha_final=None, nom_total_horas=None,
                 nom_subtotal=None, nom_total_bonificaciones=None, nom_total_descuentos=None, nom_total=None,
                 nom_status=None):
        self._nom_codigo = nom_codigo
        self._emp_codigo = emp_codigo
        self._emp_cargo = emp_cargo
        self._nom_nombre_empleado = nom_nombre_empleado
        self._nom_anio = nom_anio
        self._nom_mes = nom_mes
        self._nom_fecha_inicial = nom_fecha_inicial
        self._nom_fecha_final = nom_fecha_final
        self._nom_total_horas = nom_total_horas
        self._nom_subtotal = nom_subtotal
        self._nom_total_bonificaciones = nom_total_bonificaciones
        self._nom_total_descuentos = nom_total_descuentos
        self._nom_total = nom_total
        self._nom_status = nom_status

    def __str__(self):
        return f'Nómina: {self._nom_codigo}, Empleado: {self._emp_codigo}, Cargo: {self._emp_cargo}, ' \
               f'Nombre: {self._nom_nombre_empleado}, Año: {self._nom_anio}, Mes: {self._nom_mes}, ' \
               f'Fecha Inicial: {self._nom_fecha_inicial}, Fecha Final: {self._nom_fecha_final}, ' \
               f'Total Horas: {self._nom_total_horas}, Subtotal: {self._nom_subtotal}, ' \
               f'Total Bonificaciones: {self._nom_total_bonificaciones}, Total Descuentos: {self._nom_total_descuentos}, ' \
               f'Total: {self._nom_total}, Estado: {self._nom_status}'

    # Getters
    @property
    def nom_codigo(self):
        return self._nom_codigo

    @property
    def emp_codigo(self):
        return self._emp_codigo

    @property
    def emp_cargo(self):
        return self._emp_cargo

    @property
    def nom_nombre_empleado(self):
        return self._nom_nombre_empleado

    @property
    def nom_anio(self):
        return self._nom_anio

    @property
    def nom_mes(self):
        return self._nom_mes

    @property
    def nom_fecha_inicial(self):
        return self._nom_fecha_inicial

    @property
    def nom_fecha_final(self):
        return self._nom_fecha_final

    @property
    def nom_total_horas(self):
        return self._nom_total_horas

    @property
    def nom_subtotal(self):
        return self._nom_subtotal

    @property
    def nom_total_bonificaciones(self):
        return self._nom_total_bonificaciones

    @property
    def nom_total_descuentos(self):
        return self._nom_total_descuentos

    @property
    def nom_total(self):
        return self._nom_total

    @property
    def nom_status(self):
        return self._nom_status

    # Setters
    @nom_codigo.setter
    def nom_codigo(self, value):
        self._nom_codigo = value

    @emp_codigo.setter
    def emp_codigo(self, value):
        self._emp_codigo = value

    @emp_cargo.setter
    def emp_cargo(self, value):
        self._emp_cargo = value

    @nom_nombre_empleado.setter
    def nom_nombre_empleado(self, value):
        self._nom_nombre_empleado = value

    @nom_anio.setter
    def nom_anio(self, value):
        self._nom_anio = value

    @nom_mes.setter
    def nom_mes(self, value):
        self._nom_mes = value

    @nom_fecha_inicial.setter
    def nom_fecha_inicial(self, value):
        self._nom_fecha_inicial = value

    @nom_fecha_final.setter
    def nom_fecha_final(self, value):
        self._nom_fecha_final = value

    @nom_total_horas.setter
    def nom_total_horas(self, value):
        self._nom_total_horas = value

    @nom_subtotal.setter
    def nom_subtotal(self, value):
        self._nom_subtotal = value

    @nom_total_bonificaciones.setter
    def nom_total_bonificaciones(self, value):
        self._nom_total_bonificaciones = value

    @nom_total_descuentos.setter
    def nom_total_descuentos(self, value):
        self._nom_total_descuentos = value

    @nom_total.setter
    def nom_total(self, value):
        self._nom_total = value

    @nom_status.setter
    def nom_status(self, value):
        self._nom_status = value
