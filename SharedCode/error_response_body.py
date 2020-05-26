import json

class error_response_body:

    def __init__(self, message, errors = []):
        self._success = True
        self._message = message
        self._errors = errors


    def __str__(self):
        obj = {
            'success': self._success,
            'message': self._message,
            'error': self._errors,
        }

        return json.dumps(obj)


    def add_data(self, error):
        self._errors.add(error)
