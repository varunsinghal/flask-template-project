from commons.database import get_session
from commons.exceptions import AccountNotFoundException
from commons.factories import make_tweet_factory, make_twitter_account_factory
from commons.models import Tweet, TwitterAccount
from commons.serializer import TwitterAccountSerializer
from controllers.twitteraccounts import TwitterAccountController
from tests.controllers import TestController


class TestTweetController(TestController):
    def setUp(self) -> None:
        self.session = get_session()
        self.account_factory = make_twitter_account_factory()
        self.tweet_factory = make_tweet_factory()
        self.account_controller = TwitterAccountController()
        self.serializer = TwitterAccountSerializer()

    def tearDown(self) -> None:
        self.session.query(TwitterAccount).delete()
        self.session.commit()

    def _create_account(self) -> TwitterAccount:
        account = self.account_factory.create()
        self.session.add(account)
        self.session.commit()
        return account

    def test_get_account_when_empty(self):
        account = self.account_controller.get_account(999, "id")
        self.assertIsNone(account)

    def test_get_account_by_id(self):
        expected_account = self._create_account()
        actual_account = self.account_controller.get_account(
            expected_account.id, "id"
        )
        self.assertEqual(expected_account, actual_account)

    def test_get_account_by_screen_name(self):
        expected_account = self._create_account()
        actual_account = self.account_controller.get_account(
            expected_account.screen_name, "screen_name"
        )
        self.assertEqual(expected_account, actual_account)

    def test_create_account(self):
        expected_account = self.account_factory.create()
        actual_account = self.account_controller.create_account(
            expected_account
        )
        self.assertIsNotNone(actual_account.id)
        self.assertEqual(expected_account, actual_account)

    def test_update_account(self):
        account_dict = self.serializer.dump(self._create_account())
        account_dict["description"] = "new description"
        existing_account = self.account_controller.get_account(
            account_dict["screen_name"], "screen_name"
        )
        self.assertNotEqual(
            existing_account.description, account_dict["description"]
        )
        updated_account = self.account_controller.update_account(
            self.serializer.load(account_dict)
        )
        self.assertEqual(
            updated_account.description, account_dict["description"]
        )

    def test_delete_account(self):
        account = self._create_account()
        self.session.add_all(self.tweet_factory.create_batch(5, author=account))
        self.session.commit()
        self.account_controller.delete_account(account.id, "id")
        deleted_tweets = (
            self.session.query(Tweet)
            .filter(Tweet.author_id == account.id)
            .all()
        )
        deleted_account = (
            self.session.query(TwitterAccount)
            .filter(TwitterAccount.id == account.id)
            .all()
        )
        self.assertEqual(deleted_account, [])
        self.assertEqual(deleted_tweets, [])

    def test_delete_account_not_found(self):
        with self.assertRaises(AccountNotFoundException):
            self.account_controller.delete_account(999, "id")
