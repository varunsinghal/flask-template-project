from datetime import datetime
from unittest import TestCase

from commons.factories import make_tweet_factory, make_twitter_account_factory
from commons.models import Tweet, TwitterAccount


class TestFactory(TestCase):
    def setUp(self) -> None:
        self.tweet_factory = make_tweet_factory()
        self.account_factory = make_twitter_account_factory()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_tweet_factory(self):
        tweet: Tweet = self.tweet_factory.create()
        self.assertIsNotNone(tweet.text)
        self.assertLessEqual(len(tweet.text), 80)
        self.assertLessEqual(len(tweet.hashtags), 3)
        self.assertIsNone(tweet.in_reply_to_status_id)
        self.assertIsNone(tweet.in_reply_to_user_id)
        self.assertIsNone(tweet.quoted_status_id)
        self.assertIsNone(tweet.quoted_user_id)
        self.assertIsNone(tweet.retweeted_status_id)
        self.assertIsNone(tweet.retweeted_user_id)
        self.assertIn(tweet.is_status, [True, False])
        self.assertIsNotNone(tweet.author_id)
        self.assertLessEqual(tweet.retweet_count, 9999)
        self.assertLessEqual(tweet.favorite_count, 9999)
        self.assertIsInstance(tweet.created_at, datetime)
        self.assertEqual(tweet.user_mentions, [])
        self.assertLessEqual(len(tweet.urls), 2)
        self.assertLessEqual(len(tweet.symbols), 3)

    def test_tweet_factory_with_params(self):
        (
            reply_tweet,
            quoted_tweet,
            retweet_tweet,
        ) = self.tweet_factory.create_batch(3)
        (
            author,
            reply_account,
            quoted_account,
            retweet_account,
        ) = self.account_factory.create_batch(4)
        user_mentions = self.account_factory.create_batch(2)

        tweet: Tweet = self.tweet_factory.create(
            author=author,
            reply_tweet=reply_tweet,
            quoted_tweet=quoted_tweet,
            retweet_tweet=retweet_tweet,
            reply_account=reply_account,
            quoted_account=quoted_account,
            retweet_account=retweet_account,
            users=user_mentions,
        )

        self.assertEqual(tweet.in_reply_to_status_id, reply_tweet.id)
        self.assertEqual(tweet.quoted_status_id, quoted_tweet.id)
        self.assertEqual(tweet.retweeted_status_id, retweet_tweet.id)
        self.assertEqual(tweet.in_reply_to_user_id, reply_account.id)
        self.assertEqual(tweet.quoted_user_id, quoted_account.id)
        self.assertEqual(tweet.retweeted_user_id, retweet_account.id)
        self.assertEqual(tweet.author_id, author.id)

    def test_twitter_account_factory(self):
        account: TwitterAccount = self.account_factory.create()
        self.assertIsNotNone(account.name)
        self.assertIsNotNone(account.screen_name)
        self.assertEqual(account.screen_name.count(" "), 0)
        self.assertLessEqual(account.followers_count, 999)
        self.assertGreaterEqual(account.followers_count, 10)
        self.assertLessEqual(account.following_count, 9999)
        self.assertGreaterEqual(account.following_count, 10)
        self.assertLessEqual(account.tweets_count, 999)
        self.assertGreaterEqual(account.tweets_count, 10)
        self.assertIsNotNone(account.description)
        self.assertIsInstance(account.created_at, datetime)
        self.assertIn(account.protected, [True, False])
        self.assertIn(account.private, [True, False])
        self.assertIsNotNone(account.location)
        self.assertIsNotNone(account.url)
        self.assertTrue(account.profile_image_url.startswith("https://"))
