from fastapi import APIRouter

from app.backend.services.profile_service import get_profile

router = APIRouter()


@router.get("/profile")
def profile():
    return get_profile()
