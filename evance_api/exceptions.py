class EvanceException(Exception):
    """Base exception for all Evance API errors."""
    def __init__(self, message=None):
        #self.default_message = 'An error has occurred.'
        if message is None:
            message = self.default_message
        super().__init__(message)

class UnauthorizedError(EvanceException):
    """Exception for 401 Unauthorized errors."""
    default_message = "Invalid credentials or token expired."

class ForbiddenError(EvanceException):
    """Exception for 403 Forbidden errors."""
    default_message = "Access to this resource is forbidden."

class NotFoundError(EvanceException):
    """Exception for 404 Not Found errors."""
    default_message = "The requested resource was not found."

class MethodNotAllowedError(EvanceException):
    """Exception for 405 Method Not Allowed errors."""
    default_message = "The HTTP method used is not allowed for this endpoint."

class ServerError(EvanceException):
    """Exception for 500+ Server errors."""
    default_message = "A server error occurred. Please try again later."

class UnexpectedError(EvanceException):
    """Exception for unexpected errors."""
    default_message = "An unexpected error occurred."
