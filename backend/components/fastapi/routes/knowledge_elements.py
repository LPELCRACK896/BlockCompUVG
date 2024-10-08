from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from typing import List
from components.db.mongo.models.KnowledgeElement import KnowledgeElement
from components.fastapi.models.payload.KnowledgeElement import CreateKnowledgeElement, UpdateKnowledgeElement

knowledge_element = APIRouter()


# 1. Crear un elemento de conocimiento
@knowledge_element.post("/", response_model=KnowledgeElement, status_code=status.HTTP_201_CREATED)
async def create_knowledge_element(knowledge_element: CreateKnowledgeElement):
    new_element = KnowledgeElement(
        name=knowledge_element.name,
        meaning=knowledge_element.meaning
    )
    await new_element.create()
    return new_element


# 2. Obtener todos los elementos de conocimiento
@knowledge_element.get("/", response_model=List[KnowledgeElement])
async def get_knowledge_elements():
    elements = await KnowledgeElement.find_all().to_list()
    if not elements:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron elementos de conocimiento")
    return elements


# 3. Obtener un elemento de conocimiento por su ID
@knowledge_element.get("/{element_id}", response_model=KnowledgeElement)
async def get_knowledge_element_by_id(element_id: PydanticObjectId):
    element = await KnowledgeElement.get(element_id)
    if not element:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Elemento de conocimiento no encontrado")
    return element


# 4. Actualizar un elemento de conocimiento
@knowledge_element.patch("/{element_id}", response_model=KnowledgeElement)
async def update_knowledge_element(element_id: PydanticObjectId, element_update: UpdateKnowledgeElement):
    element = await KnowledgeElement.get(element_id)
    if not element:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Elemento de conocimiento no encontrado")

    # Actualizar los campos
    if element_update.name is not None:
        element.name = element_update.name

    if element_update.description is not None:
        element.description = element_update.description

    await element.save()  # Guardar los cambios
    return element


# 5. Eliminar un elemento de conocimiento
@knowledge_element.delete("/{element_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_knowledge_element(element_id: PydanticObjectId):
    element = await KnowledgeElement.get(element_id)
    if not element:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Elemento de conocimiento no encontrado")

    await element.delete()
    return {"message": "Elemento de conocimiento eliminado exitosamente"}


@knowledge_element.get("/search/{name}", response_model=List[KnowledgeElement])
async def search_knowledge_elements_by_name(name: str):
    elements = await KnowledgeElement.find(KnowledgeElement.name == name).to_list()

    if not elements:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No se encontraron elementos de conocimiento con ese nombre")
    return elements
