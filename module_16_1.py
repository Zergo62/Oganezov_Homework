# Домашнее задание по теме "Основы Fast Api и маршрутизация"
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page():
    return 'Главная страница'

@app.get('/user')
async def user_page(username: str = 'Sergo', age: int = 41):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}.'

@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user_page_id(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'