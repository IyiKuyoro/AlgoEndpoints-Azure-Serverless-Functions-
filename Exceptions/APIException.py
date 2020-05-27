class APIException(Exception):

    def __init__(self, message, errors=[], code=500):
        super(APIException, self).__init__(message)
        self.errors = errors
        self.code = code

    def add_error(error):
        self.errors.append(error)

