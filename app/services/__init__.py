from authy.api import AuthyApiClient

authy_api = AuthyApiClient('JoLnCzcuVnv1PazcwEtAAJj1jl65QUIg')


class UserData:
    email = None
    phone = None
    country_code = None
    @staticmethod
    def get_user_id(email, phone, country_code):
        email = email
        phone = phone
        country_code = country_code
        user = authy_api.users.create(
            email=email,phone=phone, country_code=country_code)
        return user.id
