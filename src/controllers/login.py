from fastapi import Request, Response, Depends, status
from sqlalchemy.orm import Session
from config.database.session import get_db
from repositories.user import UserRepository
from schemas.login import Login
from services.login import LoginService
from fastapi.security import OAuth2PasswordRequestForm

repository = UserRepository()
service = LoginService(repository)

class LoginController:
    async def login(request: Request, response: Response, 
        data: OAuth2PasswordRequestForm = Depends(), 
        db: Session = Depends(get_db)):
        
        login = Login(
            email=data.username,
            password=data.password
        )

        return await service.login_required(db=db, login=login)
            