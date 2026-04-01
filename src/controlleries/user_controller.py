from fastapi import Depends, Request, Response, status
from sqlmodel import Session
from repositories.user_repository import UserRepository
from schemas.user import User, UserCreate, UserUpdate
from services.user_service import UserService
from config.database.session import get_db

repository = UserRepository()
user_service = UserService(repository)

class UserController:
    async def getUsers(request: Request, response: Response, db: Session = Depends(get_db)):
        try:
            users = await user_service.get_user(db)
            response.status_code = status.HTTP_200_OK
            return { 'Usuários:' if len(users) > 1 else 'Usuário:': users }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'error': str(error) }

    async def getUserId(request: Request, response: Response, id: int, 
                db: Session = Depends(get_db)):
        try:
            user = await user_service.get_user_id(id=id, db=db)
            response.status_code = status.HTTP_200_OK
            return {'User: ': user}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'error': str(error) }

    async def createUser(request: Request, response: Response, user: UserCreate,
                db: Session = Depends(get_db)):
        try:
            user_data = await request.json()
            user = UserCreate(**user_data)
            newUser = await user_service.create_user(db=db, user=user)
            response.status_code = status.HTTP_201_CREATED
            return {'User created with sucess: ' + str(newUser.id): newUser}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'error': str(error) }

    async def updateUser(request: Request, response: Response, id: int, 
            user: UserUpdate, db: Session = Depends(get_db)):
        try: 
            user_update = await request.json()
            user = UserUpdate(**user_update)
            user_up = await user_service.update_user(db=db, id=id, user=user)
            response.status_code = status.HTTP_200_OK
            return {'User updated with sucess: ' + str(user_up.id): user_up}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'error': str(error) }
    async def deleteUser(request: Request, response: Response, id: int, 
                   db: Session = Depends(get_db)):
        try:
            user_delete = await user_service.delete_user(db=db, id=id)
            response.status_code = status.HTTP_200_OK
            return {'User deleted with sucess: ' + str(user_delete.id): user_delete}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'error': str(error) }