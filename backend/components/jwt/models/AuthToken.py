from projects.fastapi.config.config import jwt_config
from fastapi import  HTTPException
from pydantic import BaseModel
from jwt import PyJWTError, encode, decode
from typing import AnyStr, Union


algorithm: AnyStr = jwt_config.ALGORITHM
secret= jwt_config.SECRET

class AuthToken(BaseModel):
    id: AnyStr
    address: AnyStr
    exp_date: AnyStr

    def encode(self):
        return encode(self.model_dump(), secret, algorithm=algorithm)


def verify_token(token: str) -> Union[dict, HTTPException]:
    try:
        payload = decode(token, secret, algorithms=[algorithm])

        user_id: str = payload.get("id")
        address: str = payload.get("address")

        print(payload)

        if user_id is None or address is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload

    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")