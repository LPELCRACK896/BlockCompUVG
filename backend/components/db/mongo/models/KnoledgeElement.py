from beanie import Document
from pydantic import Field

class KnowledgeElement(Document):
    name: str = Field(..., description="Nombre del elemento de conocimiento")
    meaning: str = Field(..., description="Descripción o significado del elemento de conocimiento")

    class Settings:
        name = "knowledge_elements"  # Nombre de la colección en MongoDB
