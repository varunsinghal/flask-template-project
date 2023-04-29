from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from commons.exceptions import DatabaseSessionNotInitialized

DATABASE_URI = (
    "postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}"
)


class Database:
    engine: Engine = None
    session: Session = None


def get_engine() -> Engine:
    return Database.engine


def get_session() -> Session:
    if not Database.session:
        raise DatabaseSessionNotInitialized()
    return Database.session


def get_connection_uri(**db_credentials):
    return DATABASE_URI.format(**db_credentials)


def initialize_session(connection_uri: str, echo: bool = True):
    Database.engine = create_engine(connection_uri, echo=echo)
    Database.session = scoped_session(sessionmaker(bind=Database.engine))


def rollback_session():
    Database.session.rollback()


def close_session():
    Database.session.remove()
