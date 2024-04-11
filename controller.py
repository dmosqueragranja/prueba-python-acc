from sqlalchemy.orm import Session

import models


def obtener_candidato_dni(db: Session, candidato_dni: str):
    return (
        db.query(models.CandidatoORM)
        .filter(models.CandidatoORM.dni == candidato_dni)
        .first()
    )


def obtener_candidatos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CandidatoORM).offset(skip).limit(limit).all()


def insertar_candidato(db: Session, candidato: models.CandidatoCreate):
    nuevo_candidato = models.CandidatoORM(
        nombre=candidato.nombre, apellido=candidato.apellido, dni=candidato.dni
    )
    db.add(nuevo_candidato)
    db.commit()
    db.refresh(nuevo_candidato)
    return nuevo_candidato
