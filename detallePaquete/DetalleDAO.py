from logger_base import log
from cursor_del_pool import CursorDelPool
from detallePaquete.Detalle import Detalle

class DetalleDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM DETALLE ORDER BY DETCODIGO'
    _INSERTAR = '''INSERT INTO DETALLE (EMPCODIGO, DETCODIGO, DETEMPNOMBRE1, DETEMPAPELLIDO1, 
                 DETEMPBANCO, DETEMPCUENTA, DETEMPSTATUS, DETEMPSUELDO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE DETALLE SET EMPCODIGO=%s, DETEMPNOMBRE1=%s, DETEMPAPELLIDO1=%s, 
                    DETEMPBANCO=%s, DETEMPCUENTA=%s, DETEMPSTATUS=%s, DETEMPSUELDO=%s WHERE DETCODIGO=%s'''
    _ELIMINAR = 'DELETE FROM DETALLE WHERE DETCODIGO=%s'
    _BUSCAR = 'SELECT * FROM DETALLE WHERE DETCODIGO=%s'

    @classmethod
    def buscar(cls, detcodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (detcodigo,))
            registro = cursor.fetchone()
            if registro:
                return Detalle(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            detalles = []
            for registro in registros:
                detalle = Detalle(*registro)
                detalles.append(detalle)
            return detalles

    @classmethod
    def insertar(cls, detalle):
        with CursorDelPool() as cursor:
            valores = (detalle.empcodigo, detalle.detcodigo, detalle.detempnombre1, detalle.detempapellido1,
                       detalle.detempbanco, detalle.detempcuenta, detalle.detempstatus, detalle.detempsueldo)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Detalle insertado: {detalle}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, detalle):
        with CursorDelPool() as cursor:
            valores = (detalle.empcodigo, detalle.detempnombre1, detalle.detempapellido1, detalle.detempbanco,
                       detalle.detempcuenta, detalle.detempstatus, detalle.detempsueldo, detalle.detcodigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Detalle actualizado: {detalle}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, detalle):
        with CursorDelPool() as cursor:
            valores = (detalle.detcodigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Detalle eliminado: {detalle}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    detalle1 = Detalle('EMP001', 'DET001', 'Carlos', 'Velastegui', 'Pichincha', 'CUE-1234567890', 'ACT', 1234.56)
    detalles_insertados = DetalleDAO.insertar(detalle1)
    log.debug(f'Detalles insertados: {detalles_insertados}')

    # Actualizar un registro
    detalle1 = Detalle('EMP001', 'DET001', 'Carlos', 'Velastegui', 'Pichincha', 'CUE-0987654321', 'ACT', 5678.90)
    detalles_actualizados = DetalleDAO.actualizar(detalle1)
    log.debug(f'Detalles actualizados: {detalles_actualizados}')

    # Eliminar un registro
    detalle1 = Detalle(detcodigo='DET001')
    detalles_eliminados = DetalleDAO.eliminar(detalle1)
    log.debug(f'Detalles eliminados: {detalles_eliminados}')

    # Seleccionar objetos
    detalles = DetalleDAO.seleccionar()
    for detalle in detalles:
        log.debug(detalle)
