from models.user import User
from schemas.response.user_response import UserResponse
from schemas.user import UserCreate

def to_user_response(user: User) -> UserResponse:
    return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
        )