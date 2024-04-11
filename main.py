"""
Paquetes requeridos:
    - python -m pip install fastapi
    - python -m pip install "uvicorn[standar]"
    - python -m pip install sqlalchemy

Comando iniciar servidor local:
    - uvicorn main:app --port 8081
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import controller, models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    candidatos = controller.obtener_candidatos(db, skip, limit)
    return candidatos


@app.post("/candidato")
async def crear_candidato(
    candidato: models.CandidatoCreate, db: Session = Depends(get_db)
):
    candidato_db = controller.obtener_candidato_dni(db, candidato_dni=candidato.dni)
    if candidato_db:
        raise HTTPException(status_code=400, detail="Ese candidato ya está registrado")
    return controller.insertar_candidato(db, candidato)
