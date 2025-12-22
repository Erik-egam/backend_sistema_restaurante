from config.dbconfig import get_conexion
from mysql.connector import Error
from fastapi import HTTPException, status
from models.orden import OrdenPlatos, Orden


class LogicaMesero:
    async def insert_order(orden: Orden, id_sede: int):
        cnx = get_conexion()
        cursor = cnx.cursor()

        try:
            cursor.execute(
                """
                    INSERT INTO ordenes ( id_sesion, pagado, preparado )
                    SELECT id_sesion, FALSE, FALSE FROM sesion
                    WHERE id_sede = %s AND activa = TRUE LIMIT 1;
                """, ( id_sede, )
            )
            
            id_orden = cursor.lastrowid
            platos = orden.platos
            for plato in platos:
                cursor.execute(
                    """
                        INSERT INTO ordenes_platos ( id_orden, id_plato, cantidad )
                        VALUES ( %s, %s, %s);
                    """, ( id_orden, plato.id_plato, plato.cantidad )
                )
            cnx.commit()
            cursor.close()
            cnx.close()
            
        except Error as e:
            cnx.rollback()
            raise HTTPException(
                # detail='Error al ejecutar acción',
                detail=f"{e}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
