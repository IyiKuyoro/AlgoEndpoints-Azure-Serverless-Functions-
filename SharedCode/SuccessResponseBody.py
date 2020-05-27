import json

class SuccessResponseBody:

    def __init__(self, message):
        self._success = False
        self._message = message
        self._data = None


    def __str__(self):
        obj = {
            'success': self._success,
            'message': self._message,
            'data': self._data,
        }

        return json.dumps(obj)


    def add_data(self, data):
        self._data = data
