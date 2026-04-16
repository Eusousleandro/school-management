from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "A_MINHA_CHAVE_AQUI"
ALGORITHM = "HS256"
ACESS_TOKEN_MINUTES = 30

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_MINUTES)

    to_encode.update({'exp': expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token