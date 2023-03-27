from fastapi import APIRouter
from .schemas import User_Schema

users_router = APIRouter(
    tags=["users"],
)

@users_router.post('/login')
def login(user: User_Schema):
    return user
