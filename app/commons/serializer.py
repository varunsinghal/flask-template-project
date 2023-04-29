from marshmallow import EXCLUDE, Schema, fields, post_load

from commons.models import Tweet, TwitterAccount


class TweetSerializer(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    text = fields.Str()
    urls = fields.List(fields.Str())
    hashtags = fields.List(fields.Str())
    symbols = fields.List(fields.Str())
    user_mentions = fields.List(fields.Str())
    in_reply_to_status_id = fields.Int()
    in_reply_to_user_id = fields.Int()
    quoted_status_id = fields.Int()
    quoted_user_id = fields.Int()
    retweeted_status_id = fields.Int()
    retweeted_user_id = fields.Int()
    is_status = fields.Bool()
    author_id = fields.Int()
    retweet_count = fields.Int()
    favorite_count = fields.Int()
    created_at = fields.DateTime()

    @post_load
    def make_tweet(self, data, **kwargs) -> Tweet:
        return Tweet(**data)


class TwitterAccountSerializer(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    name = fields.Str()
    screen_name = fields.Str()
    followers_count = fields.Int()
    following_count = fields.Int()
    tweets_count = fields.Int()
    profile_image_url = fields.Str()
    description = fields.Str()
    location = fields.Str()
    created_at = fields.DateTime()
    protected = fields.Bool()
    private = fields.Bool()
    url = fields.Str()

    @post_load
    def make_twitter_account(self, data, **kwargs) -> TwitterAccount:
        return TwitterAccount(**data)
