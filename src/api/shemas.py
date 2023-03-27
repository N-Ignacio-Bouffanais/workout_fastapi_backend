from pydantic import BaseModel

class Routine_Schema(BaseModel):
    title: str
    category: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Rutina de verano",
                "category": "full body"
            }
        }

class Exercice_Schema(BaseModel):
    name: str
    sets: int
    weight: int
    reps: int

    class Config:
        schema_extra = {
            "example": {
                "name": "Curl biceps",
                "sets": 4,
                "weight": 12,
                "reps": 10
            }
        }


