from unittest import TestCase

from commons.factories import make_tweet_factory, make_twitter_account_factory
from commons.models import Tweet, TwitterAccount
from commons.serializer import TweetSerializer, TwitterAccountSerializer


class TestSerializer(TestCase):
    def setUp(self) -> None:
        self.tweet_factory = make_tweet_factory()
        self.account_factory = make_twitter_account_factory()

    def test_tweet_serializer(self):
        serializer = TweetSerializer()
        tweet: Tweet = self.tweet_factory.create()
        tweet_dict = serializer.dump(tweet)
        self.assertEqual(tweet.id, tweet_dict["id"])
        self.assertEqual(tweet.text, tweet_dict["text"])
        self.assertEqual(tweet.urls, tweet_dict["urls"])
        self.assertEqual(tweet.hashtags, tweet_dict["hashtags"])
        self.assertEqual(tweet.symbols, tweet_dict["symbols"])
        self.assertEqual(tweet.user_mentions, tweet_dict["user_mentions"])
        self.assertEqual(
            tweet.in_reply_to_status_id, tweet_dict["in_reply_to_status_id"]
        )
        self.assertEqual(
            tweet.in_reply_to_user_id, tweet_dict["in_reply_to_user_id"]
        )
        self.assertEqual(tweet.quoted_status_id, tweet_dict["quoted_status_id"])
        self.assertEqual(tweet.quoted_user_id, tweet_dict["quoted_user_id"])
        self.assertEqual(
            tweet.retweeted_status_id, tweet_dict["retweeted_status_id"]
        )
        self.assertEqual(
            tweet.retweeted_user_id, tweet_dict["retweeted_user_id"]
        )
        self.assertEqual(tweet.is_status, tweet_dict["is_status"])
        self.assertEqual(tweet.author_id, tweet_dict["author_id"])
        self.assertEqual(tweet.retweet_count, tweet_dict["retweet_count"])
        self.assertEqual(tweet.favorite_count, tweet_dict["favorite_count"])
        self.assertEqual(tweet.created_at.isoformat(), tweet_dict["created_at"])

    def test_twitteraccount_serializer(self):
        serializer = TwitterAccountSerializer()
        account: TwitterAccount = self.account_factory.create()
        account_dict = serializer.dump(account)
        self.assertEqual(account.id, account_dict["id"])
        self.assertEqual(account.name, account_dict["name"])
        self.assertEqual(account.screen_name, account_dict["screen_name"])
        self.assertEqual(
            account.followers_count, account_dict["followers_count"]
        )
        self.assertEqual(
            account.following_count, account_dict["following_count"]
        )
        self.assertEqual(account.tweets_count, account_dict["tweets_count"])
        self.assertEqual(
            account.profile_image_url, account_dict["profile_image_url"]
        )
        self.assertEqual(account.description, account_dict["description"])
        self.assertEqual(account.location, account_dict["location"])
        self.assertEqual(
            account.created_at.isoformat(), account_dict["created_at"]
        )
        self.assertEqual(account.protected, account_dict["protected"])
        self.assertEqual(account.private, account_dict["private"])
        self.assertEqual(account.url, account_dict["url"])
