from logger_base import log
from cursor_del_pool import CursorDelPool
from ProductosDetails import ProductosDetails

class ProductosDetailsDAO:
    _SELECCIONAR = 'SELECT * FROM PXFA ORDER BY facCodigo'
    _INSERTAR = '''INSERT INTO PXFA(prodCodigo, facCodigo, pxfCantidad, pxfValor) 
                  VALUES(%s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE PXFA SET pxfCantidad=%s, pxfValor=%s WHERE prodCodigo=%s AND facCodigo=%s'''
    _ELIMINAR = 'DELETE FROM PXFA WHERE facCodigo=%s'
    _BUSCAR = "SELECT * FROM PXFA WHERE facCodigo=%s"

    @classmethod
    def buscar(cls, fac_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (fac_codigo,))
            registros = cursor.fetchall()
            detalles = []
            for registro in registros:
                detalle = ProductosDetails(*registro)
                detalles.append(detalle)
            return detalles

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            detalles = []
            for registro in registros:
                detalle = ProductosDetails(*registro)
                detalles.append(detalle)
            return detalles

    @classmethod
    def insertar(cls, detalle):
        with CursorDelPool() as cursor:
            valores = (detalle.prodCodigo, detalle.facCodigo, detalle.prodxdetCantidad, detalle.prodxdetIVASubtotal)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Detalle insertado: {detalle}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, detalle):
        with CursorDelPool() as cursor:
            valores = (detalle.prodxdetCantidad, detalle.prodxdetIVASubtotal, detalle.prodCodigo, detalle.facCodigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Detalle actualizado: {detalle}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, fac_codigo):
        with CursorDelPool() as cursor:
            valores = (fac_codigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Detalles eliminados para la factura: {fac_codigo}')
            return cursor.rowcount
