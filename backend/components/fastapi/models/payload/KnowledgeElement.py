from pydantic import BaseModel

class CreateKnowledgeElement(BaseModel):
    name: str
    meaning: str

class UpdateKnowledgeElement(BaseModel):
    name: str
    meaning: str
