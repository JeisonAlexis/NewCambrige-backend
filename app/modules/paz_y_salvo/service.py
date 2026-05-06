from sqlalchemy.orm import Session
from typing import Optional, List
from app.shared.models import PeriodoAcademico
from app.modules.estudiantes.models import Estudiante
from app.modules.rectoria.models import FirmasPazYSalvo

def get_firmas(db: Session, estudiante_id: int, periodo_id: Optional[int] = None) -> Optional[FirmasPazYSalvo]:
    if not periodo_id:
        periodo = db.query(PeriodoAcademico).filter(PeriodoAcademico.activo == True).first()
        if not periodo:
            return None
        periodo_id = periodo.id_periodo
    
    firmas = db.query(FirmasPazYSalvo).filter(
        FirmasPazYSalvo.id_estudiante == estudiante_id,
        FirmasPazYSalvo.id_periodo == periodo_id
    ).first()
    
    if not firmas:
        firmas = FirmasPazYSalvo(
            id_estudiante=estudiante_id,
            id_periodo=periodo_id
        )
        db.add(firmas)
        db.commit()
        db.refresh(firmas)
    
    return firmas

def get_estado_completo(db: Session, estudiante_id: int, periodo_id: Optional[int] = None) -> Optional[dict]:
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    if not estudiante:
        return None
    
    if not periodo_id:
        periodo = db.query(PeriodoAcademico).filter(PeriodoAcademico.activo == True).first()
        if not periodo:
            return None
        periodo_id = periodo.id_periodo
        periodo_nombre = f"{periodo.nombre} {periodo.anio}"
    else:
        periodo = db.query(PeriodoAcademico).filter(PeriodoAcademico.id_periodo == periodo_id).first()
        periodo_nombre = f"{periodo.nombre} {periodo.anio}" if periodo else None
    
    firmas = get_firmas(db, estudiante_id, periodo_id)
    
    firmas_dict = {
        "biblioteca": firmas.biblioteca,
        "tesoreria": firmas.tesoreria,
        "uniforme": firmas.uniforme,
        "salon": firmas.salon,
        "rectoria": firmas.rectoria
    }
    
    todas_firmadas = all(firmas_dict.values())
    
    return {
        "id_estudiante": estudiante_id,
        "nombre": estudiante.nombre,
        "id_periodo": periodo_id,
        "periodo_nombre": periodo_nombre,
        "firmas": firmas_dict,
        "todas_firmadas": todas_firmadas,
        "puede_retirarse": todas_firmadas
    }

def update_firmas(db: Session, estudiante_id: int, periodo_id: Optional[int], data: dict) -> Optional[FirmasPazYSalvo]:
    if not periodo_id:
        periodo = db.query(PeriodoAcademico).filter(PeriodoAcademico.activo == True).first()
        if not periodo:
            return None
        periodo_id = periodo.id_periodo
    
    firmas = get_firmas(db, estudiante_id, periodo_id)
    
    for key, value in data.items():
        if value is not None:
            setattr(firmas, key, value)
    
    db.commit()
    db.refresh(firmas)
    return firmas

def get_sin_firmas(db: Session, periodo_id: Optional[int] = None) -> List[dict]:
    if not periodo_id:
        periodo = db.query(PeriodoAcademico).filter(PeriodoAcademico.activo == True).first()
        if not periodo:
            return []
        periodo_id = periodo.id_periodo
    
    estudiantes = db.query(Estudiante).all()
    resultado = []
    
    for e in estudiantes:
        firmas = db.query(FirmasPazYSalvo).filter(
            FirmasPazYSalvo.id_estudiante == e.id_estudiante,
            FirmasPazYSalvo.id_periodo == periodo_id
        ).first()
        
        if not firmas:
            resultado.append({"id_estudiante": e.id_estudiante, "nombre": e.nombre, "faltan": "todas"})
        else:
            faltantes = []
            if not firmas.biblioteca: faltantes.append("biblioteca")
            if not firmas.tesoreria: faltantes.append("tesoreria")
            if not firmas.uniforme: faltantes.append("uniforme")
            if not firmas.salon: faltantes.append("salon")
            if not firmas.rectoria: faltantes.append("rectoria")
            if faltantes:
                resultado.append({"id_estudiante": e.id_estudiante, "nombre": e.nombre, "faltan": faltantes})
    
    return resultado