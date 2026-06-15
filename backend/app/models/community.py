from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    author_id: int

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
