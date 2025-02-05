# Домашнее задание по теме "Модели данных Pydantic"
from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users: List[User] = []

@app.get('/users')
async def get_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=2,
                                                 max_length=10,
                                                 description='Enter username',
                                                 example='UrbanUser')],
                   age: int = Path(ge=18, le=120, description='Enter age', example=24)):
    if users:
        current_index = max(user.id for user in users) + 1
    else:
        current_index = 1
    new_user = User(id=current_index, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID',
                                                   example=56)],
                      username: str = Path(min_length=2,
                                           max_length=10,
                                           description='Enter username',
                                           example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=24)):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                   le=100,
                                                   description='Enter User ID',
                                                   example=56)]) -> str:
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return f"User ID:{user_id} deleted"
    raise HTTPException(status_code=404, detail='User was not found')