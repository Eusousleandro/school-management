from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.user import UserRepository
from config.auth.auth import create_acess_token
from config.security.security import verificy_password
from schemas.login import Login


class LoginService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def login_required(self, db: Session, login: Login):
        user = await self.repository.get_user_email(db=db, email=login.email)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not verificy_password(login.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid password")
        
        token = create_acess_token({'sub': user.email})

        return {"access_token": token, "token_type": "bearer"}