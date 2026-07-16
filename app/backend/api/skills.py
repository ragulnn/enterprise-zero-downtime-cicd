from typing import List

from fastapi import APIRouter

from app.backend.models.skill import Skill
from app.backend.services.skill_service import get_skills

router = APIRouter()


@router.get(
    "/skills",
    response_model=List[Skill]
)
def skills():

    return get_skills()
