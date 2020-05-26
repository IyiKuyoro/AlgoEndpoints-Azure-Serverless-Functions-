import json

from .response_body import response_body

class error_response_body(response_body):

    def __inti__(self, message, errors = []):
        super().__init__(False, message)
        self.errors = errors


    def __str__(self):
        obj = {
            success: self.success,
            message: self.message,
            errors: self.errors,
        }

        return json.dumps(obj)


    def add_error(self, error):
        self.errors.add(error)
