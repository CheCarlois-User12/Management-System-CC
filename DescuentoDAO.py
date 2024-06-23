# DescuentoDAO.py
from logger_base import log
from cursor_del_pool import CursorDelPool
from Descuento import Descuento

class DescuentoDAO:
    _SELECCIONAR = 'SELECT * FROM descuentos ORDER BY DESCODIGO'
    _INSERTAR = '''INSERT INTO descuentos(DESCODIGO, DESDESCRIPCION, DESVALOR) 
                  VALUES(%s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE descuentos SET DESDESCRIPCION=%s, DESVALOR=%s 
                    WHERE DESCODIGO=%s'''
    _ELIMINAR = 'DELETE FROM descuentos WHERE DESCODIGO=%s'
    _BUSCAR = "SELECT * FROM descuentos WHERE DESCODIGO=%s"

    @classmethod
    def buscar(cls, des_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (des_codigo,))
            registro = cursor.fetchone()
            if registro:
                return Descuento(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            descuentos = []
            for registro in registros:
                descuento = Descuento(*registro)
                descuentos.append(descuento)
            return descuentos

    @classmethod
    def insertar(cls, descuento):
        with CursorDelPool() as cursor:
            valores = (descuento.des_codigo, descuento.des_descripcion, descuento.des_valor)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Descuento insertado: {descuento}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, descuento):
        with CursorDelPool() as cursor:
            valores = (descuento.des_descripcion, descuento.des_valor, descuento.des_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Descuento actualizado: {descuento}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, descuento):
        with CursorDelPool() as cursor:
            valores = (descuento.des_codigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Descuento eliminado: {descuento}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    descuento1 = Descuento('DES-001', 'Descuento por pronto pago', 10.5)
    descuentos_insertados = DescuentoDAO.insertar(descuento1)
    log.debug(f'Descuentos insertados: {descuentos_insertados}')

    # Actualizar un registro
    descuento1 = Descuento('DES-001', 'Descuento por pronto pago actualizado', 15.0)
    descuentos_actualizados = DescuentoDAO.actualizar(descuento1)
    log.debug(f'Descuentos actualizados: {descuentos_actualizados}')

