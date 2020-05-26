import logging
import azure.functions as func

from ..SharedCode.error_response_body import error_response_body

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        res = error_response_body('Error occurred')
        return func.HttpResponse(
            str(res),
            status_code=400
        )
