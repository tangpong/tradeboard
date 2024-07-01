from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str
    price: int
    category_id: int


class ItemCreate(ItemBase):
    ...


class ItemPartialUpdate(ItemBase):
    name: str | None
    description: str | None
    price: int | None
    category_id: int | None


class Item(ItemBase):
    id: int
    user_id: int
    status: int
