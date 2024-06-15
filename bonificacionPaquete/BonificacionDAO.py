from logger_base import log
from conexion import Conexion
from bonificacionPaquete.Bonificacion import Bonificacion
class BonificacionDAO:
    _SELECT = 'SELECT * FROM BONIFICACIONES ORDER BY BONCODIGO'
    _INSERT = 'INSERT INTO BONIFICACIONES (BONCODIGO, BONDESCRIPCION, BONVALOR) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE BONIFICACIONES SET BONDESCRIPCION=%s, BONVALOR=%s WHERE BONCODIGO=%s'
    _DELETE = 'DELETE FROM BONIFICACIONES WHERE BONCODIGO=%s'
    _SEARCH = 'SELECT * FROM BONIFICACIONES WHERE BONCODIGO=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                bonificaciones = [Bonificacion(reg[0], reg[1], reg[2]) for reg in registros]
                return bonificaciones

    @classmethod
    def insertar(cls, bonificacion):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (bonificacion.bon_codigo, bonificacion.bon_descripcion, bonificacion.bon_valor)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Bonificacion insertada: {bonificacion}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, bonificacion):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (bonificacion.bon_descripcion, bonificacion.bon_valor, bonificacion.bon_codigo)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Bonificacion actualizada: {bonificacion}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, bonificacion):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (bonificacion.bon_codigo,)
                cursor.execute(cls._DELETE, valores)
                log.debug(f'Bonificacion eliminada: {bonificacion}')
                return cursor.rowcount

    @classmethod
    def buscar(cls, bon_codigo):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SEARCH, (bon_codigo,))
                registro = cursor.fetchone()
                if registro:
                    return Bonificacion(registro[0], registro[1], registro[2])
                else:
                    return None
