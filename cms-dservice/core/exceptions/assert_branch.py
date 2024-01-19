class AssertBranchError(Exception):

    def __init__(self, statement, message):
        self.statement = statement
        self.message = message
