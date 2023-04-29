from typing import Dict, List
from unittest.mock import patch

from commons.factories import make_tweet_factory
from commons.models import Tweet
from commons.serializer import TweetSerializer
from tests.routes import TestRoutes


class TestTweetsRoutes(TestRoutes):
    def setUp(self) -> None:
        self.tweet_factory = make_tweet_factory()
        self.serializer = TweetSerializer()
        self.tweet_controllers = patch(
            "routes.tweets.tweet_controllers", spec=True
        ).start()
        self.addCleanup(patch.stopall)

    def _compare_tweet_with_dict(
        self, tweets: List[Tweet], tweets_dict: List[Dict]
    ):
        for index, tweet in enumerate(tweets):
            self.assertEqual(tweets_dict[index], self.serializer.dump(tweet))

    def test_get_tweet(self):
        tweet: Tweet = self.tweet_factory.create()
        self.tweet_controllers.get_tweet.return_value = tweet
        tweet_dict = self.client.get("/tweets/123").json
        self._compare_tweet_with_dict(
            [
                tweet,
            ],
            [
                tweet_dict,
            ],
        )

    def test_get_account_tweets(self):
        tweets: List[Tweet] = self.tweet_factory.create_batch(4)
        self.tweet_controllers.get_account_tweets.return_value = tweets
        tweets_dict = self.client.get(
            "/tweets/account/123", query_string={"identifier_type": "id"}
        ).json
        self.assertEqual(len(tweets_dict), len(tweets))
        self._compare_tweet_with_dict(tweets, tweets_dict)

    def test_get_top_tweets(self):
        tweets: List[Tweet] = self.tweet_factory.create_batch(10)
        self.tweet_controllers.get_top_tweets.return_value = tweets
        tweets_dict = self.client.get("/tweets/top/").json
        self.assertEqual(len(tweets_dict), len(tweets))
        self._compare_tweet_with_dict(tweets, tweets_dict)

    def test_get_top_account_tweets(self):
        tweets: List[Tweet] = self.tweet_factory.create_batch(10)
        self.tweet_controllers.get_account_top_tweets.return_value = tweets
        tweets_dict = self.client.get(
            "/tweets/account/top/123", query_string={"identifier_type": "id"}
        ).json
        self.assertEqual(len(tweets_dict), len(tweets))
        self._compare_tweet_with_dict(tweets, tweets_dict)
