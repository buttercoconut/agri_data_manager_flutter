from sqlalchemy.orm import Session
from app.models.weather import Weather, WeatherCreate

class WeatherService:
    def __init__(self, db: Session):
        self.db = db

    def create_weather(self, weather_in: WeatherCreate) -> Weather:
        weather = Weather(**weather_in.dict())
        self.db.add(weather)
        self.db.commit()
        self.db.refresh(weather)
        return weather

    def get_all_weather(self) -> list[Weather]:
        return self.db.query(Weather).all()
