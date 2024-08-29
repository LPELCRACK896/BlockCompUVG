import os
from fastapi import APIRouter
from utils.configs import setup_config
user = APIRouter()

settings, mongo = setup_config()

@user.get("/")
def read_user():
    print(settings.get_config())
    return {
        "msg": "hola"
    }
