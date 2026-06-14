# FastAPI 라우터 예시
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.models.crop import Crop, CropCreate
from app.services.crop_service import CropService

router = APIRouter()

crop_service = CropService()

@router.get("/", response_model=List[Crop])
async def get_crops():
    return await crop_service.get_all_crops()

@router.post("/", response_model=Crop, status_code=status.HTTP_201_CREATED)
async def create_crop(crop: CropCreate):
    return await crop_service.create_crop(crop)
