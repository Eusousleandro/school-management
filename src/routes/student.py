from fastapi import APIRouter

router_student = APIRouter(prefix="/student", tags=["student"])

router_student.get("/get-student")(lambda: {"message": "Get a specific student"})
router_student.get("/get-students/{id}")(lambda id: {"message": f"Get students with id {id}"})
router_student.post("/create-student")(lambda: {"message": "Create a new student"})
router_student.put("/update-student/{id}")(lambda id: {"message": f"Update student with id {id}"})
router_student.delete("/delete-student/{id}")(lambda id: {"message": f"Delete student with id {id}"}) 