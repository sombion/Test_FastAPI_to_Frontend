from pydantic import BaseModel, Field


class SCreate(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

class SRegister(BaseModel):
    username: str = Field(...)
    login: str = Field(...)
    password: str = Field(...)