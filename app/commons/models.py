from sqlalchemy import (
    ARRAY,
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    Text,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Model = declarative_base()


class TwitterAccount(Model):
    __tablename__ = "twitteraccount"

    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    screen_name = Column(Text)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    tweets_count = Column(Integer)
    profile_image_url = Column(Text)
    description = Column(Text)
    location = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    protected = Column(Boolean)
    private = Column(Boolean)
    url = Column(Text)

    def __repr__(self):
        return f"<TwitterAccount-{self.name}>"


class Tweet(Model):
    __tablename__ = "tweet"

    id = Column(BigInteger, primary_key=True)
    text = Column(Text)
    urls = Column(ARRAY(Text))
    hashtags = Column(ARRAY(Text))
    symbols = Column(ARRAY(Text))
    user_mentions = Column(ARRAY(Text))
    in_reply_to_status_id = Column(BigInteger)
    in_reply_to_user_id = Column(BigInteger)
    quoted_status_id = Column(BigInteger)
    quoted_user_id = Column(BigInteger)
    retweeted_status_id = Column(BigInteger)
    retweeted_user_id = Column(BigInteger)
    is_status = Column(Boolean)
    author_id = Column(BigInteger)
    retweet_count = Column(Integer)
    favorite_count = Column(Integer)
    created_at = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<Tweet-{self.text}>"
