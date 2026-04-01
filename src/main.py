from fastapi import FastAPI
from config.database.session import Base, engine
from routes.user_route import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.state.connection = connection
app.include_router(user_router)