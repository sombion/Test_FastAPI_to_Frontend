from fastapi import FastAPI
from schemas import SCreate, SCreateItems, SEditDescription, SRegister
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

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

@app.get("/items/all")
async def api_all_items():
    return {
        "detail": "Список всех items",
        "items": [
            {"title": "Название 1", "description": "Описание 1"},
            {"title": "Название 2", "description": "Описание 2"}
        ]
    }

@app.get("/items/search")
async def api_all_items():
    return {
        "detail": "Найденные items",
        "items": [
            {"title": "Название 1", "description": "Описание 1"},
            {"title": "Название 2", "description": "Описание 2"}
        ]
    }

@app.get("/items/current/{id}")
async def api_current_items(id: int):
    return {
        "title": f"Название {id}",
        "description": f"Описание {id}"
    }

@app.post("/items/create")
async def api_create_items(data_items: SCreateItems):
    return {"detail": "Items успешно добавлен"}

@app.patch("/update")
async def api_update_items(edit_data: SEditDescription):
    return {"detail": "Items успешно изменен"}

@app.delete("/delete")
async def api_delete_items(id: int):
    return {"detail": "Items успешно удален"}