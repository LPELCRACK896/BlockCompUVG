from beanie import Document
from pydantic import Field

class Disposition(Document):
    name: str = Field(..., description="Nombre de la disposición")
    meaning: str = Field(..., description="Descripción o significado de la disposición")

    class Settings:
        name = "dispositions"  # Nombre de la colección en MongoDB
