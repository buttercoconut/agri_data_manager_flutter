from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CropBase(BaseModel):
    name: str
    variety: Optional[str] = None
    planting_date: datetime
    field_location: str

class CropCreate(CropBase):
    pass

class Crop(CropBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True
