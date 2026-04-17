def to_teacher_response(teacher):
    return {
        "id": teacher.id,
        "academy": teacher.academy,
        "person": {
            "name": teacher.name,
            "email": teacher.email,
            "cpf": teacher.cpf,
            "rg": teacher.rg,
            "date_of_birth": teacher.date_of_birth,
            "address": teacher.address,
            "number": teacher.number,
            "complement": teacher.complement,
            "city": teacher.city,
            "neighborhood": teacher.neighborhood,
            "state": teacher.state,
            "zip_code": teacher.zip_code,
            "phone": teacher.phone,
        }
    }