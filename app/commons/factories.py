from commons.factories_impl import TweetFactory, TwitterAccountFactory
from commons.models import Tweet, TwitterAccount


def make_tweet(
    *,
    author=None,
    reply_tweet=None,
    reply_account=None,
    quoted_tweet=None,
    quoted_account=None,
    retweet_tweet=None,
    retweet_account=None,
    users=[],
    **kwargs
) -> Tweet:
    if not author:
        author = make_twitter_account()
    return TweetFactory(
        author=author,
        reply_tweet=reply_tweet,
        reply_account=reply_account,
        quoted_tweet=quoted_tweet,
        quoted_account=quoted_account,
        retweet_tweet=retweet_tweet,
        retweet_account=retweet_account,
        users=users,
        **kwargs
    )


def make_twitter_account(**kwargs) -> TwitterAccount:
    return TwitterAccountFactory(**kwargs)
