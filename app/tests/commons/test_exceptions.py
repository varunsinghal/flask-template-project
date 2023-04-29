from unittest import TestCase

from commons.exceptions import (
    AccountNotFoundException,
    DatabaseSessionNotInitialized,
)


class TestException(TestCase):
    def test_account_not_found_exception(self):
        with self.assertRaises(AccountNotFoundException) as e:
            raise AccountNotFoundException("identifier")
        self.assertEqual(
            e.exception.message,
            "Account not found when searching on identifier",
        )

    def test_database_session_not_initialized(self):
        with self.assertRaises(DatabaseSessionNotInitialized) as e:
            raise DatabaseSessionNotInitialized()
        self.assertEqual(
            e.exception.message,
            (
                "Initialize the session using "
                "`initialize_session()` before accessing."
            ),
        )
