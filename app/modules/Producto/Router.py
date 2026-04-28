from typing import Annotated, List, Optional
from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.core.Database import get_session
from app.modules.Producto.Schema import ProductoCreate, ProductoRead
from app.modules.Producto import Service as producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=List[ProductoRead])
def listar_productos(
    session: Session = Depends(get_session),
    nombre: Annotated[Optional[str], Query(min_length=1)] = None,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 10,
):
    return producto_service.get_all(session, nombre, offset, limit)


@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, session: Session = Depends(get_session)):
    return producto_service.get_by_id(session, producto_id)


@router.post("/", response_model=ProductoRead, status_code=201)
def crear_producto(datos: ProductoCreate, session: Session = Depends(get_session)):
    return producto_service.create(session, datos)


@router.put("/{producto_id}", response_model=ProductoRead)
def editar_producto(producto_id: int, datos: ProductoCreate, session: Session = Depends(get_session)):
    return producto_service.update(session, producto_id, datos)


@router.delete("/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int, session: Session = Depends(get_session)):
    producto_service.delete(session, producto_id)
