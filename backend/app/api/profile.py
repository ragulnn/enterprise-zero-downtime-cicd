from fastapi import APIRouter

from app.services.profile_service import get_profile

router = APIRouter(prefix="/api", tags=["Profile"])


@router.get("/profile")
def profile():
    return get_profile()
