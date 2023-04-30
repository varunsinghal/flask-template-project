import logging

from commons.factories import make_tweet_factory, make_twitter_account_factory
from commons.serializer import TweetSerializer
from controllers.tweets import TweetController
from tests.controllers import TestController


class TestTweetController(TestController):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        account_factory = make_twitter_account_factory()
        tweet_factory = make_tweet_factory()
        cls.account, cls.other_account = account_factory.create_batch(2)
        cls.tweets = tweet_factory.create_batch(5, author=cls.account)
        cls.other_tweets = tweet_factory.create_batch(
            20, author=cls.other_account
        )
        cls.session.add_all(
            (
                [
                    cls.account,
                    cls.other_account,
                ]
                + cls.tweets
                + cls.other_tweets
            )
        )
        cls.session.commit()

    def setUp(self) -> None:
        self.log = logging.getLogger(__class__.__name__)
        self.tweet_controller = TweetController(self.session)
        self.serializer = TweetSerializer()

    def test_get_tweet(self):
        expected_tweet = self.tweets[0]
        expected_tweet_dict = self.serializer.dump(expected_tweet)
        actual_tweet = self.tweet_controller.get_tweet(expected_tweet.id)
        self.assertEqual(
            self.serializer.dump(actual_tweet), expected_tweet_dict
        )

    def test_get_account_tweets(self):
        tweets = self.tweet_controller.get_account_tweets(
            self.account.screen_name, "screen_name"
        )
        self.assertEqual(tweets, self.tweets)

    def test_top_tweets(self):
        tweets = self.tweet_controller.get_top_tweets()
        actual_favorites = [tweet.favorite_count for tweet in tweets]
        self.assertEqual(
            actual_favorites, sorted(actual_favorites, reverse=True)
        )
        self.assertLessEqual(len(tweets), 20)

    def test_get_account_top_tweets(self):
        tweets = self.tweet_controller.get_account_top_tweets(
            self.other_account.id, "id"
        )
        actual_favorites = [tweet.favorite_count for tweet in tweets]
        self.assertEqual(
            actual_favorites, sorted(actual_favorites, reverse=True)
        )
        self.assertLessEqual(len(tweets), 10)
