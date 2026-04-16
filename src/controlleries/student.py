from fastapi import Depends, Request, Response, status
from sqlmodel import Session
from config.auth.auth import get_current_user
from schemas.student import StudentCreate, StudentUpdate
from repositories.student import StudentRepository
from services.student import StudentService
from config.database.session import get_db

repository = StudentRepository()
service = StudentService(repository)

class StudentController:
    async def get_students(request: Request, response: Response, 
                db: Session = Depends(get_db), current_user = Depends(get_current_user) ):
        try:
            students = await service.get_students(db)
            response.status_code = status.HTTP_200_OK
            return {'Students:' if len(students) > 1 else 'Students:': students}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error:': str(error)}

    async def get_student(request: Request, response: Response, id: int, 
                db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        try:
            student = await service.get_student_id(db=db, id=id)
            response.status_code = status.HTTP_200_OK
            return { 'Student:': student }
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error:': str(error)}

    async def create_student(request: Request, response: Response, 
                student: StudentCreate, db: Session = Depends(get_db), 
                current_user = Depends(get_current_user)):
        try:
            student_data = await request.json()
            student = StudentCreate(**student_data)
            new_student = await service.create_student(db=db, student=student)
            response.status_code = status.HTTP_201_CREATED
            return {'Student created with sucess: ' + str(new_student.id): new_student}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error:': str(error)}

    async def update_student(request: Request, response: Response, 
                student: StudentUpdate, db: Session = Depends(get_db),
                current_user = Depends(get_current_user)):
        try:
            student_update = await request.json()
            student = StudentUpdate(**student_update)
            update_student = await service.update_student(db=db, id=id, student=student)
            return {'Student updated with sucess: ' + str(update_student.id): update_student} 
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error:': str(error)}

    async def delete_student(request: Request, response: Response,
           id: int, db: Session = Depends(get_db), 
           current_user = Depends(get_current_user)):
        try:
            student_delete = await service.delete_student(db=db, id=id)
            response.status_code = status.HTTP_200_OK
            return {'Student Deleted with sucess: ' + str(student_delete.id): student_delete}
        except Exception as error:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error:': str(error)}