import sys

import mysql.connector
from mysql.connector import pooling
from logger_base import log
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import json
from RSAProteccion import RSAProteccion

class Conexion:
    _DATABASE = 'modeloComercial'
    _DB_PORT = '3307'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                config = cls.cargar_configuracion()
                usuario = config['user']
                clave = config['password']
                rsa_proteccion = RSAProteccion()
                rsa_proteccion.load_keys('private_key.pem', 'public_key.pem')
                usuario = rsa_proteccion.decrypt(base64.b64decode(usuario))
                clave = rsa_proteccion.decrypt(base64.b64decode(clave))
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name="mypool",
                    pool_size=cls._MAX_CON,
                    host=cls._HOST,
                    user=usuario,
                    password=clave,
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

    @classmethod
    def cargar_configuracion(cls):
        config_path = r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\conexiones_base_datos.json'
        try:
            with open(config_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            log.error(f"Error al cargar configuración de la base de datos: {str(e)}")
            return {}

    @classmethod
    def limpiar_configuracion(cls):
        config_path = r'C:\Users\Carlos\Desktop\EmpleadosManagmentSystem\conexiones_base_datos.json'
        with open(config_path, 'w') as file:
            json.dump({}, file)
            log.debug("Configuración de la base de datos limpiada")
