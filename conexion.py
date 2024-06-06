from logger_base import log
import mysql.connector
from mysql.connector import pooling
import sys

class Conexion:
    _DATABASE = 'modeloComercial'
    _USERNAME = 'root'
    _PASSWORD = 'MariaDB123'
    _DB_PORT = '3307'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name="mypool",
                    pool_size=cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except mysql.connector.Error as e:
                log.error(f'Ocurrió un error al obtener el pool {e.errno} ({e.sqlstate}): {e.msg}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        try:
            conexion = cls.obtenerPool().get_connection()
            log.debug(f'Conexión obtenida del pool: {conexion}')
            return conexion
        except mysql.connector.Error as e:
            log.error(f'Ocurrió un error al obtener la conexión {e.errno} ({e.sqlstate}): {e.msg}')
            sys.exit()

    @classmethod
    def liberarConexion(cls, conexion):
        try:
            conexion.close()
            log.debug(f'Regresamos la conexión al pool: {conexion}')
        except mysql.connector.Error as e:
            log.error(f'Ocurrió un error al liberar la conexión {e.errno} ({e.sqlstate}): {e.msg}')

    @classmethod
    def cerrarConexiones(cls):
        if cls._pool is not None:
            cls._pool.close()
            log.debug(f'Todas las conexiones del pool han sido cerradas')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
