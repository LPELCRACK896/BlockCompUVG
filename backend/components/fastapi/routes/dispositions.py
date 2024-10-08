from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from components.db.mongo.models.Disposition import Disposition
from components.fastapi.models.payload.Diposition import CreateDisposition, UpdateDisposition

dispositions = APIRouter()


@dispositions.post("/", response_model=Disposition, status_code=status.HTTP_201_CREATED)
async def create_disposition(disposition: CreateDisposition):
    new_disposition = Disposition(name=disposition.name, meaning=disposition.meaning)
    await new_disposition.create()
    return new_disposition


@dispositions.get("/", response_model=List[Disposition])
async def get_dispositions():
    dispositions = await Disposition.find_all().to_list()
    if not dispositions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron disposiciones")
    return dispositions


@dispositions.get("/{disposition_id}", response_model=Disposition)
async def get_disposition_by_id(disposition_id: PydanticObjectId):
    disposition = await Disposition.get(disposition_id)
    if not disposition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Disposición no encontrada")
    return disposition


@dispositions.put("/{disposition_id}", response_model=Disposition)
async def update_disposition(disposition_id: PydanticObjectId, disposition_update: UpdateDisposition):
    disposition = await Disposition.get(disposition_id)
    if not disposition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Disposición no encontrada")

    disposition.name = disposition_update.name
    disposition.meaning = disposition_update.meaning
    await disposition.save()
    return disposition


@dispositions.delete("/{disposition_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_disposition(disposition_id: PydanticObjectId):
    disposition = await Disposition.get(disposition_id)
    if not disposition:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Disposición no encontrada")

    await disposition.delete()
    return {"message": "Disposición eliminada exitosamente"}


# 6. Buscar disposiciones por nombre
@dispositions.get("/search/{name}", response_model=List[Disposition])
async def search_dispositions_by_name(name: str):
    result_dispositions = await Disposition.find(Disposition.name == name).to_list()
    if not result_dispositions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron disposiciones con ese nombre")
    return result_dispositions
