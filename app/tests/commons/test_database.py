from unittest import TestCase
from unittest.mock import patch

from commons.database import (
    Database,
    close_session,
    get_connection_uri,
    get_engine,
    get_session,
    initialize_session,
    rollback_session,
)
from commons.exceptions import DatabaseSessionNotInitialized


class TestDatabase(TestCase):
    def setUp(self) -> None:
        self.create_engine = patch("commons.database.create_engine").start()
        self.scoped_session = patch("commons.database.scoped_session").start()
        self.addCleanup(patch.stopall)
        initialize_session("connection-uri")

    def test_get_connection_uri(self):
        actual = get_connection_uri(
            **{
                "username": "user-name",
                "password": "pass-word",
                "hostname": "host-name",
                "port": 5432,
                "database": "db-name",
            }
        )
        expected = (
            "postgresql+psycopg2://user-name:pass-word@host-name:5432/db-name"
        )
        self.assertEqual(actual, expected)

    def test_initialize_session(self):
        self.create_engine.assert_called_once_with("connection-uri", echo=True)
        self.scoped_session.assert_called_once()

    def test_rollback_session(self):
        rollback_session()
        get_session().rollback.assert_called_once()

    def test_close_session(self):
        close_session()
        get_session().remove.assert_called_once()

    def test_get_session_with_empty_session(self):
        Database.session = None
        with self.assertRaises(DatabaseSessionNotInitialized):
            get_session()

    def test_get_session(self):
        session = get_session()
        self.assertEqual(session, self.scoped_session.return_value)

    def test_get_engine(self):
        engine = get_engine()
        self.assertEqual(engine, self.create_engine.return_value)
