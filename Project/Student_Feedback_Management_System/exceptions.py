# exceptions.py

class DatabaseConnectionError(Exception):
    pass

class DuplicateFeedbackError(Exception):
    pass

class FileHandlingError(Exception):
    pass

class AuthenticationError(Exception):
    pass
