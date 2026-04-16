from fastapi import FastAPI
from config.database.session import Base, engine
from routes.user import user_router
from routes.login import router_login
from routes.student import router_student
from routes.teacher import router_teacher

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.state.connection = connection
app.include_router(user_router)
app.include_router(router_login)
app.include_router(router_student)
app.include_router(router_teacher)