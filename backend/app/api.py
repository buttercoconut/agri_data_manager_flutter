from fastapi import APIRouter
from ..routes.crop import router as crop_router

api_router = APIRouter()
api_router.include_router(crop_router)
