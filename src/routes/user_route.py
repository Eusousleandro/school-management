from fastapi import APIRouter
from controlleries.user_controller import UserController

user_router = APIRouter()

user_router.get('/users', status_code=200)(UserController.getUsers)
user_router.get('/users/{id}', status_code=201)(UserController.getUserId)
user_router.post('/users/create/', status_code=201)(UserController.createUser)
user_router.put('/users/update/{id}', status_code=200)(UserController.updateUser)
user_router.delete('/users/delete/{id}', status_code=200)(UserController.deleteUser)