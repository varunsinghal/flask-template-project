import logging
import os
from unittest import TestCase

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from commons.database import get_connection_uri
from commons.models import Model


class TestController(TestCase):
    @classmethod
    def setUpClass(cls):
        db_credentials = {
            "username": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "hostname": os.getenv("POSTGRES_HOSTNAME"),
            "database": "test_app",
            "port": os.getenv("POSTGRES_PORT"),
        }
        connection_uri = get_connection_uri(**db_credentials)
        engine = create_engine(connection_uri, echo=False)
        Model.metadata.create_all(engine)
        cls.session = scoped_session(sessionmaker(bind=engine))

    @classmethod
    def tearDownClass(cls) -> None:
        for tbl in reversed(Model.metadata.sorted_tables):
            try:
                cls.session.execute(text("DROP TABLE IF EXISTS " + tbl.name))
                cls.session.commit()
            except Exception:
                logging.info("Skipping %r" % tbl)
        cls.session.remove()
