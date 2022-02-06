from typing import Optional
from fastapi import APIRouter, Body, Depends, HTTPException
from db.db import get_session
from models.users import User


router = APIRouter()


@router.get("/users/{user_id}")
async def read_user(user_id: int, q: Optional[str] = None):
    return {"id": user_id, "q": q}