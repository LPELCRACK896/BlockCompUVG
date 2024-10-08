from typing import List
from beanie import Document
from pydantic import Field, BaseModel

class SkillLevelRecord(BaseModel):
    author: str = Field(..., description="Dirección del autor que evaluó la habilidad")
    isAuthorized: bool = Field(..., description="Indica si el autor está autorizado para realizar la evaluación")
    value: List[str] = Field(..., description="Lista de valores que representan los niveles de habilidad")

class SkillLevel(Document):
    skillLevelId: int = Field(..., description="Identificador único del nivel de habilidad")
    records: List[SkillLevelRecord] = Field(..., description="Registros de las evaluaciones realizadas")

    class Settings:
        name = "skill_levels"  # Nombre de la colección en MongoDB
