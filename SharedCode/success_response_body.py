import json

class success_response_body:

    def __init__(self, message):
        self._success = False
        self._message = message
        self.data = None


    def __str__(self):
        obj = {
            'success': self.success,
            'message': self.message,
            'data': self.data,
        }

        return json.dumps(obj)


    def add_data(self, data):
        self.data = data
