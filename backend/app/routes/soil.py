from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.soil import Soil, SoilCreate
from app.services.soil_service import SoilService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Soil, status_code=status.HTTP_201_CREATED)
def create_soil(soil_in: SoilCreate, db: Session = Depends(get_db)):
    service = SoilService(db)
    return service.create_soil(soil_in)

@router.get("/", response_model=list[Soil])
def list_soils(db: Session = Depends(get_db)):
    service = SoilService(db)
    return service.get_all_soils()
