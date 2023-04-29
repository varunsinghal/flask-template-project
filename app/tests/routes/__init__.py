from unittest import TestCase

from app import create_app


class TestRoutes(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app = create_app(
            {
                "TESTING": True,
                "DEBUG": True,
                "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            }
        )
        cls.headers = {}
        cls.client = app.test_client()

    @classmethod
    def tearDown(cls) -> None:
        pass
