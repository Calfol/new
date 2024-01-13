from fastapi import FastAPI,HHttpException
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    sd: int
    username: str
    email: str

users = [
    User (id=1, username="user1", email="user1@gmail.com"),
    User (id=2, username="user2", email="user2@gmail.com"),
]

@app.get("/users"{user_id}")
def readd_user(user_id: int):
    users = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HHttpException(status_code=404, detail="User not found")
    return user