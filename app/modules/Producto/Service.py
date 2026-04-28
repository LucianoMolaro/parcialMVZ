from typing import Optional, List
from sqlmodel import Session, select
from fastapi import HTTPException

from app.core.UnitOfWork import UnitOfWork
from app.modules.Producto.Schema import ProductoCreate
from app.modules.models import Producto, Categoria, Ingrediente, ProductoCategoria, ProductoIngrediente


def get_all(session: Session, nombre: Optional[str], offset: int, limit: int) -> List[Producto]:
    with UnitOfWork(session) as uow:
        query = select(Producto)
        if nombre:
            query = query.where(Producto.nombre.contains(nombre))
        productos = uow._session.exec(query.offset(offset).limit(limit)).all()
        for p in productos:
            _ = p.categorias
            _ = p.ingredientes
        return productos


def get_by_id(session: Session, producto_id: int) -> Producto:
    with UnitOfWork(session) as uow:
        producto = uow._session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        _ = producto.categorias
        _ = producto.ingredientes
        return producto


def create(session: Session, data: ProductoCreate) -> Producto:
    with UnitOfWork(session) as uow:
        producto = Producto(nombre=data.nombre, precio=data.precio, descripcion=data.descripcion)
        uow._session.add(producto)
        uow._session.flush()  # obtenemos el ID sin cerrar la transacción

        for cat_id in data.categoria_ids:
            if not uow._session.get(Categoria, cat_id):
                raise HTTPException(status_code=404, detail=f"Categoría {cat_id} no encontrada")
            uow._session.add(ProductoCategoria(producto_id=producto.id, categoria_id=cat_id))

        for ing_id in data.ingrediente_ids:
            if not uow._session.get(Ingrediente, ing_id):
                raise HTTPException(status_code=404, detail=f"Ingrediente {ing_id} no encontrado")
            uow._session.add(ProductoIngrediente(producto_id=producto.id, ingrediente_id=ing_id))

        uow._session.flush()
        _ = producto.categorias
        _ = producto.ingredientes
        return producto
        # __exit__ hace commit automático


def update(session: Session, producto_id: int, data: ProductoCreate) -> Producto:
    with UnitOfWork(session) as uow:
        producto = uow._session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        producto.nombre = data.nombre
        producto.precio = data.precio
        producto.descripcion = data.descripcion

        for link in uow._session.exec(select(ProductoCategoria).where(ProductoCategoria.producto_id == producto_id)).all():
            uow._session.delete(link)
        for link in uow._session.exec(select(ProductoIngrediente).where(ProductoIngrediente.producto_id == producto_id)).all():
            uow._session.delete(link)

        uow._session.flush()

        for cat_id in data.categoria_ids:
            uow._session.add(ProductoCategoria(producto_id=producto.id, categoria_id=cat_id))
        for ing_id in data.ingrediente_ids:
            uow._session.add(ProductoIngrediente(producto_id=producto.id, ingrediente_id=ing_id))

        uow._session.flush()
        _ = producto.categorias
        _ = producto.ingredientes
        return producto


def delete(session: Session, producto_id: int) -> None:
    with UnitOfWork(session) as uow:
        producto = uow._session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        uow._session.delete(producto)
        uow._session.flush()
