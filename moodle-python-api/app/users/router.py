"""
User endpoints — stub for MTP-59 (User CRUD implementation).
"""
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/status")
async def users_status():
    return {"status": "users module loaded — implementation in MTP-59"}
