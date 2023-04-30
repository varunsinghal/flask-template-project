from flask import Blueprint, request

from commons.cache import ttl_cache
from commons.enums import IdentifierTypeEnum
from commons.serializer import TweetSerializer
from controllers.tweets import TweetController

tweets = Blueprint("tweets", __name__)
tweet_controllers = TweetController()
tweet_serializer = TweetSerializer()


@tweets.route("/<string:id>", methods=["GET"])
@ttl_cache
def get_tweet(id: str):
    """
    id: the int64 tweet id
    """
    tweet = tweet_controllers.get_tweet(id)
    return tweet_serializer.dump(tweet)


@tweets.route("/account/<string:identifier>", methods=["GET"])
def get_account_tweets(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = IdentifierTypeEnum(
        request.args.get("identifier_type")
    ).value
    tweets = tweet_controllers.get_account_tweets(identifier, identifier_type)
    return tweet_serializer.dump(tweets, many=True)


@tweets.route("/top", methods=["GET"])
def get_top_tweets():
    """ """
    tweets = tweet_controllers.get_top_tweets()
    return tweet_serializer.dump(tweets, many=True)


@tweets.route("/account/top/<string:identifier>", methods=["GET"])
def get_top_account_tweets(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = IdentifierTypeEnum(
        request.args.get("identifier_type")
    ).value
    tweets = tweet_controllers.get_account_top_tweets(
        identifier, identifier_type
    )
    return tweet_serializer.dump(tweets, many=True)
