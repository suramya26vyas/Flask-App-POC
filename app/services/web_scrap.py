from . import UserData
from ..utilities import LibraryUtilities

user_data = UserData()

db = LibraryUtilities.return_db_instance()


def get_webscrap_data(required_job_data):
    try:
        job = required_job_data.get('Job')
        country = required_job_data.get('Country',"")
        return LibraryUtilities.get_scrapped_data(job, country)
    except Exception:
        raise


def get_names_of_all_git_projects(required_job_data):
    try:
        email = required_job_data.get('Email')
        password = required_job_data.get('Password')
        return {"email": email, "projects": LibraryUtilities.get_names_of_all_git_projects(email, password)}
    except Exception:
        raise