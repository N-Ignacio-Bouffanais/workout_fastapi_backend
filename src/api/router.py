from fastapi import APIRouter, Depends, status, Response, HTTPException
from .models import Routine
from .shemas import Routine_Schema

items_router = APIRouter(
    tags=["routines"],
)

