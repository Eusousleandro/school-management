from fastapi import APIRouter
from controlleries.teacher import TeacherController

router_teacher = APIRouter(prefix="/teachers", tags=["teachers"])

router_teacher.get('/teachers', status_code=200)(TeacherController.get_teachers)
router_teacher.get('/teacher/{id}', status_code=200)(TeacherController.get_teacher)
router_teacher.post('/create/teacher', status_code=201)(TeacherController.create_teacher)
router_teacher.put('/update/{id}', status_code=200)(TeacherController.update_teacher)
router_teacher.delete('/delete/{id}', status_code=200)(TeacherController.delete_teacher)