from sqlmodel import Session


class UnitOfWork:
    """
    Gestiona el ciclo de vida de la transacción de base de datos.
    Uso en servicios:
        with UnitOfWork(session) as uow:
            uow._session.add(obj)
        # commit automático si no hay excepción
        # rollback automático si hay excepción
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self._session.commit()
        else:
            self._session.rollback()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
