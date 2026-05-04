from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.modules.auth.models import Usuario
from app.core.security import crear_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def autenticar_usuario(db: Session, correo: str, password: str):
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario or not pwd_context.verify(password, usuario.contrasena):
        return None
    return usuario

def generar_token(usuario: Usuario) -> dict:
    token = crear_token({"sub": str(usuario.id_usuario)})
    return {"access_token": token, "token_type": "bearer"}