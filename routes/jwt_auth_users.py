from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from datetime import datetime, timedelta

from jose import jwt, JWTError
from passlib.context import CryptContext

from models.usuario import Usuario, UsuarioDb

from logic.logica_usuario import LogicaUsuario

from config.constants import ALGORITHM, ACCESS_TOKEN_DURATION, SECRET

router = APIRouter( tags=[ 'Autenticacion' ] )

oauth2 = OAuth2PasswordBearer( tokenUrl='login' )

crypt = CryptContext( schemes=["bcrypt"] )

exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciales invalidas',
            headers={'WWW-Authenticate': "bearer"}
        )

async def usuario_autenticado( token: str = Depends( oauth2 )):
    try:
        cedula = jwt.decode( token, SECRET, algorithms= ALGORITHM ).get('sub')
        if cedula is None:
            raise exception
        
    except JWTError as e:
        raise exception
    
    return LogicaUsuario.buscar_usuario( cedula )


async def current_user( usuario: Usuario = Depends( usuario_autenticado ) ):
    
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
    
    

    if not crypt.verify( form.password , usuario.password ):
        raise HTTPException(
            detail='Contraseña incorrecta',
            status_code=status.HTTP_400_BAD_REQUEST
        )
        
        
    if not usuario.activo:
        raise HTTPException(
            detail="Usuario está inactivo",
            status_code=status.HTTP_400_BAD_REQUEST
        )
        
        
    access_token = {
        "sub": usuario.cedula,
        "exp": datetime.utcnow() + timedelta( minutes=ACCESS_TOKEN_DURATION, )
    }

    return {
        "access_token": jwt.encode( access_token, SECRET, algorithm=ALGORITHM ), "token_type": "bearer",
        "rol": usuario.rol
    }