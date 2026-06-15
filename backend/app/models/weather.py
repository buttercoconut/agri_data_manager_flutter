from pydantic import BaseModel
from datetime import datetime

class WeatherBase(BaseModel):
    location: str
    temperature: float
    humidity: float
    forecast: str

class WeatherCreate(WeatherBase):
    pass

class Weather(WeatherBase):
    id: int
    recorded_at: datetime

    class Config:
        orm_mode = True
