from pydantic import BaseModel
from typing import Optional

class CreateSkillLevel(BaseModel):
    name: str
    description: str

class UpdateSkillLevel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
