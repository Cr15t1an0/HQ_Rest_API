from rest_framework.response import Response


class ApiException(Exception):
    def __init__(self, http_code, error_code, message):
        self.http_code = http_code
        self.error_code = error_code
        self.message = message
        self.response = Response(
            data={
                "error_code": self.error_code,
                "message": self.message
            },
            status=http_code
        )