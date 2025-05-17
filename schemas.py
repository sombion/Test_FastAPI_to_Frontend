from pydantic import BaseModel, Field


class SCreate(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

class SRegister(BaseModel):
    username: str = Field(...)
    login: str = Field(...)
    password: str = Field(...)

class SCreateItems(BaseModel):
    title: str = Field(...)
    description: str = Field(...)

class SEditDescription(BaseModel):
    description: str = Field(...)