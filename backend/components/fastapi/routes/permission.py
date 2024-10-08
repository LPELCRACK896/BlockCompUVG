from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from components.db.mongo.models.Permission import Permission
from components.fastapi.models.payload.Permission import CreatePermission, UpdatePermission

permissions = APIRouter()


@permissions.post("/", response_model=Permission, status_code=status.HTTP_201_CREATED)
async def create_permission(permission: CreatePermission):
    new_permission = Permission(
        competencyId=permission.competencyId,
        ownerAddress=permission.ownerAddress,
        grantedTo=permission.grantedTo,
        canEdit=permission.canEdit,
        canTransfer=permission.canTransfer,
        grantedAt=permission.grantedAt
    )
    await new_permission.create()
    return new_permission


@permissions.get("/", response_model=List[Permission])
async def get_permissions():
    all_permissions = await Permission.find_all().to_list()
    if not all_permissions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron permisos")
    return all_permissions


@permissions.get("/{permission_id}", response_model=Permission)
async def get_permission_by_id(permission_id: PydanticObjectId):
    permission = await Permission.get(permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permiso no encontrado")
    return permission


@permissions.patch("/{permission_id}", response_model=Permission)
async def update_permission(permission_id: PydanticObjectId, permission_update: UpdatePermission):
    permission = await Permission.get(permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permiso no encontrado")

    if permission_update.competencyId is not None:
        permission.competencyId = permission_update.competencyId

    if permission_update.ownerAddress is not None:
        permission.ownerAddress = permission_update.ownerAddress

    if permission_update.grantedTo is not None:
        permission.grantedTo = permission_update.grantedTo

    if permission_update.canEdit is not None:
        permission.canEdit = permission_update.canEdit

    if permission_update.canTransfer is not None:
        permission.canTransfer = permission_update.canTransfer

    if permission_update.grantedAt is not None:
        permission.grantedAt = permission_update.grantedAt

    await permission.save()
    return permission


@permissions.delete("/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_permission(permission_id: PydanticObjectId):
    permission = await Permission.get(permission_id)
    if not permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permiso no encontrado")

    await permission.delete()
    return {"message": "Permiso eliminado exitosamente"}


@permissions.get("/search/{ownerAddress}", response_model=List[Permission])
async def search_permissions_by_owner(ownerAddress: str):
    results_permissions = await Permission.find(Permission.ownerAddress.regex(ownerAddress, "i")).to_list()

    if not results_permissions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron permisos para ese propietario")
    return results_permissions
