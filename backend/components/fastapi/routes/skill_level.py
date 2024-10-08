from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from components.db.mongo.models.SkillLevel import SkillLevel
from components.fastapi.models.payload.SkillLevel import CreateSkillLevel, UpdateSkillLevel

skill_levels = APIRouter()


@skill_levels.post("/", response_model=SkillLevel, status_code=status.HTTP_201_CREATED)
async def create_skill_level(skill_level: CreateSkillLevel):
    new_skill_level = SkillLevel(
        name=skill_level.name,
        description=skill_level.description
    )
    await new_skill_level.create()
    return new_skill_level


@skill_levels.get("/", response_model=List[SkillLevel])
async def get_skill_levels():
    levels = await SkillLevel.find_all().to_list()
    if not levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron niveles de habilidad")
    return levels


@skill_levels.get("/{skill_level_id}", response_model=SkillLevel)
async def get_skill_level_by_id(skill_level_id: PydanticObjectId):
    skill_level = await SkillLevel.get(skill_level_id)
    if not skill_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel de habilidad no encontrado")
    return skill_level


@skill_levels.patch("/{skill_level_id}", response_model=SkillLevel)
async def update_skill_level(skill_level_id: PydanticObjectId, skill_level_update: UpdateSkillLevel):
    skill_level = await SkillLevel.get(skill_level_id)
    if not skill_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel de habilidad no encontrado")

    if skill_level_update.name is not None:
        skill_level.name = skill_level_update.name

    if skill_level_update.description is not None:
        skill_level.description = skill_level_update.description

    await skill_level.save()
    return skill_level

@skill_levels.delete("/{skill_level_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill_level(skill_level_id: PydanticObjectId):
    skill_level = await SkillLevel.get(skill_level_id)
    if not skill_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel de habilidad no encontrado")

    await skill_level.delete()
    return {"message": "Nivel de habilidad eliminado exitosamente"}


@skill_levels.get("/search/{name}", response_model=List[SkillLevel])
async def search_skill_levels_by_name(name: str):
    skill_levels = await SkillLevel.find(SkillLevel.name.regex(name, "i")).to_list()

    if not skill_levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron niveles de habilidad con ese nombre")
    return skill_levels
