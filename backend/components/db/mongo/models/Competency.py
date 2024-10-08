from optparse import Option
from typing import List, Optional
from beanie import Document, BeanieObjectId
from pydantic import BaseModel, Field

class Competency(Document):
    name: str = Field(..., description="Nombre de la competencia")
    statement: str = Field(..., description="Declaración o descripción de la competencia")
    knowledgeElements: Optional[List[BeanieObjectId]] = Field(..., description="IDs de los elementos de conocimiento asociados")
    dispositions: Optional[List[BeanieObjectId]] = Field(..., description="IDs de las disposiciones asociadas")

    class Settings:
        name = "competencies"  # Nombre de la colección en MongoDB

