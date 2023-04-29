import logging
import os
from unittest import TestCase

from sqlalchemy import text

from commons.database import (
    close_session,
    get_connection_uri,
    get_engine,
    get_session,
    initialize_session,
)
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
        initialize_session(connection_uri, echo=False)
        Model.metadata.create_all(get_engine())

    @classmethod
    def tearDownClass(cls) -> None:
        session = get_session()
        for tbl in reversed(Model.metadata.sorted_tables):
            try:
                session.execute(text("DROP TABLE IF EXISTS " + tbl.name))
                session.commit()
            except Exception:
                logging.info("Skipping %r" % tbl)
        close_session()
