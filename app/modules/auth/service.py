from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.modules.usuarios.models import Usuario, RolUsuario, Rol
from app.modules.auth.models import SesionUsuario
from app.core.security import crear_token
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_contra(contra: str):
    return pwd_context.hash(contra)

def autenticar_usuario(db: Session, nombre: str, password: str):
    usuario = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if not usuario or not pwd_context.verify(password, usuario.contrasena):
        return None
    return usuario

def crear_usuario(db: Session, nombre: str, contra: str, roles: list = None):
    existente = db.query(Usuario).filter(Usuario.nombre == nombre).first()
    if existente:
        return None

    nuevo = Usuario(
        nombre=nombre,
        contrasena=hash_contra(contra)
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    if not roles:
        roles = ["none"]
    for rol_nombre in roles:
        rol = db.query(Rol).filter(Rol.nombre == rol_nombre).first()
        if rol:
            db.add(RolUsuario(
                id_usuario=nuevo.id_usuario,
                id_rol=rol.id_rol
            ))
    db.commit()
    return nuevo


def generar_token(db: Session, usuario: Usuario) -> dict:
    roles_db = (
        db.query(Rol.nombre)
        .join(RolUsuario, Rol.id_rol == RolUsuario.id_rol)
        .filter(RolUsuario.id_usuario == usuario.id_usuario)
        .all()
    )

    roles = [r[0] for r in roles_db]  # convertir a lista simple
    token = crear_token({
        "sub": str(usuario.id_usuario),
        "roles": roles
    })

    # buscar sesion activa
    sesion = db.query(SesionUsuario).filter(
        SesionUsuario.id_usuario == usuario.id_usuario,
        SesionUsuario.activa == True
    ).first()

    if sesion:
        sesion.token = token
        sesion.fecha_inicio = datetime.utcnow()
        sesion.fecha_expiracion = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    else:
        sesion = SesionUsuario(
            id_usuario=usuario.id_usuario,
            token=token,
            fecha_expiracion=datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            ),
            activa=True
        )
        db.add(sesion)

    db.commit()

    return {
        "access_token": token,
        "token_type": "bearer"
    }