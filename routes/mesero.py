from fastapi import APIRouter, Depends, HTTPException, status
from routes.jwt_auth_users import current_user

from models.usuario import Usuario
from models.orden import Orden

from logic.logica_mesero import LogicaMesero


router = APIRouter( tags= [ "Mesero" ] )

def isMesero( rol: int ):
    return rol == 'MESERO'


@router.post( '/order/{id_sede}', status_code=status.HTTP_201_CREATED )
async def create_order( orden: Orden, id_sede: int, usuario: Usuario = Depends( current_user )):
    
    if not isMesero( usuario.rol ): raise HTTPException(
        detail="Usuario no autorizado para realizar esta acción",
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    
    if orden == None: raise HTTPException(
        detail="Request sin información necesaria",
        status_code=status.HTTP_400_BAD_REQUEST
    )

    if len(orden.platos) == 0: raise HTTPException(
        detail="No hay platos seleccionados",
        status_code=status.HTTP_400_BAD_REQUEST
    )
    
    await LogicaMesero.insert_order( orden, id_sede )
    
    return {
        'detail': 'Orden registrada correctamente'
    }
    
    