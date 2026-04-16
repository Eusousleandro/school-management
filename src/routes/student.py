from fastapi import APIRouter
from controlleries.student import StudentController

router_student = APIRouter(prefix="/student", tags=["student"])

router_student.get("/get-student", status_code=200)(StudentController.get_students)
router_student.get("/get-students/{id}")(StudentController.get_student)
router_student.post("/create-student")(StudentController.create_student)
router_student.put("/update-student/{id}")(StudentController.update_student)
router_student.delete("/delete-student/{id}")(StudentController.delete_student) 