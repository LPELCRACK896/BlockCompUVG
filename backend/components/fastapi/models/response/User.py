from pydantic import BaseModel
from typing import List, AnyStr

class RegisterResponse(BaseModel):
    id: AnyStr
    name: AnyStr
    keypair: List[AnyStr]