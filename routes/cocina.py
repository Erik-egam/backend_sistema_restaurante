from fastapi import APIRouter, Depends, HTTPException, status
from routes.jwt_auth_users import current_user

from models.usuario import Usuario
from models.orden import Orden

from logic.logica_cocina import LogicaCocina


router = APIRouter( tags= [ "Cocina" ] )

def isCocina( rol: int ):
    return rol == 'COCINA'

@router.patch("/order/{id_orden}", status_code=status.HTTP_202_ACCEPTED)
async def set_order_preparada( id_orden: int, usuario: Usuario = Depends( current_user ) ):
    
    if not isCocina( usuario.rol ): raise HTTPException(
        detail="Usuario no autorizado para realizar esta acción",
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    
    await LogicaCocina.setOrdenPreparada( id_orden )
    return {
        "detail": "Estado de la orden actualizada"
    }


@router.get("/orders/{id_sede}/preparar", status_code=status.HTTP_202_ACCEPTED)
async def set_order_preparada( id_sede: int, usuario: Usuario = Depends( current_user ) ):
    
    if not isCocina( usuario.rol ): raise HTTPException(
        detail="Usuario no autorizado para realizar esta acción",
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    
    return await LogicaCocina.getOrdenesPorPreparar( id_sede )