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
        teacher = Teacher(
            name=teacher.name,
            email=teacher.email,
            cpf=teacher.cpf,
            rg=teacher.rg,
            date_of_birth=teacher.date_of_birth,
            address=teacher.address,
            number=teacher.number,
            complement=teacher.complement,
            city=teacher.city,
            neighborhood=teacher.neighborhood,
            state=teacher.state,
            zip_code=teacher.zip_code,
            phone=teacher.phone
        )
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        return teacher
    
    @staticmethod
    async def update_teacher(self, db: Session, id: int, teacher: Teacher):
        teacher_update = db.query(Teacher).filter(Teacher.id == id).first()
        teacher_update.name = teacher.name
        teacher_update.email = teacher.email
        teacher_update.cpf = teacher.cpf
        teacher_update.rg = teacher.rg
        teacher_update.date_of_birth = teacher.date_of_birth
        teacher_update.address = teacher.address
        teacher_update.number = teacher.number
        teacher_update.complement = teacher.complement
        teacher_update.city = teacher.city
        teacher_update.neighborhood = teacher.neighborhood
        teacher_update.state = teacher.state
        teacher_update.zip_code = teacher.zip_code
        teacher_update.phone = teacher.phone
        db.commit()
        db.refresh(teacher_update)
        return teacher_update
    
    @staticmethod
    async def delete_teacher(self, db: Session, id: int):
        teacher_delete = db.query(Teacher).filter(Teacher.id == id).first()
        db.delete(teacher_delete)
        db.commit()
        return teacher_delete