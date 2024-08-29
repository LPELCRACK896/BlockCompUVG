from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

""" 
from models.user import User, UserInDB
from models.token import Token
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

auth = APIRouter()


@auth.post("/token")
async def login_for_access_token(user: User):
    
    if not user.username in USERS:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    

    if not verify(user.username, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token = jwt.encode({"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
         
"""