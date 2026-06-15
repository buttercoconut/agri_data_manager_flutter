from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User, UserCreate
from app.services.user_service import UserService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.create_user(user_in)
    return user

@router.get("/", response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()
