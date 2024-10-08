from pydantic import BaseModel

class CreateDisposition(BaseModel):
    name: str
    meaning: str

class UpdateDisposition(BaseModel):
    name: str
    meaning: str
