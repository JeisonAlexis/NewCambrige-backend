from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class SesionUsuario(Base):
    __tablename__ = "sesion_usuario"
    id_sesion = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"))
    token = Column(String(255), nullable=False)
    fecha_inicio = Column(TIMESTAMP, server_default=func.now())
    fecha_expiracion = Column(TIMESTAMP)
    activa = Column(Boolean, default=True)
    usuario = relationship("Usuario", back_populates="sesiones")
