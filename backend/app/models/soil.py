from pydantic import BaseModel
from datetime import datetime

class SoilBase(BaseModel):
    field_location: str
    ph: float
    moisture: float
    nutrients: str

class SoilCreate(SoilBase):
    pass

class Soil(SoilBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True
