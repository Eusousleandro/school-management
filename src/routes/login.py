from fastapi import APIRouter
from schemas.token import TokenResponse
from controlleries.login import LoginController

router_login = APIRouter()

router_login.post('/login', response_model=TokenResponse)(LoginController.login)