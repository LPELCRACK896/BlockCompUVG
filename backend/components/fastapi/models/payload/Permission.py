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
    competencyId: BeanieObjectId
    ownerAddress: str
    grantedTo: str
    canEdit: bool
    canTransfer: bool
    grantedAt: datetime
