from app.database.database import Base
from app.models.user import User
from app.models.crop import Crop
from app.models.soil import Soil
from app.models.weather import Weather
from app.models.community import Post

# This file imports all models so that Base.metadata.create_all can create tables
