from fastapi import APIRouter
from src.schemas.user import User

router = APIRouter()

@router.post("/")
def create_user(user: User):
    return user

@router.get("/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
