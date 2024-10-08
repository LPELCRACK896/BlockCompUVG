from pydantic import BaseModel
from typing import Optional, AnyStr


class CreateDisposition(BaseModel):
    name: str
    meaning: str

class UpdateDisposition(BaseModel):
    name: Optional[AnyStr] = None
    meaning: Optional[AnyStr] = None
