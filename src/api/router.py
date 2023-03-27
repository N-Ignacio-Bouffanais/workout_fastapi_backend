from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Routine
from .shemas import Routine_Schema
from database import SessionLocal

items_router = APIRouter(
    tags=["items"],
)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@items_router.post('/routine')
async def create(request: Routine_Schema, db: Session = Depends(get_db)):
    new_routine = Routine(title = request.title, category = request.category)
    db.add(new_routine)
    db.commit()
    db.refresh(new_routine)
    return new_routine
