from unittest.mock import patch

from commons.factories import make_twitter_account_factory
from commons.models import TwitterAccount
from commons.serializer import TwitterAccountSerializer
from tests.routes import TestRoutes


class TestTwitterAccountRoutes(TestRoutes):
    def setUp(self) -> None:
        self.account_factory = make_twitter_account_factory()
        self.serializer = TwitterAccountSerializer()
        self.account_controller = patch(
            "routes.twitteraccounts.account_controller", spec=True
        ).start()
        self.addCleanup(patch.stopall)

    def test_create_account(self):
        account: TwitterAccount = self.account_factory.create()
        account_dict = self.serializer.dump(account)
        self.account_controller.create_account.return_value = account
        actual_account_dict = self.client.post(
            "/twitteraccount/", json=account_dict
        ).json
        self.assertEqual(account_dict, actual_account_dict)

    def test_update_account(self):
        account: TwitterAccount = self.account_factory.create()
        account_dict = self.serializer.dump(account)
        self.account_controller.update_account.return_value = account
        actual_account_dict = self.client.put(
            "/twitteraccount/", json=account_dict
        ).json
        self.assertEqual(account_dict, actual_account_dict)

    def test_get_account(self):
        account: TwitterAccount = self.account_factory.create()
        account_dict = self.serializer.dump(account)
        self.account_controller.get_account.return_value = account
        actual_account_dict = self.client.get(
            "/twitteraccount/123", query_string={"identifier_type": "id"}
        ).json
        self.assertEqual(account_dict, actual_account_dict)

    def test_delete_account(self):
        self.account_controller.delete_account.return_value = {}
        response = self.client.delete(
            "/twitteraccount/123", query_string={"identifier_type": "id"}
        ).json
        self.assertEqual(response, {})
