from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models.usuario import Usuario, UsuarioDb

from logic.logica_usuario import LogicaUsuario


router = APIRouter( tags=['Autenticacion'] )

oauth2 = OAuth2PasswordBearer(tokenUrl='login')


async def current_user( token: str = Depends(oauth2) ):
    usuario: Usuario = LogicaUsuario.buscar_usuario( token )
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciales invalidas',
            headers={'WWW-Authenticate': "bearer"}
        )
        
    if not usuario.activo:
        raise HTTPException(
            detail="Usuario está inactivo",
            status_code=status.HTTP_400_BAD_REQUEST
        )
        
    return usuario


@router.get('/users/me')
async def perfil( usuario: Usuario = Depends( current_user ) ):
    return usuario


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    usuario: UsuarioDb = LogicaUsuario.buscar_usuario_db(form.username)
    
    if not usuario: raise HTTPException(
        detail="usuario no encontrado",
        status_code=status.HTTP_400_BAD_REQUEST
    )

    if not form.password == usuario.password:
        raise HTTPException(
            detail='Contraseña incorrecta',
            status_code=status.HTTP_400_BAD_REQUEST
        )
        
    if not usuario.activo:
        raise HTTPException(
            detail="Usuario está inactivo",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    return {
        "access_token": usuario.cedula, "token_type": "bearer"
    }
