from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class CategoryCreate(CategoryBase):
    ...


class CategoryPartialUpdate(CategoryBase):
    name: str | None


class Category(CategoryBase):
    id: int
