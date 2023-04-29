from datetime import datetime
from typing import List

import factory
import factory.fuzzy
from faker import Faker

from commons.models import Tweet, TwitterAccount


def make_tweet_factory() -> factory.Factory:
    class _TweetFactory(factory.Factory):
        class Meta:
            model = Tweet

        class Params:
            url_count = factory.Faker("random_int", max=2)
            symbol_count = factory.Faker("random_int", max=3)
            author = make_twitter_account_factory().create()
            reply_tweet: Tweet = None
            reply_account: TwitterAccount = None
            quoted_tweet: Tweet = None
            quoted_account: TwitterAccount = None
            retweet_tweet: Tweet = None
            retweet_account: TwitterAccount = None
            users: List[TwitterAccount] = []

        id = factory.Sequence(lambda n: n + 1)
        text = factory.Faker("text", max_nb_chars=80)
        hashtags = factory.Faker("words", nb=3)
        in_reply_to_status_id = factory.LazyAttribute(
            lambda o: o.reply_tweet.id if o.reply_tweet else None
        )
        in_reply_to_user_id = factory.LazyAttribute(
            lambda o: o.reply_account.id if o.reply_account else None
        )
        quoted_status_id = factory.LazyAttribute(
            lambda o: o.quoted_tweet.id if o.quoted_tweet else None
        )
        quoted_user_id = factory.LazyAttribute(
            lambda o: o.quoted_account.id if o.quoted_account else None
        )
        retweeted_status_id = factory.LazyAttribute(
            lambda o: o.retweet_tweet.id if o.retweet_tweet else None
        )
        retweeted_user_id = factory.LazyAttribute(
            lambda o: o.retweet_account.id if o.retweet_account else None
        )
        is_status = factory.fuzzy.FuzzyChoice([True, False])
        author_id = factory.LazyAttribute(lambda o: o.author.id)
        retweet_count = factory.fuzzy.FuzzyInteger(low=10, high=9999)
        favorite_count = factory.fuzzy.FuzzyInteger(low=10, high=9999)
        created_at = factory.LazyFunction(datetime.now)

        @factory.lazy_attribute
        def user_mentions(self):
            _user_ids = []
            for user in self.users:
                _user_ids.append(user.id)
            return _user_ids

        @factory.lazy_attribute
        def urls(self):
            _urls = []
            for _ in range(self.url_count):
                _urls.append(Faker().uri())
            return _urls

        @factory.lazy_attribute
        def symbols(self):
            _symbols = []
            for _ in range(self.symbol_count):
                _symbols.append(Faker().lexify(text="????"))
            return _symbols

    return _TweetFactory


def make_twitter_account_factory() -> factory.Factory:
    class _TwitterAccountFactory(factory.Factory):
        class Meta:
            model = TwitterAccount

        class Params:
            city = factory.Faker("city")
            country = factory.Faker("country")

        id = factory.Sequence(lambda n: n + 1)
        name = factory.Faker("name")
        screen_name = factory.LazyAttribute(
            lambda o: "".join(o.name.split(" "))
        )
        followers_count = factory.fuzzy.FuzzyInteger(low=10, high=999)
        following_count = factory.fuzzy.FuzzyInteger(low=10, high=9999)
        tweets_count = factory.fuzzy.FuzzyInteger(low=10, high=999)
        description = factory.Faker("sentence", nb_words=10)
        created_at = factory.LazyFunction(datetime.now)
        protected = factory.fuzzy.FuzzyChoice([True, False])
        private = factory.fuzzy.FuzzyChoice([True, False])
        location = factory.LazyAttribute(lambda o: o.city + ", " + o.country)
        url = factory.Faker("lexify", text="https://t.co/??????????")
        profile_image_url = factory.Faker(
            "numerify", text="https://pbs.twimg.com/profile_images/%##########"
        )

    return _TwitterAccountFactory
