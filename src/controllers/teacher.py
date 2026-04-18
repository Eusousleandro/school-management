from fastapi import Request, Response, Depends, status
from sqlmodel import Session
from config.auth.auth import get_current_user
from config.database.session import get_db
from mappers.teacher_mapper import to_teacher_response
from repositories.teacher import TeacherRepository
from schemas.teacher import TeacherCreate, TeacherUpdate
from services.teacher import TeacherService

repository = TeacherRepository()
service = TeacherService(repository)

class TeacherController:
    async def get_teachers(request: Request, response: Response, 
            db: Session = Depends(get_db), current_user = Depends(get_current_user)):

        teachers = await service.get_teachers(db)
        return [to_teacher_response(teacher) for teacher in teachers]

    async def get_teacher(request: Request, response: Response, 
            id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        
        teacher = await service.get_teacher_id(db=db, id=id)
        return to_teacher_response(teacher)

    async def create_teacher(request: Request, response: Response,
            teacher: TeacherCreate, db: Session = Depends(get_db), 
            current_user = Depends(get_current_user)):
        
        return await service.create_teacher(db=db, teacher=teacher)

    async def update_teacher(request: Request, id: int, teacher: TeacherUpdate, 
            db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        
        return await service.update_teacher(db=db, id=id, teacher=teacher)

    async def delete_teacher(request: Request, response: Response,
            id: int, db: Session = Depends(get_db),
            current_user = Depends(get_current_user)):

        return await service.delete_teacher(db=db, id=id)