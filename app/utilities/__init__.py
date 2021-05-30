from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from app.config.config import ENC_DEC_KEY
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


class LibraryUtilities:
    """
    This class contains all the standard functions
    that can be used as library utilities and common
    functionalities
    """

    @staticmethod
    def return_db_instance():
        return SQLAlchemy()

    @staticmethod
    def encrypt(data):
        """ Encrypt """
        try:
            data = str(data)
            cipher_suite = Fernet(ENC_DEC_KEY)
            res = cipher_suite.encrypt(data.encode('utf-8')).decode('utf-8')
            return res
        except Exception:
            raise

    @staticmethod
    def decrypt(data):
        """ Decrypt """
        cipher_suite = Fernet(ENC_DEC_KEY)
        try:
            decrypted_code = cipher_suite.decrypt(
                data.encode('utf-8')).decode('utf-8')
            return decrypted_code
        except Exception as e:
            return e.args

    @staticmethod
    def get_scrapped_data(job, country):
        try:
            url = 'https://www.monster.com/jobs/search/?q={0}&where={1}'.format(job, country)
            data = requests.get(url)
            web_data = BeautifulSoup(data.content, 'html.parser')
            job_not_found = web_data.find('section', class_='mux-secondary-navigation')
            jobs_message = job_not_found.find_next('h1').text.strip()
            job_elems = web_data.find_all('section', class_='card-content')
            jobs = []

            if job_elems and jobs_message != "Sorry, we didn't find any jobs matching your criteria":
                for job_elem in job_elems:
                    job_title = job_elem.find('h2', class_='title')
                    job_location = job_elem.find('div', class_='location')
                    job_company = job_elem.find('div', class_='company')
                    if job_title is not None and "Get "+job+" jobs in " + country not in job_title.text:
                        jobs.append(job_title.text.strip() + " - " + job_company.text.strip() + " : "+job_location.text.strip())
            else:
                jobs = jobs_message
            return jobs
        except Exception:
            raise

    @staticmethod
    def fb_login_selenium(username, password):
        try:
            driver = webdriver.Chrome(executable_path="app\\webdriver\\windows\\chromedriver.exe")
            url = 'https://www.facebook.com'
            driver.get(url)
            email_field = driver.find_element_by_id('email')
            password_field = driver.find_element_by_id('pass')
            email_field.send_keys(username)
            password_field.send_keys(password)
            login = driver.find_element_by_id('u_0_b')
            login.submit()
            text = driver.find_element_by_class_name('_2md').text
            if text == "Facebook":
                driver.close()
            return {"status": "true", "message": "Login Successful!!, please wait for the window to open and automatically login to the browser."}
        except Exception:
            raise

    @staticmethod
    def get_names_of_all_git_projects(email, password):
        try:
            login_url = 'https://gitlab.com/users/sign_in'
            session_requests = requests.session()
            data = session_requests.get(
                login_url
            )
            projects = []
            from lxml import html
            web_data = BeautifulSoup(data.content, 'html.parser')
            hidden_input_data = web_data.find_all("input", {'type':'hidden'})
            utf8 = hidden_input_data[0]['value']
            auth_id = hidden_input_data[1]['value']
            remember_me = hidden_input_data[2]['value']
            email_opted_in = hidden_input_data[2]['value']
            payload = {
                "user[login]": email,
                "user[password]": password,
                "authenticity_token": auth_id,
                "utf8": utf8,
                "user[remember_me]": remember_me,
                "new_user[email_opted_in]": email_opted_in
            }
            result = session_requests.post(
                login_url,
                data=payload,
                verify=False
            )
            if result.status_code == 200:
                my_projects = 'https://gitlab.com/'
                data = session_requests.get(my_projects)
                web_data = BeautifulSoup(data.content, 'html.parser')
                all_projects = web_data.find_all('ul', class_="projects-list")
                for project in all_projects:
                    projects.append(project.find("span", class_='project-name').text.strip())
                return projects
        except Exception:
            raise
