from typing import List

from fastapi import APIRouter

from app.models.skill import Skill


from app.services.skill_service import get_skills

router = APIRouter(prefix="/api", tags=["Skills"])


@router.get(
    "/skills",
    response_model=List[Skill]
)
def skills():

    return get_skills()
