from gongish.exceptions import HTTPInternalServerError
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from cytra.db.base import DeclarativeBase, CytraDBQuery, DBSessionProxy
from cytra.exceptions import PostgresSQLError


class DatabaseAppMixin:
    db: Session = None

    def on_end_response(self):
        super().on_end_response()
        if self.db:
            self.db.remove()

    def handle_exception(self, exc, start_response):
        if isinstance(exc, SQLAlchemyError):
            self.__logger__.exception(str(exc))
            if PostgresSQLError.validate_postgres_error(exc):
                exc = PostgresSQLError(exc)
            else:
                exc = HTTPInternalServerError()
        return super().handle_exception(exc, start_response)

    def setup(self):
        if "sqlalchemy" in self.config:
            db_config = self.config.sqlalchemy
            session_kw = dict(db_config.get("session", dict()))
            session_factory = sessionmaker(
                bind=create_engine(**db_config.engine),
                query_cls=CytraDBQuery,
                **session_kw
            )
            session = scoped_session(session_factory)
            DeclarativeBase.query = session.query_property()
            DeclarativeBase.__app__ = self
            CytraDBQuery.__app__ = self
            self.db = session
            DBSessionProxy.__cytra_session__ = session
        else:
            self.db = None
        super().setup()

    def shutdown(self):
        if self.db is not None:
            self.db.close()
            self.db.get_bind().dispose()
            DeclarativeBase.__app__ = None
            CytraDBQuery.__app__ = None
            DBSessionProxy.__cytra_session__ = None

        super().shutdown()

    def commit(self):
        try:
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
