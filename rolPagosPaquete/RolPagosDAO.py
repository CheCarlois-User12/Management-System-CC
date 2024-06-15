from logger_base import log
from cursor_del_pool import CursorDelPool
from rolPagosPaquete.RolPagos import RolPagos


class RolPagosDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM ROLPAGOS ORDER BY ROLCODIGO'
    _INSERTAR = '''INSERT INTO ROLPAGOS (ROLCODIGO, BONXDESCODIGO, DETCODIGO, ROLTOTALBENEFICIOS, 
                 ROLTOTALDESCUENTOS, ROLSUBTOTAL, ROLTOTALPAGAR) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE ROLPAGOS SET BONXDESCODIGO=%s, DETCODIGO=%s, ROLTOTALBENEFICIOS=%s, 
                    ROLTOTALDESCUENTOS=%s, ROLSUBTOTAL=%s, ROLTOTALPAGAR=%s WHERE ROLCODIGO=%s'''
    _ELIMINAR = 'DELETE FROM ROLPAGOS WHERE ROLCODIGO=%s'
    _BUSCAR = 'SELECT * FROM ROLPAGOS WHERE ROLCODIGO=%s'

    @classmethod
    def buscar(cls, rolcodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (rolcodigo,))
            registro = cursor.fetchone()
            if registro:
                return RolPagos(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            rolpagos = []
            for registro in registros:
                rolpago = RolPagos(*registro)
                rolpagos.append(rolpago)
            return rolpagos

    @classmethod
    def insertar(cls, rolpago):
        with CursorDelPool() as cursor:
            valores = (rolpago.rolcodigo, rolpago.bonxdescodigo, rolpago.detcodigo, rolpago.roltotalbeneficios,
                       rolpago.roltotaldescuentos, rolpago.rolsubtotal, rolpago.roltotalpagar)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'RolPagos insertado: {rolpago}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, rolpago):
        with CursorDelPool() as cursor:
            valores = (rolpago.bonxdescodigo, rolpago.detcodigo, rolpago.roltotalbeneficios,
                       rolpago.roltotaldescuentos, rolpago.rolsubtotal, rolpago.roltotalpagar, rolpago.rolcodigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'RolPagos actualizado: {rolpago}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, rolpago):
        with CursorDelPool() as cursor:
            valores = (rolpago.rolcodigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'RolPagos eliminado: {rolpago}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    rolpago1 = RolPagos('ROL001', 'BXD001', 'DET001', 1500.00, 500.00, 1000.00, 1000.00)
    rolpagos_insertados = RolPagosDAO.insertar(rolpago1)
    log.debug(f'RolPagos insertados: {rolpagos_insertados}')

    # Actualizar un registro
    rolpago1 = RolPagos('ROL001', 'BXD002', 'DET002', 2000.00, 600.00, 1400.00, 1400.00)
    rolpagos_actualizados = RolPagosDAO.actualizar(rolpago1)

