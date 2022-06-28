from typing import Optional
from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from db.db import get_session
from sqlmodel import Session, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User


router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(user_id: int, response: Response):
    user = None

    async with await get_session() as s:
        async with s.begin():
            statement = select(User).where(User.id == user_id)
            results = await s.execute(statement)
            user = results.first()

    if user:
        user = user[0]
        return {"id": user.id, "first_name": user.first_name}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {}
