from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class Auditoria(Base):
    __tablename__ = "auditoria"
    id_auditoria = Column(Integer, primary_key=True, index=True)
    tabla = Column(String(100))
    id_registro = Column(Integer)
    accion = Column(String(50))
    usuario = Column(String(100))
    fecha = Column(TIMESTAMP, server_default=func.now())
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class Pupitre(Base):
    __tablename__ = "pupitres"
    id_mantenimiento = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    estado = Column(String(20))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class InventarioLibro(Base):
    __tablename__ = "inventario_libro"
    id_libro = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    autor = Column(String(100), nullable=False)
    id_salon = Column(Integer, ForeignKey("salon.id_salon"))
    disponible = Column(Boolean, default=True)


class PrestamoLibro(Base):
    __tablename__ = "prestamo_libro"
    id_prestamo = Column(Integer, primary_key=True, index=True)
    id_libro = Column(Integer, ForeignKey("inventario_libro.id_libro"))
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)
    estado = Column(Boolean)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
