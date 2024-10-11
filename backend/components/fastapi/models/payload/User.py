from typing import Optional, List, Literal, AnyStr
from pydantic import BaseModel

class RegisterPayload(BaseModel):
    name: AnyStr
    nick: AnyStr
    email: AnyStr
    password: AnyStr
    role: Literal["student", "educator"]