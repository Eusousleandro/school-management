from fastapi import Depends, Request, Response, status
from sqlmodel import Session
from config.auth.auth import get_current_user
from mappers.user_mapper import to_user_response
from repositories.user import UserRepository
from schemas.user import  UserCreate, UserUpdate
from services.user import UserService
from config.database.session import get_db
from config.security.security import hash_password

repository = UserRepository()
user_service = UserService(repository)

class UserController:
    async def getUsers(request: Request, response: Response, 
            db: Session = Depends(get_db), 
            current_user = Depends(get_current_user)):
            
            users = await user_service.get_user(db)
            return [to_user_response(u) for u in users]
    
    async def getUserId(request: Request, response: Response, id: int, 
            db: Session = Depends(get_db), current_user = Depends(get_current_user)):

            user = await user_service.get_user_id(id=id, db=db)
            return to_user_response(user)

    async def createUser(request: Request, response: Response, user: UserCreate,
            db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        
            user.password = hash_password(user.password)
            return await user_service.create_user(db=db, user=user)

    async def updateUser(request: Request, response: Response, id: int, 
            user: UserUpdate, db: Session = Depends(get_db),
            current_user = Depends(get_current_user)):

            return await user_service.update_user(db=db, id=id, user=user)
            
    async def deleteUser(request: Request, response: Response, id: int, 
            db: Session = Depends(get_db), current_user = Depends(get_current_user)):
  
            return await user_service.delete_user(db=db, id=id)
