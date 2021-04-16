import datetime
import jwt
from flask_jwt_extended import *


def generateJwt(data):
    expires = datetime.timedelta(days=1)
    expires_refresh = datetime.timedelta(days=2)
    access_token = create_access_token(data,
                                       fresh=True,
                                       expires_delta=expires)
    payload = {
        "access_token": access_token,
    }
    return payload


def verifyJwt(token):
    token = get_jwt_identity(token)
    print(token)
    return token
