

# from pydantic import BaseModel, Field
from typing import Optional, List, Literal, AnyStr
from beanie import  Document
import datetime

class Notification(Document):
    timestamp: datetime.datetime
    title: AnyStr
    detail: AnyStr
    resource: AnyStr
    seen: bool

    class Settings:
        name = "notifications" # Collection's name