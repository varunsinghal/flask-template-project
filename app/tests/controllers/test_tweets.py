from commons.factories import make_tweet, make_twitter_account
from commons.serializer import TweetSerializer
from controllers.tweets import TweetController
from tests.controllers import TestController


class TestTweetController(TestController):

    def setUp(self) -> None:
        self.tweet_controller = TweetController()
        self.serializer = TweetSerializer()
        self.account = make_twitter_account()
        self.other_account = make_twitter_account()
        self.tweets = [make_tweet(author=self.account) for _ in range(5)]
        self.other_tweets = [
            make_tweet(author=self.other_account) for _ in range(20)
        ]
        self.tweet_controller.session.add_all(
            (
                [
                    self.account,
                    self.other_account,
                ]
                + self.tweets
                + self.other_tweets
            )
        )
        self.tweet_controller.session.commit()

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
