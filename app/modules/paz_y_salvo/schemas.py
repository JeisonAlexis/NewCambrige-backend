from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FirmasBase(BaseModel):
    biblioteca: bool = False
    tesoreria: bool = False
    uniforme: bool = False
    salon: bool = False
    rectoria: bool = False

class FirmasUpdate(BaseModel):
    biblioteca: Optional[bool] = None
    tesoreria: Optional[bool] = None
    uniforme: Optional[bool] = None
    salon: Optional[bool] = None
    rectoria: Optional[bool] = None

class FirmasResponse(FirmasBase):
    id_firma: int
    id_estudiante: int
    id_periodo: int
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class EstadoPazSalvoResponse(BaseModel):
    id_estudiante: int
    nombre: str
    id_periodo: int
    periodo_nombre: Optional[str] = None
    firmas: FirmasBase
    todas_firmadas: bool
    puede_retirarse: bool