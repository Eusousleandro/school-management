from sqlmodel import Session
from repositories.user import UserRepository
from fastapi import HTTPException
from schemas.user import User, UserCreate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_user(self, db: Session):
        users = await self.repository.get_user(db)
        if not users: 
            raise HTTPException(status_code=404, detail="No users found")
        return users

    async def get_user_id(self, id: int, db: Session):
        user = await self.repository.get_user_id(db=db, id=id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def create_user(self, db: Session, user: UserCreate): 
        existing_user = await self.repository.get_user_email(db=db, email=user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")
            
        create_user = await self.repository.create_user(db=db, user=user)
        if not create_user:
            raise HTTPException(status_code=400, detail="User could not be created")
        return create_user

    async def update_user(self, db: Session, id: int, user: User):
        existing_user = self.repository.get_user_id(db=db, id=id)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        update_user = await self.repository.updateUser(db=db, id=id, user=user)
        if not update_user:
            raise HTTPException(status_code=400, detail="User could not be updated")
        return update_user

    async def delete_user(self, db: Session, id: int):
        existing_user = self.repository.get_user_id(db=db, id=id)
        if not existing_user:   
            raise HTTPException(status_code=404, detail="User not found")

        delete_user = await self.repository.deleteUser(db=db, id=id) 
        if not delete_user:
            raise HTTPException(status_code=404, detail="User not found")
        return delete_user
