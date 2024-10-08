from typing import Optional

from pydantic import BaseModel

class CreateKnowledgeElement(BaseModel):
    name: str
    meaning: str

class UpdateKnowledgeElement(BaseModel):
    name: Optional[str] = None
    meaning: Optional[str] = None
