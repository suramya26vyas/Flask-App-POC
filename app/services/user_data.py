from . import UserData
from ..Model.model import StudentsData, Students, StudentCredentials
from ..utilities import LibraryUtilities
from ..error_handlers.exceptions import DataBaseError
from error_codes import ERROR_CODES

user_data = UserData()

db = LibraryUtilities.return_db_instance()


def get_user_data(email, phone, country_code):
    user_data.email = email
    user_data.phone = phone
    user_data.country_code = country_code
    try:
        student_data = StudentsData.query.filter_by(email=user_data.email).first()
        if student_data is None:
            raise DataBaseError(status_code=ERROR_CODES.get('DataBaseError'), message="Data with Email Id: "+email+" doesn't exists.")
        else:
            is_details_fetched = True
            student_info = {"DetailsFetched": is_details_fetched, "StudentName": student_data.name}
            return student_info
    except Exception:
        raise


def create_user(email, phone, username, password, name, lastname):
    try:
        student_data = StudentsData.query.join(StudentsData.EmailIDRel).filter(StudentsData.email == email).all()
        if student_data:
            raise DataBaseError(status_code=ERROR_CODES.get('DataBaseError'),
                                message="Student with email id " + email + " already exists and cannot be added")
        student = Students(name=name, lastname=lastname)
        student_data = StudentsData(name=name, email=email, PhoneNumber=phone)
        student_credentials = StudentCredentials(email=email, username=username, password=password)
        db.session.add(student_data)
        db.session.add(student)
        db.session.add(student_credentials)
        db.session.commit()
        is_details_fetched = True
        return {"Created": is_details_fetched}
    except Exception:
        raise
