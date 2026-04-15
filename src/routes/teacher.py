from fastapi import APIRouter

router_teacher = APIRouter(prefix="/teachers", tags=["teachers"])

router_teacher.get('/', status_code=200)(lambda: {"message": "Get all teachers"})
router_teacher.get('/{id}', status_code=200)(lambda id: {"message": f"Get teacher with id {id}"})
router_teacher.post('/create', status_code=201)(lambda: {"message": "Create a new teacher"})
router_teacher.put('/update/{id}', status_code=200)(lambda id: {"message": f"Update teacher with id {id}"})
router_teacher.delete('/delete/{id}', status_code=200)(lambda id: {"message": f"Delete teacher with id {id}"})