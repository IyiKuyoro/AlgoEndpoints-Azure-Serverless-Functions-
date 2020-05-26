import json

from .response_body import response_body

class success_response_body(response_body):

    def __init__(self, message):
        super().__init__(True, message)
        self.data = None


    def __str__(self):
        obj = {
            success: self.success,
            message: self.message,
            data: self.data,
        }

        return json.dumps(obj)


    def add_data(self, data):
        self.data = data
