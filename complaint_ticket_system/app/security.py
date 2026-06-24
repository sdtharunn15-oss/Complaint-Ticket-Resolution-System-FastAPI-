from jose import jwt
from passlib.context import CryptContext


SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def create_token(data: dict):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def hash_password(password):
    return pwd_context.hash(password)