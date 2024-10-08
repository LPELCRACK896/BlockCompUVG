from pydantic import BaseModel

class CreateSkillLevel(BaseModel):
    name: str
    description: str

class UpdateSkillLevel(BaseModel):
    name: str
    description: str
