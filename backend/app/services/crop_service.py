from sqlalchemy.orm import Session
from app.models.crop import Crop, CropCreate

class CropService:
    def __init__(self, db: Session):
        self.db = db

    def create_crop(self, crop_in: CropCreate) -> Crop:
        crop = Crop(**crop_in.dict())
        self.db.add(crop)
        self.db.commit()
        self.db.refresh(crop)
        return crop

    def get_all_crops(self) -> list[Crop]:
        return self.db.query(Crop).all()
