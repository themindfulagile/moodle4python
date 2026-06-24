"""
Course endpoints — stub for MTP-66 (Course CRUD implementation).
"""
from fastapi import APIRouter

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("/status")
async def courses_status():
    return {"status": "courses module loaded — implementation in MTP-66"}
