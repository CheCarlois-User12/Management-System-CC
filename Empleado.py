
# empleado.py
class Empleado:
    def __init__(self, emp_codigo=None, emp_apellido1=None, emp_apellido2=None, emp_nombre1=None, emp_nombre2=None,
                 emp_fecha_nacimiento=None, emp_sexo=None, emp_email=None, emp_direccion=None, emp_tipo_sangre=None,
                 emp_sueldo=None, emp_banco=None, emp_cuenta=None, emp_status=None):

        self._emp_codigo = emp_codigo
        self._emp_apellido1 = emp_apellido1
        self._emp_apellido2 = emp_apellido2
        self._emp_nombre1 = emp_nombre1
        self._emp_nombre2 = emp_nombre2
        self._emp_fecha_nacimiento = emp_fecha_nacimiento
        self._emp_sexo = emp_sexo
        self._emp_email = emp_email
        self._emp_direccion = emp_direccion
        self._emp_tipo_sangre = emp_tipo_sangre
        self._emp_sueldo = emp_sueldo
        self._emp_banco = emp_banco
        self._emp_cuenta = emp_cuenta
        self._emp_status = emp_status

    def __str__(self):
        return f'''
            Código: {self._emp_codigo}, Apellido1: {self._emp_apellido1},
            Apellido2: {self._emp_apellido2}, Nombre1: {self._emp_nombre1},
            Nombre2: {self._emp_nombre2}, Fecha de Nacimiento: {self._emp_fecha_nacimiento},
            Sexo: {self._emp_sexo}, Email: {self._emp_email}, Dirección: {self._emp_direccion},
            Tipo de Sangre: {self._emp_tipo_sangre}, Sueldo: {self._emp_sueldo}, Banco: {self._emp_banco},
            Cuenta Bancaria: {self._emp_cuenta}, Estado: {self._emp_status}
        '''

    @property
    def emp_codigo(self):
        return self._emp_codigo

    @emp_codigo.setter
    def emp_codigo(self, emp_codigo):
        self._emp_codigo = emp_codigo

    @property
    def emp_apellido1(self):
        return self._emp_apellido1

    @emp_apellido1.setter
    def emp_apellido1(self, emp_apellido1):
        self._emp_apellido1 = emp_apellido1

    @property
    def emp_apellido2(self):
        return self._emp_apellido2

    @emp_apellido2.setter
    def emp_apellido2(self, emp_apellido2):
        self._emp_apellido2 = emp_apellido2

    @property
    def emp_nombre1(self):
        return self._emp_nombre1

    @emp_nombre1.setter
    def emp_nombre1(self, emp_nombre1):
        self._emp_nombre1 = emp_nombre1

    @property
    def emp_nombre2(self):
        return self._emp_nombre2

    @emp_nombre2.setter
    def emp_nombre2(self, emp_nombre2):
        self._emp_nombre2 = emp_nombre2

    @property
    def emp_fecha_nacimiento(self):
        return self._emp_fecha_nacimiento

    @emp_fecha_nacimiento.setter
    def emp_fecha_nacimiento(self, emp_fecha_nacimiento):
        self._emp_fecha_nacimiento = emp_fecha_nacimiento

    @property
    def emp_sexo(self):
        return self._emp_sexo

    @emp_sexo.setter
    def emp_sexo(self, emp_sexo):
        self._emp_sexo = emp_sexo

    @property
    def emp_email(self):
        return self._emp_email

    @emp_email.setter
    def emp_email(self, emp_email):
        self._emp_email = emp_email

    @property
    def emp_direccion(self):
        return self._emp_direccion

    @emp_direccion.setter
    def emp_direccion(self, emp_direccion):
        self._emp_direccion = emp_direccion

    @property
    def emp_tipo_sangre(self):
        return self._emp_tipo_sangre

    @emp_tipo_sangre.setter
    def emp_tipo_sangre(self, emp_tipo_sangre):
        self._emp_tipo_sangre = emp_tipo_sangre

    @property
    def emp_sueldo(self):
        return self._emp_sueldo

    @emp_sueldo.setter
    def emp_sueldo(self, emp_sueldo):
        self._emp_sueldo = emp_sueldo

    @property
    def emp_banco(self):
        return self._emp_banco

    @emp_banco.setter
    def emp_banco(self, emp_banco):
        self._emp_banco = emp_banco

    @property
    def emp_cuenta(self):
        return self._emp_cuenta

    @emp_cuenta.setter
    def emp_cuenta(self, emp_cuenta):
        self._emp_cuenta = emp_cuenta

    @property
    def emp_status(self):
        return self._emp_status

    @emp_status.setter
    def emp_status(self, emp_status):
        self._emp_status = emp_status

# empleado_dao.py
from logger_base import log
from cursor_del_pool import CursorDelPool
from Empleado import Empleado