from typing import Optional, List
from sqlmodel import Session, select
from fastapi import HTTPException

from app.core.UnitOfWork import UnitOfWork
from app.modules.Ingrediente.Schema import IngredienteCreate
from app.modules.models import Ingrediente


def get_all(session: Session, nombre: Optional[str], offset: int, limit: int) -> List[Ingrediente]:
    with UnitOfWork(session) as uow:
        query = select(Ingrediente)
        if nombre:
            query = query.where(Ingrediente.nombre.contains(nombre))
        return uow._session.exec(query.offset(offset).limit(limit)).all()


def get_by_id(session: Session, ingrediente_id: int) -> Ingrediente:
    with UnitOfWork(session) as uow:
        ingrediente = uow._session.get(Ingrediente, ingrediente_id)
        if not ingrediente:
            raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
        return ingrediente


def create(session: Session, data: IngredienteCreate) -> Ingrediente:
    with UnitOfWork(session) as uow:
        nuevo = Ingrediente(nombre=data.nombre, unidad=data.unidad)
        uow._session.add(nuevo)
        uow._session.flush()
        return nuevo


def update(session: Session, ingrediente_id: int, data: IngredienteCreate) -> Ingrediente:
    with UnitOfWork(session) as uow:
        ingrediente = uow._session.get(Ingrediente, ingrediente_id)
        if not ingrediente:
            raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
        ingrediente.nombre = data.nombre
        ingrediente.unidad = data.unidad
        uow._session.flush()
        return ingrediente


def delete(session: Session, ingrediente_id: int) -> None:
    with UnitOfWork(session) as uow:
        ingrediente = uow._session.get(Ingrediente, ingrediente_id)
        if not ingrediente:
            raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
        uow._session.delete(ingrediente)
        uow._session.flush()
