from typing import List

from fastapi import APIRouter
from controlleries.user import UserController
from schemas.response.user_response import UserResponse

user_router = APIRouter(prefix='/users', tags=['users'])

user_router.get('/users', response_model=List[UserResponse], status_code=200)(UserController.getUsers)
user_router.get('/users/{id}', response_model=UserResponse, status_code=201)(UserController.getUserId)
user_router.post('/users/create/', status_code=201)(UserController.createUser)
user_router.put('/users/update/{id}', status_code=200)(UserController.updateUser)
user_router.delete('/users/delete/{id}', status_code=200)(UserController.deleteUser)