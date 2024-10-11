from components.db.mongo.models.User import User
from components.fastapi.models.payload.User import  RegisterPayload
from fastapi import APIRouter, Depends, HTTPException, status, Header
from components.services.CWeb3 import CWeb3, create_wallet
from components.jwt.models.AuthToken import verify_token, AuthToken
from projects.fastapi.config.config import mongo_db, block_chain_network
from datetime import datetime, timedelta
import bcrypt
from typing import Annotated

users = APIRouter()
GANACHE_URL = block_chain_network.URL



def hash_password(password: str, encode: str = "utf-8") -> str:
    hashed_password = bcrypt.hashpw(password.encode(encode), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def check_password(plain_password: str, hashed_password: str, encode: str = "utf-8") -> bool:
    return bcrypt.checkpw(plain_password.encode(encode), hashed_password.encode(encode))


@users.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: RegisterPayload):

    user.password = hash_password(user.password)

    web3_instance = CWeb3(url=GANACHE_URL)
    web3_conn = web3_instance.get_connection()

    address_and_private_key = create_wallet(web3_conn)
    address = address_and_private_key["address"]
    private_key = address_and_private_key["private_key"]

    new_user = User(
        name=user.name,
        email=user.email,
        nick=user.nick,
        role=user.role,
        profile_picture="",
        password=user.password,
        address=address,
        private_key=private_key,
        verified=False,
        notifications=[]
    )
    try:
        create_operation_result = await new_user.create()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


    return create_operation_result


@users.post("/login", status_code=status.HTTP_200_OK)
async def login(user: str, password: str):

    db_user = await User.find_one({"$or": [{"email": user}, {"nick": user}]})

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    if not check_password(password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )


    exp_date = (datetime.utcnow() + timedelta(minutes=15)).isoformat()
    auth_token = AuthToken(
        id=str(db_user.id),
        address=db_user.address,
        exp_date=exp_date
    )

    token = auth_token.encode()

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@users.get("/verify-token")
async def verify_token_endpoint(access_token:Annotated[str | None, Header()] = None):
    if access_token is None:
        return HTTPException(status_code=400, detail="Invalid token")

    token = access_token.split("Bearer ")[1] if "Bearer " in access_token else access_token

    valid_token = verify_token(token)

    return valid_token

