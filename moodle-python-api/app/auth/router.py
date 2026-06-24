"""
Auth endpoints — stub for MTP-52 (JWT auth implementation).
"""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/status")
async def auth_status():
    return {"status": "auth module loaded — implementation in MTP-52"}
