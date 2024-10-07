# from pydantic import BaseModel, Field
from typing import Optional, List, Literal, AnyStr
from beanie import  Document


class User(Document):
    address: AnyStr
    name: AnyStr
    nick: AnyStr
    email: AnyStr
    password: AnyStr
    role: Literal["student", "educator"]
    profile_pic: Optional[AnyStr]
    public_key: AnyStr
    verified: bool
    notifications: Optional[List[AnyStr]]

    class Settings:
        name = "users" # Collection's name