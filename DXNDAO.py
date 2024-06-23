from conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool
from DXN import DXN

class DXNDAO:
    _SELECCIONAR = 'SELECT * FROM DXN WHERE dxnStatus <> "INA" ORDER BY desCodigo'
    _INSERTAR = '''INSERT INTO DXN(desCodigo, nomCodigo, dxnValor, dxnDescripcion, dxnStatus) 
                  VALUES(%s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE DXN SET dxnValor=%s, dxnDescripcion=%s, dxnStatus=%s WHERE desCodigo=%s AND nomCodigo=%s'''
    _ELIMINAR = 'UPDATE DXN SET dxnStatus="INA" WHERE desCodigo=%s AND nomCodigo=%s'
    _BUSCAR = "SELECT * FROM DXN WHERE desCodigo=%s AND nomCodigo=%s AND dxnStatus <> 'INA'"

    @classmethod
    def buscar(cls, des_codigo, nom_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (des_codigo, nom_codigo))
            registro = cursor.fetchone()
            if registro:
                return DXN(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            dxns = []
            for registro in registros:
                dxn = DXN(*registro)
                dxns.append(dxn)
            return dxns

    @staticmethod
    def insertar(dxn, cursor=None):
        query = DXNDAO._INSERTAR
        valores = (dxn.des_codigo, dxn.nom_codigo, dxn.dxn_valor, dxn.dxn_descripcion, dxn.dxn_status)
        if cursor:
            cursor.execute(query, valores)
        else:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            try:
                cursor.execute(query, valores)
                conexion.commit()
            except Exception as e:
                print(f"Error al insertar el descuento: {e}")
            finally:
                Conexion.liberarConexion(conexion)

    @classmethod
    def actualizar(cls, dxn):
        with CursorDelPool() as cursor:
            valores = (dxn.dxn_valor, dxn.dxn_descripcion, dxn.dxn_status, dxn.des_codigo, dxn.nom_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Descuento actualizado: {dxn}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, des_codigo, nom_codigo):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                query = "CALL desactivar_nomina(%s)"
                cursor.execute(query, (nom_codigo,))
            conexion.commit()
            log.debug(f'Descuento eliminado: des_codigo={des_codigo}, nom_codigo={nom_codigo}')
        except Exception as e:
            print(f"Error al eliminar el descuento: {e}")
        finally:
            Conexion.liberarConexion(conexion)
