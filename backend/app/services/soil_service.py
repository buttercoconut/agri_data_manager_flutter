from sqlalchemy.orm import Session
from app.models.soil import Soil, SoilCreate

class SoilService:
    def __init__(self, db: Session):
        self.db = db

    def create_soil(self, soil_in: SoilCreate) -> Soil:
        soil = Soil(**soil_in.dict())
        self.db.add(soil)
        self.db.commit()
        self.db.refresh(soil)
        return soil

    def get_all_soils(self) -> list[Soil]:
        return self.db.query(Soil).all()
