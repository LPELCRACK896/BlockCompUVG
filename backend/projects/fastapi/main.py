# Libraries
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from pydantic import BaseModel
import os

# Modules
# from .dal_beanie import get_instance, ListSummary, ToDoList
from projects.fastapi.config.config import mongo_db

# Routes
from components.fastapi.routes.users import users

DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}




MONGODB_URI = mongo_db.MONGODB_URI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup:
    client = AsyncIOMotorClient(MONGODB_URI)
    database = client.get_database(name="blockcompuvg")

    # Ensure the database is available:
    pong = await database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")
    # print("Cluster connection is okay!")
    # app.todo_dal = await get_instance(database)

    # Yield back to FastAPI Application:
    yield

    # Shutdown:
    client.close()


app = FastAPI(lifespan=lifespan, debug=DEBUG, title="BlockCompUVG-API")

@app.get("/ping")
async def ping():
    return "pong!"


general_prefix = "/api/v1"
app.include_router(users, prefix=f"{general_prefix}/user", tags=["Users"])
"""
@app.get("/api/lists")
async def get_all_lists() -> list[ListSummary]:
    return [i async for i in app.todo_dal.list_todo_lists()]


class NewList(BaseModel):
    name: str


class NewListResponse(BaseModel):
    id: str
    name: str


@app.post("/api/lists", status_code=status.HTTP_201_CREATED)
async def create_todo_list(new_list: NewList) -> NewListResponse:
    return NewListResponse(
        id=str(await app.todo_dal.create_todo_list(new_list.name)),
        name=new_list.name,
    )


@app.get("/api/lists/{list_id}")
async def get_list(list_id: str) -> ToDoList:
    # Get a single to-do list
    return await app.todo_dal.get_todo_list(list_id)


@app.delete("/api/lists/{list_id}")
async def delete_list(list_id: str) -> bool:
    return await app.todo_dal.delete_todo_list(list_id)


class NewItem(BaseModel):
    label: str


class NewItemResponse(BaseModel):
    id: str
    label: str


@app.post(
    "/api/lists/{list_id}/items/",
    status_code=status.HTTP_201_CREATED,
)
async def create_item(list_id: str, new_item: NewItem) -> ToDoList:
    return await app.todo_dal.create_item(list_id, new_item.label)


@app.delete("/api/lists/{list_id}/items/{item_id}")
async def delete_item(list_id: str, item_id: str) -> ToDoList:
    return await app.todo_dal.delete_item(list_id, item_id)


class ToDoItemUpdate(BaseModel):
    item_id: str
    checked_state: bool


@app.patch("/api/lists/{list_id}/checked_state")
async def set_checked_state(list_id: str, update: ToDoItemUpdate) -> ToDoList:
    return await app.todo_dal.set_checked_state(
        list_id, update.item_id, update.checked_state
    )

"""