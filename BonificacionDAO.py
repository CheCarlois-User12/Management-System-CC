from logger_base import log
from cursor_del_pool import CursorDelPool
from Bonificacion import Bonificacion

class BonificacionDAO:
    _SELECCIONAR = 'SELECT * FROM bonificaciones ORDER BY bonCodigo'
    _INSERTAR = 'INSERT INTO bonificaciones(bonCodigo, bonDescripcion, bonValor) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE bonificaciones SET bonDescripcion=%s, bonValor=%s WHERE bonCodigo=%s'
    _ELIMINAR = 'DELETE FROM bonificaciones WHERE bonCodigo=%s'
    _BUSCAR = 'SELECT * FROM bonificaciones WHERE bonCodigo=%s'

    @classmethod
    def buscar(cls, bon_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (bon_codigo,))
            registro = cursor.fetchone()
            if registro:
                return Bonificacion(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            bonificaciones = []
            for registro in registros:
                bonificacion = Bonificacion(*registro)
                bonificaciones.append(bonificacion)
            return bonificaciones

    @classmethod
    def insertar(cls, bonificacion):
        with CursorDelPool() as cursor:
            valores = (bonificacion.bon_codigo, bonificacion.bon_descripcion, bonificacion.bon_valor)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Bonificación insertada: {bonificacion}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, bonificacion):
        with CursorDelPool() as cursor:
            valores = (bonificacion.bon_descripcion, bonificacion.bon_valor, bonificacion.bon_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Bonificación actualizada: {bonificacion}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, bonificacion):
        with CursorDelPool() as cursor:
            valores = (bonificacion.bon_codigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Bonificación eliminada: {bonificacion}')
            return cursor.rowcount
