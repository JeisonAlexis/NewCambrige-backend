from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class PeriodoAcademico(Base):
    __tablename__ = "periodo_academico"
    id_periodo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    anio = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)


class Salon(Base):
    __tablename__ = "salon"
    id_salon = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    grado = Column(Integer, nullable=False)
    grupo = Column(Integer, nullable=False)
    id_periodo = Column(Integer, ForeignKey("periodo_academico.id_periodo"))
    periodo = relationship("PeriodoAcademico")
    estudiantes = relationship("Estudiante", back_populates="salon")
