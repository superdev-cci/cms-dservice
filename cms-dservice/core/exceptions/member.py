class MemberHasChild(Exception):

    def __init__(self, statement, message):
        self.statement = statement
        self.message = message


class IdCardError(Exception):

    def __init__(self, statement, message):
        self.statement = statement
        self.message = message


class MemberIsExist(Exception):

    def __init__(self, statement, message):
        self.statement = statement
        self.message = message
