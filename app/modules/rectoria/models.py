from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class TipoPrueba(Base):
    __tablename__ = "tipo_prueba"
    id_tipo_prueba = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    grado_min = Column(Integer)
    grado_max = Column(Integer)


class Prueba(Base):
    __tablename__ = "prueba"
    id_prueba = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    id_tipo_prueba = Column(Integer, ForeignKey("tipo_prueba.id_tipo_prueba"))
    estado = Column(String(20))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    estudiante = relationship("Estudiante")
    tipo_prueba = relationship("TipoPrueba")
