from unittest import TestCase

from commons.factories import make_tweet_factory, make_twitter_account_factory


class TestModel(TestCase):
    def setUp(self) -> None:
        self.tweet_factory = make_tweet_factory()
        self.account_factory = make_twitter_account_factory()

    def test_tweet_model_repr(self):
        tweet = self.tweet_factory.create()
        self.assertEqual(str(tweet), f"<Tweet-{tweet.text}>")

    def test_account_model_repr(self):
        account = self.account_factory.create()
        self.assertEqual(str(account), f"<TwitterAccount-{account.name}>")
