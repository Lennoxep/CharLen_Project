from pydantic import BaseModel
from datetime import datetime


class SwipeCreate(BaseModel):
    user_id: int
    book_id: int
    action: str  # "like" or "dislike"


class SwipeResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    action: str
    created_at: datetime

    class Config:
        from_attributes = True
