from unittest import TestCase

from commons.factories import make_tweet, make_twitter_account


class TestFactory(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_make_twitter_account(self):
        account = make_twitter_account()

    def test_make_tweet(self):
        tweet = make_tweet()
