from fastapi import FastAPI
from schemas import SCreate, SRegister


app = FastAPI()


@app.get("/auth/me")
async def api_detail_auth():
    return {
        "id": "1",
        "username": "Имя пользователя",
        "login": "Логин пользователя"
    }

@app.post("/auth/login")
async def api_login_auth(user_data: SCreate):
    return {"detail": "Вы успешно вошли"}

@app.post("/auth/register")
async def api_register_auth(user_data: SRegister):
    return {"detail": "Вы успешно зарегистрировались"}

@app.post("/auth/logout")
async def api_logout_auth():
    return {"detail": "Вы успешно вышли"}