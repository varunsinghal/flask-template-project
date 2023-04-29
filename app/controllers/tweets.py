from typing import List

from commons.models import Tweet, TwitterAccount
from controllers import Controller


class TweetController(Controller):
    def get_tweet(self, id) -> Tweet:
        """
        Gets the tweet details with the given id
        """
        return self.session.query(Tweet).filter(Tweet.id == id).one_or_none()

    def get_account_tweets(self, identifier, identifier_type) -> List[Tweet]:
        """
        Gets the tweets for a given account
        """
        account: TwitterAccount = (
            self.session.query(TwitterAccount)
            .filter_by(**{identifier_type: identifier})
            .one_or_none()
        )
        return (
            self.session.query(Tweet)
            .filter(Tweet.author_id == account.id)
            .all()
        )

    def get_top_tweets(self) -> List[Tweet]:
        """
        Gets the top 10 tweets by favourite count
        """
        return (
            self.session.query(Tweet)
            .order_by(Tweet.favorite_count.desc())
            .limit(20)
            .all()
        )

    def get_account_top_tweets(
        self, identifier, identifier_type
    ) -> List[Tweet]:
        """
        Gets the top 10 tweets by favourite count for a given twitter account
        """
        account: TwitterAccount = (
            self.session.query(TwitterAccount)
            .filter_by(**{identifier_type: identifier})
            .one_or_none()
        )
        return (
            self.session.query(Tweet)
            .filter(Tweet.author_id == account.id)
            .order_by(Tweet.favorite_count.desc())
            .limit(10)
            .all()
        )
