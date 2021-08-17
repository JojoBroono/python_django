import logging


class LogUserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(filename='app.log',format='%(asctime)s - %(message)s', level=logging.INFO)

    def __call__(self, request, *args, **kwargs):
        logging.info(f"URL: {request.build_absolute_uri()}, METHOD: {request.method}")
        response = self.get_response(request)
        return response
