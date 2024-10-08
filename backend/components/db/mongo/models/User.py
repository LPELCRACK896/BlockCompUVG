from typing import Optional, List, Literal
from beanie import Document
from pydantic import Field

class User(Document):
    address: str = Field(..., description="Blockchain address of the user")
    name: str = Field(..., description="Full name of the user")
    nick: str = Field(..., description="Nickname or username of the user")
    email: str = Field(..., description="User's email address")
    password: str = Field(..., description="Hashed password of the user")
    role: Literal["student", "educator"] = Field(..., description="Role of the user, either student or educator")
    profile_pic: Optional[str] = Field(None, description="URL of the user's profile picture")
    public_key: str = Field(..., description="Public key of the user for blockchain operations")
    verified: bool = Field(False, description="Whether the user's account is verified")
    notifications: Optional[List[str]] = Field(default=[], description="List of notification IDs associated with the user")

    class Settings:
        name = "users"  # Collection name in MongoDB
