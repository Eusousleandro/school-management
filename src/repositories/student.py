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
        student = Student(
            name=student.name,
            email=student.email,
            cpf=student.cpf,
            rg=student.rg,
            date_of_birth=student.date_of_birth,
            address=student.address,
            number=student.number,
            complement=student.complement,
            city=student.city,
            neighborhood=student.neighborhood,
            state=student.state,
            zip_code=student.zip_code,
            phone=student.phone,
            name_responsible_father=student.name_responsible_father,
            name_responsible_mother=student.name_responsible_mother,
            academy_responsible=student.academy_responsible,
            financy_responsible=student.financy_responsible,
            email_responsible_acadamy=student.email_responsible_acadamy,
            financy_responsible_email=student.financy_responsible_email,
        )
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    async def update_student(self, db: Session, id: int, student: Student):
        up_student = db.query(Student).filter(Student.id == id).first()
        up_student.name = student.name
        up_student.email = student.email
        up_student.cpf = student.cpf
        up_student.rg = student.rg
        up_student.date_of_birth = student.date_of_birth
        up_student.address = student.address
        up_student.number = student.number
        up_student.complement = student.complement
        up_student.city = student.city
        up_student.neighborhood = student.neighborhood
        up_student.state = student.state
        up_student.zip_code = student.zip_code
        up_student.phone = student.phone
        up_student.name_responsible_father = student.name_responsible_father
        up_student.name_responsible_mother = student.name_responsible_mother
        up_student.academy_responsible = student.academy_responsible
        up_student.financy_responsible = student.financy_responsible
        up_student.email_responsible_acadamy = student.email_responsible_acadamy
        up_student.financy_responsible_email = student.financy_responsible_email
        db.commit()
        db.refresh(up_student)
        return up_student
    
    async def delete_student(self, db: Session, id: int):
        student_delete = db.query(Student).filter(Student.id == id).first()
        db.delete(student_delete)
        db.commit()
        return student_delete