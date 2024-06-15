from logger_base import log
from cursor_del_pool import CursorDelPool
from bonxdesxoPaquete.Bonxdesxo import Bonxdesxo

class BonxdesxoDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM BONXDESXO ORDER BY BONXDESCODIGO'
    _INSERTAR = 'INSERT INTO BONXDESXO (DESCODIGO, BONCODIGO, BONXDESCODIGO, BONXDESVALOR) VALUES (%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE BONXDESXO SET DESCODIGO=%s, BONCODIGO=%s, BONXDESVALOR=%s WHERE BONXDESCODIGO=%s'
    _ELIMINAR = 'DELETE FROM BONXDESXO WHERE BONXDESCODIGO=%s'
    _BUSCAR = 'SELECT * FROM BONXDESXO WHERE BONXDESCODIGO=%s'

    @classmethod
    def buscar(cls, bonxdescodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (bonxdescodigo,))
            registro = cursor.fetchone()
            if registro:
                return Bonxdesxo(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            bonxdesxos = []
            for registro in registros:
                bonxdesxo = Bonxdesxo(*registro)
                bonxdesxos.append(bonxdesxo)
            return bonxdesxos

    @classmethod
    def insertar(cls, bonxdesxo):
        with CursorDelPool() as cursor:
            valores = (bonxdesxo.descodigo, bonxdesxo.boncodigo, bonxdesxo.bonxdescodigo, bonxdesxo.bonxdesvalor)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Bonxdesxo insertado: {bonxdesxo}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, bonxdesxo):
        with CursorDelPool() as cursor:
            valores = (bonxdesxo.descodigo, bonxdesxo.boncodigo, bonxdesxo.bonxdesvalor, bonxdesxo.bonxdescodigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Bonxdesxo actualizado: {bonxdesxo}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, bonxdesxo):
        with CursorDelPool() as cursor:
            valores = (bonxdesxo.bonxdescodigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Bonxdesxo eliminado: {bonxdesxo}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    bonxdesxo1 = Bonxdesxo('DESC001', 'BON001', 'BXD001', 123.45)
    bonxdesxos_insertados = BonxdesxoDAO.insertar(bonxdesxo1)
    log.debug(f'Bonxdesxos insertados: {bonxdesxos_insertados}')

    # Actualizar un registro
    bonxdesxo1 = Bonxdesxo('DESC002', 'BON002', 'BXD001', 678.90)
    bonxdesxos_actualizados = BonxdesxoDAO.actualizar(bonxdesxo1)
    log.debug(f'Bonxdesxos actualizados: {bonxdesxos_actualizados}')

    # Eliminar un registro
    bonxdesxo1 = Bonxdesxo(bonxdescodigo='BXD001')
    bonxdesxos_eliminados = BonxdesxoDAO.eliminar(bonxdesxo1)
    log.debug(f'Bonxdesxos eliminados: {bonxdesxos_eliminados}')

    # Seleccionar objetos
    bonxdesxos = BonxdesxoDAO.seleccionar()
    for bonxdesxo in bonxdesxos:
        log.debug(bonxdesxo)
