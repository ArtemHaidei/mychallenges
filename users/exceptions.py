from django.core.exceptions import ObjectDoesNotExist


class UserNotFoundException(ObjectDoesNotExist):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(message)
