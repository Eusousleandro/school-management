from sqlalchemy.orm import Session
from models.teacher import Teacher

class TeacherRepository: 

    @staticmethod
    async def get_teachers(self, db: Session):
        return db.query(Teacher).all()
    
    @staticmethod
    async def get_teacher_id(self, db: Session, id: int):
        return db.query(Teacher).filter(Teacher.id == id).first()
    
    @staticmethod
    async def create_teacher(self, db: Session, teacher: Teacher):
        new_teacher = Teacher(**teacher.dict())
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return new_teacher
    
    @staticmethod
    async def update_teacher(self, db: Session, id: int, teacher: Teacher):
        teacher_update = db.query(Teacher).filter(Teacher.id == id).first()
        update_data = teacher.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(update_data, key, value)
            
        db.commit()
        db.refresh(teacher_update)
        return teacher_update
    
    @staticmethod
    async def delete_teacher(self, db: Session, id: int):
        teacher_delete = db.query(Teacher).filter(Teacher.id == id).first()
        db.delete(teacher_delete)
        db.commit()
        return teacher_delete