from pydantic import BaseModel, EmailStr

class User_Schema(BaseModel):
    username: str
    password: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "username": "Luis Pereira",
                "password": "abcdef1234",
                "email": "username@example.com"
            }
        }
