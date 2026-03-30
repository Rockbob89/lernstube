from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

fake_users_db = {
    "alice": {"username": "alice", "role": "admin"},
    "bob": {"username": "bob", "role": "user"},
}


def common_params(skip: int = 0, limit: int = 100):
    pass


class CommonParams:
    def __init__(self, skip: int = 0, limit: int = 100):
        pass


def get_db():
    pass


def get_current_user(x_user: str = Header(default=None), db=Depends(get_db)):
    pass


def get_db_session():
    pass


@app.get("/items")
def list_items(params=Depends(common_params)):
    pass


@app.get("/users")
def list_users(params=Depends(common_params)):
    pass


@app.get("/me")
def get_me(user=Depends(get_current_user)):
    pass
