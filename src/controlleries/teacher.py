from fastapi import Request, Response, Depends, status
from sqlmodel import Session
from config.database.session import get_db
from repositories.teacher import TeacherRepository
from schemas.teacher import TeacherCreate, TeacherUpdate
from services.teacher import TeacherService

repository = TeacherRepository()
service = TeacherService(repository)

class TeacjerService:
    async def get_teachers(request: Request, response: Response, db: Session = Depends(get_db)):
        try:
            teachers = await service.get_teachers(db)
            response.status_code = status.HTTP_200_OK
            return { 'Teachers:' if len(teachers) > 1 else 'Teachers:': teachers }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Error:': str(error) }

    async def get_teacher(request: Request, response: Response, id: int, db: Session = Depends(get_db)):
        try:
            teacher = await service.get_teacher_id(db=db, id=id)
            response.status_code = status.HTTP_200_OK
            return { 'Teacher:': teacher }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Error:': str(error) }

    async def create_teacher(request: Request, response: Response,
            teacher: TeacherCreate, db: Session = Depends(get_db)):
        try:
            teacher_create = request.json()
            teacher = TeacherCreate(**teacher_create)
            new_teacher = await service.create_teacher(db=db, teacher=teacher)
            response.status_code = status.HTTP_201_CREATED
            return { 'Teacher created with sucess:': str(new_teacher.id), 'Teacher:': new_teacher }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Error:': str(error) }

    async def update_teacher(request: Request, response: Response,
            id: int, teacher: TeacherUpdate, db: Session = Depends(get_db)):
        try:
            teacher_update = request.json()
            teacher = TeacherUpdate(**teacher_update)
            update_teacher = await service.update_teacher(db=db, id=id, teacher=teacher)
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Teacher updated with secuss:': str(update_teacher.id), 'Teacher:': update_teacher }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Error:': str(error) }

    async def delete_teacher(request: Request, response: Response,
            id: int, db: Session = Depends(get_db)):
        try:
            teacher_delete = await service.delete_teacher(db=db, id=id)
            response.status_code = status.HTTP_200_OK
            return { 'Teacher deleted with sucess:': str(teacher_delete.id), 'Teacher:': teacher_delete }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return { 'Error:': str(error) }

