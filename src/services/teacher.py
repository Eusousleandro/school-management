from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.teacher import TeacherRepository
from schemas.teacher import TeacherCreate, TeacherUpdate

class TeacherService:
    def __init__(self, repository: TeacherRepository):
        self.repository = repository
    
    async def get_teachers(self, db: Session):
        teachers = await self.repository.get_teachers(db=db)
        if not teachers:
            raise HTTPException(status_code=404, detail="Teachers not found")
        return teachers
    
    async def get_teacher_id(self, db: Session, id: int):
        teacher = await self.repository.get_teacher_id(db=db, id=id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return teacher

    async def create_teacher(self, db: Session, teacher: TeacherCreate):
        existing_teacher = await self.repository.get_teacher_id(db=db, id=teacher.id)
        if existing_teacher:
            raise HTTPException(status_code=400, detail="Teacher with this ID already exists")
        
        create_teacher = await self.repository.create_teacher(db=db, teacher=teacher)
        return create_teacher

    async def update_teacher(self, db: Session, id: int, teacher: TeacherUpdate):
        existing_teacher = await self.repository.get_teacher_id(db=db, id=id)
        if not existing_teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        teacher_update = await self.repository.update_teacher(db=db, id=id, teacher=teacher)
        return teacher_update

    async def delete_teacher(self, db: Session, id: int):
        existing_teacher = await self.repository.get_teacher_id(db=db, id=id)
        if not existing_teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        delete_teacher = await self.repository.delete_teacher(db=db, id=id)
        return delete_teacher
        