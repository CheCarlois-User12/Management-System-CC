from logger_base import log
from cursor_del_pool import CursorDelPool
from Producto import Producto

class ProductoDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM productos ORDER BY PRODCODIGO'

    _INSERTAR = '''INSERT INTO productos(PRODCODIGO, PRODDESCRIPCION, PRODUNIDADMEDIDA, PRODSALDOINICIAL, PRODINGRESOS, PRODEGRESOS, PRODAJUSTES, PRODSALDOFINAL, PRODCOSTOXUNIDAD, PRODSTATUS) 
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    _ACTUALIZAR = '''UPDATE productos SET PRODDESCRIPCION=%s, PRODUNIDADMEDIDA=%s, PRODSALDOINICIAL=%s, PRODINGRESOS=%s, PRODEGRESOS=%s, PRODAJUSTES=%s, PRODSALDOFINAL=%s, PRODCOSTOXUNIDAD=%s, PRODSTATUS=%s 
                     WHERE PRODCODIGO=%s'''

    _ELIMINAR = 'DELETE FROM productos WHERE PRODCODIGO=%s'

    _BUSCAR = "SELECT * FROM productos WHERE PRODCODIGO=%s"

    @classmethod
    def buscar(cls, prod_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (prod_codigo,))
            registro = cursor.fetchone()
            if registro:
                return Producto(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(*registro)
                productos.append(producto)
            return productos

    @classmethod
    def insertar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.prod_codigo, producto.prod_descripcion, producto.prod_unidad_medida, producto.prod_saldo_inicial,
                       producto.prod_ingresos, producto.prod_egresos, producto.prod_ajustes, producto.prod_saldo_final,
                       producto.prod_costo_x_unidad, producto.prod_status)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Producto insertado: {producto}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.prod_descripcion, producto.prod_unidad_medida, producto.prod_saldo_inicial, producto.prod_ingresos,
                       producto.prod_egresos, producto.prod_ajustes, producto.prod_saldo_final, producto.prod_costo_x_unidad,
                       producto.prod_status, producto.prod_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Producto actualizado: {producto}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.prod_codigo,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Producto eliminado: {producto}')
            return cursor.rowcount
