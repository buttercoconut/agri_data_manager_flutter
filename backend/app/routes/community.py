from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.community import Post, PostCreate
from app.services.community_service import CommunityService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post_in: PostCreate, db: Session = Depends(get_db)):
    service = CommunityService(db)
    return service.create_post(post_in)

@router.get("/", response_model=list[Post])
def list_posts(db: Session = Depends(get_db)):
    service = CommunityService(db)
    return service.get_all_posts()
