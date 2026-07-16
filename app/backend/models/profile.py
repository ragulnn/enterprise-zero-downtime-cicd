from pydantic import BaseModel
from typing import List


class Profile(BaseModel):
    name: str
    title: str
    location: str
    summary: str
    skills: List[str]
