from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

# Use python-jose for JWT: pip install python-jose[cryptography]
# Use passlib for hashing: pip install passlib[bcrypt]

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "alice": {"username": "alice", "hashed_password": "...", "role": "admin"},
    "bob": {"username": "bob", "hashed_password": "...", "role": "user"},
}


def hash_password(password: str) -> str:
    pass


def verify_password(plain: str, hashed: str) -> bool:
    pass


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    pass


def decode_access_token(token: str) -> dict:
    pass


def get_current_user(token: str = Depends(oauth2_scheme)):
    pass


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    pass


@app.get("/me")
def get_me(user=Depends(get_current_user)):
    pass


@app.get("/admin")
def admin_only(user=Depends(get_current_user)):
    pass
