from models.teacher import Teacher
from schemas.response.teacher_response import TeacherResponse
from schemas.teacher import TeacherCreate

def to_teacher_response(teacher: Teacher) -> TeacherResponse:
    return TeacherResponse(
        id=teacher.id,
        academy=teacher.academy,
        person=TeacherCreate(
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
            phone=teacher.phone,
        )
    )