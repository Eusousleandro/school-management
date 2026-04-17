from fastapi import Depends, Request, Response, status
from sqlmodel import Session
from config.auth.auth import get_current_user
from mappers.student_mapper import to_student_response
from schemas.student import StudentCreate, StudentUpdate
from repositories.student import StudentRepository
from services.student import StudentService
from config.database.session import get_db

repository = StudentRepository()
service = StudentService(repository)

class StudentController:
    async def get_students(request: Request, response: Response, 
                db: Session = Depends(get_db), current_user = Depends(get_current_user) ):
        
        students = await repository.get_students(db)
        return [to_student_response(s) for s in students]   

    async def get_student(request: Request, response: Response, id: int, 
                db: Session = Depends(get_db), current_user = Depends(get_current_user)):
        
        student = await service.get_student_id(db=db, id=id)
        return to_student_response(student)
    
    async def create_student(request: Request, response: Response, 
                student: StudentCreate, db: Session = Depends(get_db), 
                current_user = Depends(get_current_user)):
        
        return await service.create_student(db=db, student=student)

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