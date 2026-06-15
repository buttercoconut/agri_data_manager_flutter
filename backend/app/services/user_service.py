from sqlalchemy.orm import Session
from app.models.user import User, UserCreate
from app.database import Base

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self) -> list[User]:
        return self.db.query(User).all()
