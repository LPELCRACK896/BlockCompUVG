from beanie import Document, BeanieObjectId
from pydantic import Field
from datetime import datetime
from bson import ObjectId

class Permission(Document):
    competency_id: BeanieObjectId = Field(..., description="ID de la competencia")
    owner_address: str = Field(..., description="Dirección del dueño de la competencia")
    granted_to: BeanieObjectId = Field(..., description="Id  del usuario que recibe los permisos")
    can_edit: bool = Field(..., description="Permiso para editar la competencia")
    can_transfer: bool = Field(..., description="Permiso para transferir la competencia")
    granted_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha en que se otorgaron los permisos")

    class Settings:
        name = "permissions"
