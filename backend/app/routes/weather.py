from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.weather import Weather, WeatherCreate
from app.services.weather_service import WeatherService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Weather, status_code=status.HTTP_201_CREATED)
def create_weather(weather_in: WeatherCreate, db: Session = Depends(get_db)):
    service = WeatherService(db)
    return service.create_weather(weather_in)

@router.get("/", response_model=list[Weather])
def list_weather(db: Session = Depends(get_db)):
    service = WeatherService(db)
    return service.get_all_weather()
