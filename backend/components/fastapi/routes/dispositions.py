from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Depends, status
from components.db.mongo.models.Disposition import Disposition
from components.fastapi.models.payload.Diposition import CreateDisposition

dispositions = APIRouter()


@dispositions.post("/", response_model=Disposition, status_code=status.HTTP_201_CREATED )
async def create_disposition(disposition: Disposition):
    return await disposition.create()