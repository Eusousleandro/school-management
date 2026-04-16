import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _normalize(password: str) -> str:
    # tamanho fixo, independe de emoji/acentos
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_password(password: str):
    return pwd_context.hash(_normalize(password))

def verificy_password(plain_password, hashed_password):
    return pwd_context.verify(_normalize(plain_password), hashed_password)