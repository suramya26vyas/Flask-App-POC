from . import UserData, authy_api

otp = UserData()


def send_otp(email, phone, country_code):
    otp.email = email
    otp.phone = phone
    otp.country_code = country_code
    try:
        sms = authy_api.users.request_sms(otp.get_user_id(otp.email,otp.phone,otp.country_code), options={'force': True})
        if sms.ok():
            return {"otp_sent": "true", "mobile_number": phone}
        else:
            print(sms.errors())
    except Exception:
        raise


def verification(one_time_pass):
    try:
        is_verified = False
        verification = authy_api.tokens.verify(otp.get_user_id(otp.email, otp.phone, otp.country_code), token=one_time_pass, options={'force': True})
        if verification.ok():
            is_verified = True
        return {"verified": is_verified}
    except Exception:
        raise


