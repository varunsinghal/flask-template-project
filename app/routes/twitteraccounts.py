from flask import Blueprint, request

from commons.enums import IdentifierTypeEnum
from commons.serializer import TwitterAccountSerializer
from controllers.twitteraccounts import TwitterAccountController

twitteraccount = Blueprint("twitteraccount", __name__)
account_controller = TwitterAccountController()
account_serializer = TwitterAccountSerializer()


@twitteraccount.route("", methods=["POST", "PUT"])
def add_modify_twitter_accounts():
    body = request.get_json(force=True)
    serialized_body = account_serializer.load(body)
    if request.method == "POST":
        account = account_controller.create_account(serialized_body)
    elif request.method == "PUT":
        account = account_controller.update_account(serialized_body)
    return account_serializer.dump(account)


@twitteraccount.route("/<string:identifier>", methods=["GET", "DELETE"])
def get_delete_twitter_account(identifier: str):
    """
    identifier: a str which could represent a screen_name or an id

    query params:
    identifier_type: Union['id','screen_name']
    """
    identifier_type = IdentifierTypeEnum(
        request.args.get("identifier_type")
    ).value
    if request.method == "GET":
        account = account_controller.get_account(identifier, identifier_type)
        return account_serializer.dump(account)
    elif request.method == "DELETE":
        return account_controller.delete_account(identifier, identifier_type)
