class AccountNotFoundException(Exception):
    def __init__(self, identifiers):
        self.message = f"Account not found when searching on {identifiers}"
        super().__init__(self.message)
