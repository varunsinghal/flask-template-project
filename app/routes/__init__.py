from flask import request

from app import app
from controllers.twitteraccounts import get_account, create_account, update_account, delete_account
from controllers import tweets as tweet_controllers


@app.route('/twitteraccount/:identifier', methods=["GET", "DELETE"])
def get_delete_twitter_account(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = request.args.get("identifier_type")
    if request.method == "GET":
        return get_account(identifier, identifier_type)
    elif request.method == "DELETE":
        return delete_account(identifier, identifier_type)


@app.route('/twitteraccount', methods=['POST', 'PUT'])
def add_modify_twitter_accounts():
    body = request.get_json(force=True)
    if request.method == "POST":
        return create_account(body)
    elif request.method == "PUT":
        return update_account(body)


@app.route('/tweets/:id', methods=['GET'])
def get_tweet(id: str):
    """
    id: the int64 tweet id
    """
    return tweet_controllers.get_tweet(id)


@app.route('/tweets/account/:identifier', methods=['GET'])
def get_account_tweets(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = request.args.get("identifier_type")
    return tweet_controllers.get_account_tweets(identifier, identifier_type)


@app.route('/tweets/top', methods=['GET'])
def get_top_tweets():
    """
    
    """
    return tweet_controllers.get_top_tweets()

@app.route('/tweets/account/top/:identifier', methods=['GET'])
def get_top_account_tweets(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = request.args.get("identifier_type")
    return tweet_controllers.get_account_top_tweets(identifier, identifier_type)