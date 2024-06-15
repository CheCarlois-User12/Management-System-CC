from logger_base import log
from conexion import Conexion
from descuentosPaquete.Descuento import Descuento
class DescuentoDAO:
    _SELECT = 'SELECT * FROM DESCUENTOS ORDER BY DESCODIGO'
    _INSERT = 'INSERT INTO DESCUENTOS (DESCODIGO, DESDESCRIPCION, DESVALOR) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE DESCUENTOS SET DESDESCRIPCION=%s, DESVALOR=%s WHERE DESCODIGO=%s'
    _DELETE = 'DELETE FROM DESCUENTOS WHERE DESCODIGO=%s'
    _SEARCH = 'SELECT * FROM DESCUENTOS WHERE DESCODIGO=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                descuentos = [Descuento(reg[0], reg[1], reg[2]) for reg in registros]
                return descuentos

    @classmethod
    def insertar(cls, descuento):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (descuento.des_codigo, descuento.des_descripcion, descuento.des_valor)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Descuento insertado: {descuento}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, descuento):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (descuento.des_descripcion, descuento.des_valor, descuento.des_codigo)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Descuento actualizado: {descuento}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, descuento):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (descuento.des_codigo,)
                cursor.execute(cls._DELETE, valores)
                log.debug(f'Descuento eliminado: {descuento}')
                return cursor.rowcount

    @classmethod
    def buscar(cls, des_codigo):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SEARCH, (des_codigo,))
                registro = cursor.fetchone()
                if registro:
                    return Descuento(registro[0], registro[1], registro[2])
                else:
                    return None
