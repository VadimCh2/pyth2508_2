import jwt
import datetime

JWT_SECRET = 'dkfghkdfjhgldkshgklhdfsgd6fg56df5g6df5g6df56g5df65g5fdg5dg56df56gdf65'
WRONG_SECRET = 'this-is-a-completely-different-secret-key-12345'

payload = {
    "sub": '2011',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=600),
    "surname": 'Chernyakov',
    "group": 'IPZ-21',
    "subject": 'Web Programming'
}

encode_jwt = jwt.encode(
    payload=payload,
    key=JWT_SECRET,
    algorithm='HS256'
)
print(encode_jwt)

decode = jwt.decode(
    jwt=encode_jwt,
    key=WRONG_SECRET,
    algorithms=['HS256'],
)

print(decode)