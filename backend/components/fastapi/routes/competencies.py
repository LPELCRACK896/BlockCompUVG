from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from components.db.mongo.models.Competency import Competency
from components.fastapi.models.payload.Competency import CreateCompetency, UpdateCompetency

competencies = APIRouter()


@competencies.post("/", response_model=Competency, status_code=status.HTTP_201_CREATED)
async def create_competency(competency: CreateCompetency):
    new_competency = Competency(
        name=competency.name,
        statement=competency.statement,
        knowledgeElements=competency.knowledgeElements,
        dispositions=competency.dispositions
    )
    await new_competency.create()
    return new_competency


@competencies.get("/", response_model=List[Competency])
async def get_competencies():
    competencies = await Competency.find_all().to_list()
    if not competencies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron competencias")
    return competencies


@competencies.get("/{competency_id}", response_model=Competency)
async def get_competency_by_id(competency_id: PydanticObjectId):
    competency = await Competency.get(competency_id)
    if not competency:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Competencia no encontrada")
    return competency


@competencies.patch("/{competency_id}", response_model=Competency)
async def update_competency(competency_id: PydanticObjectId, competency_update: UpdateCompetency):
    competency = await Competency.get(competency_id)
    if not competency:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Competencia no encontrada")

    if competency_update.name is not None:
        competency.name = competency_update.name

    if competency_update.statement is not None:
        competency.statement = competency_update.statement

    if competency_update.knowledgeElements is not None:
        competency.knowledgeElements = competency_update.knowledgeElements

    if competency_update.dispositions is not None:
        competency.dispositions = competency_update.dispositions

    await competency.save()  # Guardar los cambios
    return competency


@competencies.delete("/{competency_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_competency(competency_id: PydanticObjectId):
    competency = await Competency.get(competency_id)
    if not competency:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Competencia no encontrada")

    await competency.delete()
    return {"message": "Competencia eliminada exitosamente"}


@competencies.get("/search/{name}", response_model=List[Competency])
async def search_competencies_by_name(name: str):
    result_competencies = await Competency.find(Competency.name == name).to_list()

    if not result_competencies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron competencias con ese nombre")
    return result_competencies
