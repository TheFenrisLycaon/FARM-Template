from fastapi import status


class BaseException(Exception):
    """
    Base exception class for the application.
    All custom exceptions should inherit from this class.

    Args:
        status_code (int): HTTP status code for the exception.
        detail (str): Detailed error message.
    """

    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = "An unexpected error occurred.",
    ):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)
