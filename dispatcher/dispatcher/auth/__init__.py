from flask_httpauth import HTTPTokenAuth

authclass = HTTPTokenAuth(scheme='Bearer')

def get_tokens():
    return {"MYTOKEN": "DAN"}

@authclass.verify_token
def verify_token(token):
    return token in get_tokens()
