from uuid import uuid4

from auth.schemas import UserOut, UserAuth, TokenSchema, SystemUser
from auth.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token, OAuthEmail2PasswordRequestForm
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from auth.deps import get_current_user
from auth import models

app = FastAPI()

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    """
    Redirects the user to the '/docs' URL.

    Parameters:
        None

    Returns:
        RedirectResponse: The response object that redirects the user to the '/docs' URL.
    """
    return RedirectResponse(url='/docs')

def db_connection():
     db = SessionLocal()
     try:
          print(id(db))
          yield db
     finally:
          db.close()

@app.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth, db: Session = Depends(db_connection)):
    # querying database to check if user already exist
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    db_user = models.User(email=data.email, hashed_password=get_hashed_password(data.password), id=str(uuid4()))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuthEmail2PasswordRequestForm = Depends(), db: Session = Depends(db_connection)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.hashed_password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }

@app.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user

