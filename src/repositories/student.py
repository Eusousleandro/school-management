from sqlalchemy.orm import Session
from models.student import Student

class StudentRepository: 

    @staticmethod
    async def get_students(db: Session):
        return db.query(Student).all()

    async def get_student_id(self, db: Session, id: int):
        return db.query(Student).filter(Student.id == id).first()
    
    async def get_student_email(self, db: Session, email: str):
        return db.query(Student).filter(Student.email == email).first()
    
    async def get_student_cpf(self, db: Session, cpf: str):
        return db.query(Student).filter(Student.cpf == cpf).first()
    
    async def get_student_rg(self, db: Session, rg: str):
        return db.query(Student).filter(Student.rg == rg).first()

    async def create_student(self, db: Session, student: Student):
        new_student = Student(**student.dict())
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student

    async def update_student(self, db: Session, id: int, student: Student):
        up_student = db.query(Student).filter(Student.id == id).first()
        update_data = student.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(up_student, key, value)
            
        db.commit()
        db.refresh(up_student)
        return up_student
    
    async def delete_student(self, db: Session, id: int):
        student_delete = db.query(Student).filter(Student.id == id).first()
        db.delete(student_delete)
        db.commit()
        return student_delete