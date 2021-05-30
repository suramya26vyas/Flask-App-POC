from . import UserData
from ..Model.model import StudentCredentials
from ..utilities import LibraryUtilities
from ..error_handlers.exceptions import InputKeywordError
from error_codes import ERROR_CODES

user_data = UserData()

db = LibraryUtilities.return_db_instance()


def validate_login_credentials(email, username, password):
    is_details_fetched = False
    student_info = {"StudentExists": is_details_fetched, "User": username}
    try:
        if password is None:
            raise InputKeywordError(status_code=ERROR_CODES.get('InputKeywordError'), message="Password is not passed")
        password = LibraryUtilities.decrypt(password)
        if email:
            student_info["User"] = email
            student_data = StudentCredentials.query.filter_by(email=email, password=password).first()
        else:
            student_data = StudentCredentials.query.filter_by(username=username, password=password).first()
        if student_data is not None:
            is_details_fetched = True
            student_info = {"StudentExists": is_details_fetched, "EmailId": student_data.email}
            user_data.email = student_data.email
        return student_info
    except Exception:
        raise
