from fastapi import APIRouter, Depends, status, Response, HTTPException
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


@items_router.post('/routine', status_code=status.HTTP_201_CREATED)
async def create(request: Routine_Schema, db: Session = Depends(get_db)):
    new_routine = Routine(title=request.title, category=request.category)
    db.add(new_routine)
    db.commit()
    db.refresh(new_routine)
    return new_routine


@items_router.get('/routine', status_code=status.HTTP_200_OK)
async def get_routines(db: Session = Depends(get_db)):
    routines = db.query(Routine).all()
    return routines


@items_router.get('/routine/{id}', status_code=status.HTTP_200_OK)
async def get_routine(id: str, response: Response, db: Session = Depends(get_db)):
    routine = db.query(Routine).filter(Routine.id == id).first()
    if not routine:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'the item with id {id} not found')
    return routine
