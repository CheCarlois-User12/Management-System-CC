from logger_base import log
from cursor_del_pool import CursorDelPool
from Factura import Factura

class FacturaDAO:
    _SELECCIONAR = 'SELECT * FROM FACTURAS ORDER BY facCodigo'
    _INSERTAR = '''INSERT INTO FACTURAS (facCodigo, cliCodigo, facFecha, facHora, facSubtotal, facDescuento, facIva, facTotal, facFormaPago, facStatus) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE FACTURAS SET cliCodigo=%s, facFecha=%s, facHora=%s, facSubtotal=%s, facDescuento=%s, facIva=%s, facTotal=%s, facFormaPago=%s, facStatus=%s 
                     WHERE facCodigo=%s'''
    _ELIMINAR = 'DELETE FROM FACTURAS WHERE facCodigo=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            facturas = []
            for registro in registros:
                factura = Factura(*registro)
                facturas.append(factura)
            return facturas

    @classmethod
    def insertar(cls, factura):
        with CursorDelPool() as cursor:
            valores = (factura.facCodigo, factura.cliCodigo, factura.facFecha, factura.facHora, factura.facSubtotal,
                       factura.facDescuento, factura.facIva, factura.facTotal, factura.facFormaPago, factura.facStatus)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Factura insertada: {factura}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, factura):
        with CursorDelPool() as cursor:
            valores = (factura.cliCodigo, factura.facFecha, factura.facHora, factura.facSubtotal, factura.facDescuento,
                       factura.facIva, factura.facTotal, factura.facFormaPago, factura.facStatus, factura.facCodigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Factura actualizada: {factura}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, facCodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (facCodigo,))
            log.debug(f'Factura eliminada: {facCodigo}')
            return cursor.rowcount
