from sqlalchemy.orm import Session
from app.models.community import Post, PostCreate

class CommunityService:
    def __init__(self, db: Session):
        self.db = db

    def create_post(self, post_in: PostCreate) -> Post:
        post = Post(**post_in.dict())
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def get_all_posts(self) -> list[Post]:
        return self.db.query(Post).all()
