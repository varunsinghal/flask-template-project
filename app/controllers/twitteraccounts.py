from commons.exceptions import AccountNotFoundException
from commons.models import Tweet, TwitterAccount
from controllers import Controller


class TwitterAccountController(Controller):
    def get_account(
        self, identifier: str, identifier_type: str
    ) -> TwitterAccount:
        """
        Gets the account with the specified account id or screen name
        """
        return (
            self.session.query(TwitterAccount)
            .filter_by(**{identifier_type: identifier})
            .one_or_none()
        )

    def create_account(self, data: TwitterAccount) -> TwitterAccount:
        """
        Creates an account from the given data
        """
        self.session.add(data)
        self.session.commit()
        return data

    def update_account(self, data: TwitterAccount) -> TwitterAccount:
        """
        Updates a twitter account's details
        """
        self.session.merge(data)
        self.session.commit()
        return data

    def delete_account(self, identifier: str, identifier_type: str) -> None:
        """
        Deletes an account from the database
        """
        identifiers = {identifier_type: identifier}
        account: TwitterAccount = (
            self.session.query(TwitterAccount)
            .filter_by(**identifiers)
            .one_or_none()
        )
        if not account:
            raise AccountNotFoundException(identifiers)
        # delete the tweets made by the account
        (
            self.session.query(Tweet)
            .filter(Tweet.author_id == account.id)
            .delete()
        )
        # delete the twitter account
        self.session.delete(account)
        self.session.commit()
        return {}
