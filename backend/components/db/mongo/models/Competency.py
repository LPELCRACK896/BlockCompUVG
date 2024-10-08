from typing import List
from beanie import Document, BeanieObjectId
from pydantic import BaseModel, Field
from bson import ObjectId

class Competency(Document):
    name: str = Field(..., description="Nombre de la competencia")
    statement: str = Field(..., description="Declaración o descripción de la competencia")
    knowledgeElements: List[BeanieObjectId] = Field(..., description="IDs de los elementos de conocimiento asociados")
    dispositions: List[BeanieObjectId] = Field(..., description="IDs de las disposiciones asociadas")

    class Settings:
        name = "competencies"  # Nombre de la colección en MongoDB

