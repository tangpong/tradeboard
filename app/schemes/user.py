from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserPartialUpdate(UserBase):
    name: str | None
    email: str | None
    password: str | None


class User(UserBase):
    id: int
