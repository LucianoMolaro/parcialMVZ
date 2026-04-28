from typing import Optional, List
from sqlmodel import Session
from fastapi import HTTPException

from app.modules.Categoria.UnitOfWork import CategoriaUnitOfWork
from app.modules.Categoria.Schema import CategoriaCreate
from app.modules.models import Categoria


def get_all(session: Session, nombre: Optional[str], offset: int, limit: int) -> List[Categoria]:
    with CategoriaUnitOfWork(session) as uow:
        if nombre:
            return uow.categorias.get_by_nombre(nombre, offset, limit)
        return uow.categorias.get_all(offset, limit)


def get_by_id(session: Session, categoria_id: int) -> Categoria:
    with CategoriaUnitOfWork(session) as uow:
        categoria = uow.categorias.get_by_id(categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return categoria


def create(session: Session, data: CategoriaCreate) -> Categoria:
    with CategoriaUnitOfWork(session) as uow:
        nueva = Categoria(nombre=data.nombre, descripcion=data.descripcion)
        return uow.categorias.add(nueva)
    # el __exit__ hace commit automático


def update(session: Session, categoria_id: int, data: CategoriaCreate) -> Categoria:
    with CategoriaUnitOfWork(session) as uow:
        categoria = uow.categorias.get_by_id(categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        categoria.nombre = data.nombre
        categoria.descripcion = data.descripcion
        uow.categorias.add(categoria)
        return categoria


def delete(session: Session, categoria_id: int) -> None:
    with CategoriaUnitOfWork(session) as uow:
        categoria = uow.categorias.get_by_id(categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        uow.categorias.delete(categoria)
