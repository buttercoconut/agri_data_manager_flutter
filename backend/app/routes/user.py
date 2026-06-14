from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService()

@router.get("/", response_model=List[User])
async def list_users():
    return await user_service.get_all_users()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: User):
    return await user_service.create_user(user_in)
