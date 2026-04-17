from models.student import Student
from schemas.person import PersonCreate
from schemas.response.student_response import StudentResponse


def to_student_response(student: Student)  -> StudentResponse:
    return StudentResponse(
id=student.id,
    person=PersonCreate(
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
    ),
    photo=student.photo,
    name_responsible_father=student.name_responsible_father,
    name_responsible_mother=student.name_responsible_mother,
    academy_responsible=student.academy_responsible,
    financy_responsible=student.financy_responsible,
    email_responsible_acadamy=student.email_responsible_acadamy,
    financy_responsible_email=student.financy_responsible_email,
    phone_responsible_academy=student.phone_responsible_academy,
    phone_responsible_financy=student.phone_responsible_financy,
)