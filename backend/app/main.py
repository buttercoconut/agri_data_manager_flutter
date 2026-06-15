from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.routes.user import router as user_router
from app.routes.crop import router as crop_router
from app.routes.soil import router as soil_router
from app.routes.weather import router as weather_router
from app.routes.community import router as community_router

app = FastAPI(title="Agri Data Manager API")

# CORS for Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(crop_router, prefix="/crops", tags=["crops"])
app.include_router(soil_router, prefix="/soil", tags=["soil"])
app.include_router(weather_router, prefix="/weather", tags=["weather"])
app.include_router(community_router, prefix="/community", tags=["community"])

@app.get("/")
async def root():
    return {"message": "Welcome to Agri Data Manager API"}
