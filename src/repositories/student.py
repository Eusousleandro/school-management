from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import StudentCreate

class StudentRepository: 

    @staticmethod
    async def get_students(db: Session):
        return db.query(Student).all()

    @staticmethod
    async def get_student_id(db: Session, id: int):
        return db.query(Student).filter(Student.id == id).first()
    
    @staticmethod
    async def get_student_email(db: Session, email: str):
        return db.query(Student).filter(Student.email == email).first()
    
    @staticmethod
    async def get_student_cpf(db: Session, cpf: str):
        return db.query(Student).filter(Student.cpf == cpf).first()
    
    @staticmethod
    async def get_student_rg(db: Session, rg: str):
        return db.query(Student).filter(Student.rg == rg).first()

    @staticmethod
    async def create_student(db: Session, student: StudentCreate):
        person = student.person.model_dump()
        student_data = student.model_dump(exclude={"person"})

        new_student = Student(**person, **student_data)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student

    async def update_student(db: Session, id: int, student: Student):
        up_student = db.query(Student).filter(Student.id == id).first()
        update_data = student.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(up_student, key, value)
            
        db.commit()
        db.refresh(up_student)
        return up_student
    
    @staticmethod
    async def delete_student(db: Session, id: int):
        student_delete = db.query(Student).filter(Student.id == id).first()
        db.delete(student_delete)
        db.commit()
        return student_delete