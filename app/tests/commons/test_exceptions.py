from unittest import TestCase

from commons.exceptions import AccountNotFoundException


class TestException(TestCase):
    def test_account_not_found_exception(self):
        with self.assertRaises(AccountNotFoundException) as e:
            raise AccountNotFoundException("identifier")
        self.assertEqual(
            e.exception.message,
            "Account not found when searching on identifier",
        )
