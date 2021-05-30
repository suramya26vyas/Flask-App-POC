from . import UserData
from ..utilities import LibraryUtilities

user_data = UserData()

db = LibraryUtilities.return_db_instance()


def fb_login_selenium(required_job_data):
    try:
        return LibraryUtilities.fb_login_selenium(required_job_data['Username'], required_job_data['Password'])
    except Exception:
        raise
