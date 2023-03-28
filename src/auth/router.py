from fastapi import APIRouter
from .schemas import User_Schema

users = APIRouter(
    tags=["users"],
)

@users.post('/login')
def login(user: User_Schema):
    return user
