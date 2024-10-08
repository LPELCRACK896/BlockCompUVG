from pydantic import BaseModel, Field

class CreateDisposition(BaseModel):
    name: str = Field(..., description="Nombre de la disposición")
    meaning: str = Field(..., description="Descripción o significado de la disposición")
