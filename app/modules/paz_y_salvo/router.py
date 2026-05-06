from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional, List
from app.core.database import get_db
from app.modules.paz_y_salvo import service
from app.modules.paz_y_salvo.schemas import FirmasResponse, FirmasUpdate, EstadoPazSalvoResponse
from app.modules.auth.deps import require_roles

router = APIRouter()

@router.get("/estudiante/{estudiante_id}", response_model=EstadoPazSalvoResponse)
def obtener_estado_paz_salvo(
    estudiante_id: int,
    periodo_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(require_roles(["admin", "secretaria", "tesoreria", "rectoria"]))
):
    resultado = service.get_estado_completo(db, estudiante_id, periodo_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Estudiante o periodo no encontrado")
    return resultado

@router.get("/firmas/{estudiante_id}", response_model=FirmasResponse)
def obtener_firmas(
    estudiante_id: int,
    periodo_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(require_roles(["admin", "secretaria", "tesoreria"]))
):
    firmas = service.get_firmas(db, estudiante_id, periodo_id)
    if not firmas:
        raise HTTPException(status_code=404, detail="No se encontraron firmas")
    return firmas

@router.put("/firmas/{estudiante_id}", response_model=FirmasResponse)
def actualizar_firmas(
    estudiante_id: int,
    data: FirmasUpdate,
    periodo_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(require_roles(["admin", "secretaria", "tesoreria", "rectoria"]))
):
    firmas = service.update_firmas(db, estudiante_id, periodo_id, data.model_dump(exclude_unset=True))
    if not firmas:
        raise HTTPException(status_code=404, detail="Estudiante o periodo no encontrado")
    return firmas

@router.get("/sin-firmar/periodo/{periodo_id}")
def estudiantes_sin_firmas(
    periodo_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user = Depends(require_roles(["admin", "secretaria", "rectoria"]))
):
    return service.get_sin_firmas(db, periodo_id)