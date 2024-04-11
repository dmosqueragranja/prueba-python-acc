from pydantic import BaseModel
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class CandidatoBase(BaseModel):
    nombre: str
    apellido: str
    dni: str


class CandidatoCreate(CandidatoBase):
    pass


class CandidatoORM(Base):
    __tablename__ = "candidatos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column("Nombre", String(32), nullable=False)
    apellido: Mapped[str] = mapped_column("Apellido", String(32), nullable=False)
    dni: Mapped[int] = mapped_column("Dni", String(16), unique=True)
