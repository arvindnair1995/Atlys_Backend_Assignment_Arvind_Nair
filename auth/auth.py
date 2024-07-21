from fastapi import Header, HTTPException
from core.config import STATIC_TOKEN


async def verify_token(token: str = Header(...)):
    if token != STATIC_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
