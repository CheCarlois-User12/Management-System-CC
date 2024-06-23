from logger_base import log
from cursor_del_pool import CursorDelPool
from Empleado import Empleado

class EmpleadoDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM empleados ORDER BY EMPCODIGO'
    _INSERTAR = '''INSERT INTO empleados(EMPCODIGO, EMPAPELLIDO1, EMPAPELLIDO2, EMPNOMBRE1, EMPNOMBRE2, EMPIDENTIFICACION, EMPFECHANACIMIENTO, 
                  EMPTIPOSANGRE, EMPSEXO, EMPCARGO, EMPEMAIL, EMPDIRECCION, EMPSUELDO, EMPBANCO, EMPCUENTA, EMPSTATUS) 
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE empleados SET EMPAPELLIDO1=%s, EMPAPELLIDO2=%s, EMPNOMBRE1=%s, EMPNOMBRE2=%s, EMPIDENTIFICACION=%s, EMPFECHANACIMIENTO=%s, 
                    EMPTIPOSANGRE=%s, EMPSEXO=%s, EMPCARGO=%s, EMPEMAIL=%s, EMPDIRECCION=%s, EMPSUELDO=%s, EMPBANCO=%s, EMPCUENTA=%s, EMPSTATUS=%s 
                    WHERE EMPCODIGO=%s'''
    _ELIMINAR = 'DELETE FROM empleados WHERE EMPCODIGO=%s'
    _BUSCAR = "SELECT * FROM empleados WHERE EMPCODIGO=%s"

    @classmethod
    def buscar(cls, emp_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (emp_codigo,))
            registro = cursor.fetchone()
            if registro:
                return Empleado(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for registro in registros:
                empleado = Empleado(*registro)
                empleados.append(empleado)
            return empleados

    @classmethod
    def insertar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.emp_codigo, empleado.emp_apellido1, empleado.emp_apellido2, empleado.emp_nombre1,
                       empleado.emp_nombre2, empleado.emp_identificacion, empleado.emp_fecha_nacimiento,
                       empleado.emp_tipo_sangre, empleado.emp_sexo, empleado.emp_cargo, empleado.emp_email,
                       empleado.emp_direccion, empleado.emp_sueldo, empleado.emp_banco, empleado.emp_cuenta,
                       empleado.emp_status)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Empleado insertado: {empleado}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.emp_apellido1, empleado.emp_apellido2, empleado.emp_nombre1, empleado.emp_nombre2,
                       empleado.emp_identificacion, empleado.emp_fecha_nacimiento, empleado.emp_tipo_sangre,
                       empleado.emp_sexo, empleado.emp_cargo, empleado.emp_email, empleado.emp_direccion,
                       empleado.emp_sueldo, empleado.emp_banco, empleado.emp_cuenta, empleado.emp_status,
                       empleado.emp_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Empleado actualizado: {empleado}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.emp_codigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Empleado eliminado: {empleado}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    empleado1 = Empleado('EMP-001', 'Velastegui', 'Constante', 'Carlos', 'Francisco', '1234567890', '2004-11-22', 'A+', 'M', 'Programador', 'cf@outlook.com', 'La tolita', 100.1, 'Pichincha', 'CUE-0000000000000001', 'ACT')
    empleados_insertados = EmpleadoDAO.insertar(empleado1)
    log.debug(f'Empleados insertados: {empleados_insertados}')

    # Actualizar un registro
    empleado1 = Empleado('EMP-001', 'Velastegui', 'Constante', 'Carlos', 'Francisco', '1234567890', '2004-11-22', 'A+', 'M', 'Analista', 'cf_new@outlook.com', 'La tolita nueva', 200.5, 'Pichincha', 'CUE-0000000000000002', 'ACT')
    empleados_actualizados = EmpleadoDAO.actualizar(empleado1)
    log.debug(f'Empleados actualizados: {empleados_actualizados}')

    # Eliminar un registro
    empleado1 = Empleado(emp_codigo='EMP-001')
    empleados_eliminados = EmpleadoDAO.eliminar(empleado1)
    log.debug(f'Empleados eliminados: {empleados_eliminados}')

    # Seleccionar objetos
    empleados = EmpleadoDAO.seleccionar()
    for empleado in empleados:
        log.debug(empleado)
