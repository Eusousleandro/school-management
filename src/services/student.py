from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.student import StudentRepository
from schemas.student import StudentCreate, StudentUpdate

class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    async def get_students(self, db: Session):
        students = await self.repository.get_students(db=db)
        if not students:
            raise HTTPException(status_code=404, detail="No students found")
        return students

    async def get_student_id(self, id: int, db: Session):
        studend = await self.repository.get_student_id(db=db, id=id)
        if not studend:
            raise HTTPException(status_code=404, detail="Student not found")
        return studend

    async def create_student(self, db: Session, student: StudentCreate):
        existing_student = await self.repository.get_student_cpf(db=db, cpf=student.person.cpf)
        if existing_student:
            raise HTTPException(status_code=400, detail="Student with this CPF already exists")
        
        create_student = await self.repository.create_student(db=db, student=student)
        if not create_student:
            raise HTTPException(status_code=400, detail="Student could not be created")
        return create_student
    
    async def update_student(self, db: Session, id: int, student: StudentUpdate):
        existing_student = await self.repository.get_student_id(db=db, id=id)
        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        student_update= await self.repository.update_student(db=db, id=id, student=student)
        if not student_update:
            raise HTTPException(status_code=400, detail="Student could not be updated")
        return student_update

    async def delete_student(self, db: Session, id: int):
        existing_student = await self.repository.get_student_id(db=db, id=id)
        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        delete_student = await self.repository.delete_student(db=db, id=id)
        if not self.delete_student:
            raise HTTPException(status_code=400, detail="Student could not be deleted")
        return delete_student
      