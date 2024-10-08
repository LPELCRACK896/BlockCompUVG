from optparse import Option

from pydantic import BaseModel
from typing import List, Optional
from beanie import BeanieObjectId

class CreateCompetency(BaseModel):
    name: str
    statement: str
    knowledgeElements: Optional[List[BeanieObjectId]]
    dispositions: Optional[List[BeanieObjectId]]

class UpdateCompetency(BaseModel):
    name: Optional[str] = None
    statement: Optional[str] = None
    knowledgeElements: Optional[List[BeanieObjectId]] = None
    dispositions: Optional[List[BeanieObjectId]] = None
