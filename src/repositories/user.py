from sqlalchemy.orm import Session
from models.user import User

class UserRepository: 
    @staticmethod
    async def get_user(db: Session):
        return db.query(User).all()
    
    @staticmethod
    async def get_user_id(db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    async def get_user_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    async def create_user(db: Session, user: User):
        newUser = User(**user.dict())
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return newUser
    
    @staticmethod
    async def updateUser(db: Session, id: int, user: User):
        userUpdate = db.query(User).filter(User.id == id).first()
        update_data = user.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(userUpdate, key, value)
            
        db.commit()
        db.refresh(userUpdate)
        return userUpdate
    
    @staticmethod
    async def deleteUser(db: Session, id: int): 
        userToDelete = db.query(User).filter(User.id == id).first()
        db.delete(userToDelete)
        db.commit()
        return userToDelete