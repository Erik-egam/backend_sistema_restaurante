from config.dbconfig import get_conexion
from mysql.connector import Error
from fastapi import HTTPException, status
from models.orden import OrdenPlatos, Orden


class LogicaCocina:
    async def setOrdenPreparada(id_orden: int):
        cnx = get_conexion()
        cursor = cnx.cursor()

        try:
            cursor.execute(
                "Update ordenes Set preparado=TRUE WHERE id_orden=%s",
                (id_orden, )
            )
            cnx.commit()
            cursor.close()
            cnx.close()

        except Error as e:
            raise HTTPException(
                detail=f"{e}",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    async def getOrdenesPorPreparar(id_sede: int):
        cnx = get_conexion()
        cursor = cnx.cursor()

        try:
            cursor.execute(
                """SELECT * FROM ordenes o 
                JOIN ordenes_platos op ON o.id_orden = op.id_orden  WHERE
                id_sesion=(
                    SELECT id_sesion FROM sesion
                    WHERE id_sede = %s AND activa = TRUE LIMIT 1
                    ) AND o.preparado=FALSE;""", (id_sede, )
            )

            resultado = cursor.fetchall()
            id_actual = resultado[0][0]
            ordenes = []
            platos = [
                OrdenPlatos(
                    id_plato=resultado[0][-2],
                    cantidad=resultado[0][-1],
                )
            ]
            for i in range(1, len(resultado)):

                if id_actual == resultado[i][0]:
                    platos.append(
                        OrdenPlatos(
                            id_plato=resultado[i][-2],
                            cantidad=resultado[i][-1],
                        )
                    )
                else:
                    ordenes.append(
                        Orden(
                            id_orden=resultado[i - 1][0],
                            platos=platos
                        )
                    )
                    platos = []
                    id_actual = resultado[i][0]
                    platos.append(
                        OrdenPlatos(
                            id_plato=resultado[i][-2],
                            cantidad=resultado[i][-1],
                        )
                    )
                    
            if id_actual == resultado[-1][0]:
                ordenes.append(
                        Orden(
                            id_orden=resultado[i - 1][0],
                            platos=platos
                        )
                    )
                
            else:
                    ordenes.append(
                        Orden(
                            id_orden=resultado[i - 1][0],
                            platos=platos
                        )
                    )
                    platos = []
                    id_actual = resultado[i][0]
                    platos.append(
                        OrdenPlatos(
                            id_plato=resultado[i][-2],
                            cantidad=resultado[i][-1],
                        )
                    )

            cursor.close()
            cnx.close()

            return ordenes
        except Error as e:
            raise HTTPException(
                detail=f"{e}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
