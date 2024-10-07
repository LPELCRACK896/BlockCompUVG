from components.db.mongo.models.User import User
from components.fastapi.models.response.User import RegisterResponse
from components.fastapi.models.payload.User import  RegisterPayload
from fastapi import APIRouter, Depends, HTTPException, status

users = APIRouter()
@users.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: RegisterPayload) -> RegisterResponse:


    """
    return NewListResponse(
        id=str(await app.todo_dal.create_todo_list(new_list.name)),
        name=new_list.name,
    )
    """
    return  user
