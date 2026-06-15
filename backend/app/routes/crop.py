from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.crop import Crop, CropCreate
from app.services.crop_service import CropService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Crop, status_code=status.HTTP_201_CREATED)
def create_crop(crop_in: CropCreate, db: Session = Depends(get_db)):
    service = CropService(db)
    return service.create_crop(crop_in)

@router.get("/", response_model=list[Crop])
def list_crops(db: Session = Depends(get_db)):
    service = CropService(db)
    return service.get_all_crops()
