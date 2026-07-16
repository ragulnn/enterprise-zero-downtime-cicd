from pydantic import BaseModel


class Skill(BaseModel):
    category: str
    name: str
    level: str
