# Libraries
from sys import prefix

from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from pydantic import BaseModel
import os

from components.fastapi.routes.blockchain.blockchain_router import block_chain_router
from components.fastapi.routes.permission import permissions
from components.fastapi.routes.skill_level import skill_levels

# Modules
# from .dal_beanie import get_instance, ListSummary, ToDoList
from projects.fastapi.config.config import mongo_db, block_chain_network
from beanie import init_beanie
from components.services.CWeb3 import CWeb3, vitals_connection
# Routes
from components.fastapi.routes.users import users
from components.fastapi.routes.dispositions import dispositions
from components.fastapi.routes.competencies import competencies
from components.fastapi.routes.knowledge_elements import knowledge_element



#Models
from components.db.mongo.models.Disposition import Disposition  # Asegúrate de que los modelos estén importados
from components.db.mongo.models.User import User
from components.db.mongo.models.KnowledgeElement import KnowledgeElement
from components.db.mongo.models.Competency import Competency
from components.db.mongo.models.Permission import Permission
from components.db.mongo.models.SkillLevel import SkillLevel


DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}
MONGODB_URI = mongo_db.MONGODB_URI
GANACHE_URL = block_chain_network.URL


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Mongo:
    client = AsyncIOMotorClient(MONGODB_URI)
    database = client.get_database(name="blockcompuvg")

    # Ensure the database is available:
    pong = await database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")

    # Inicializar Beanie con los modelos
    await init_beanie(database=database, document_models=[Disposition, Competency, Permission, SkillLevel, KnowledgeElement, User])

    #Startup ganache
    web3_instance = CWeb3(url=GANACHE_URL)
    web3_conn = web3_instance.get_connection()
    if not vitals_connection(web3_conn):
        raise RuntimeError("Web3 connection is not okay!")

    print("Web3 connection is ok!")
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

app.include_router(block_chain_router, prefix=f"{general_prefix}/blockchain", tags=["Blockchain"])
app.include_router(dispositions, prefix=f"{general_prefix}/disposition", tags=["Dispositions"])
app.include_router(competencies, prefix=f"{general_prefix}/competency", tags=["Competencies"])
app.include_router(knowledge_element,  prefix=f"{general_prefix}/knowledge_element", tags=["KnowledgeElement"])
app.include_router(skill_levels, prefix=f"{general_prefix}/skill_levels", tags=["Skill Level"])
app.include_router(permissions, prefix=f"{general_prefix}/skill_levels", tags=["Permissions"] )