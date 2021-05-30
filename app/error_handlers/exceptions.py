class FlaskPOCError(Exception):
    """
    Base Class to handle all the Exceptions Associated with this Application
    """
    pass


class InputKeywordError(FlaskPOCError):
    """
    Class to handle all the Wrong Keyword Exceptions
    """
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class DataBaseError(FlaskPOCError):
    """
    Class to handle all the Data Not Found Exceptions
    """
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
