from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from beanie import BeanieObjectId

class CreatePermission(BaseModel):
    competencyId: BeanieObjectId
    ownerAddress: str
    grantedTo: str
    canEdit: bool
    canTransfer: bool
    grantedAt: datetime

class UpdatePermission(BaseModel):
    competencyId: Optional[BeanieObjectId] = None
    ownerAddress: Optional[str] = None
    grantedTo: Optional[str] = None
    canEdit: Optional[bool] = None
    canTransfer: Optional[bool] = None
    grantedAt: Optional[datetime] = None
