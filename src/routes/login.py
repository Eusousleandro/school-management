from fastapi import APIRouter
from schemas.response.token_response import TokenResponse
from controlleries.login import LoginController

router_login = APIRouter(prefix="/login", tags=['Authentication'])

router_login.post('/login', response_model=TokenResponse)(LoginController.login)