from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from orm.models import Base, Category, Item, Feedback, User


class BaseCRUD:
    model = Base

    @classmethod
    async def create(cls, session: AsyncSession, scheme: BaseModel):
        data = cls.model(**scheme.model_dump())
        session.add(data)
        await session.commit()
        return data

    @classmethod
    async def get(cls, session: AsyncSession, item_id: int):
        model = await session.get_one(cls.model, item_id)
        return model

    @classmethod
    async def get_all(cls, session: AsyncSession):
        stmt = select(cls.model).order_by(cls.model.id)
        items = (await session.execute(stmt)).scalars().all()
        return items

    @classmethod
    async def update(cls, session: AsyncSession, item_id: int, scheme: BaseModel):
        model = await session.get_one(cls.model, item_id)

        for attr, value in scheme.model_dump().items():
            setattr(model, attr, value)

        await session.commit()
        return model

    @classmethod
    async def delete(cls, session: AsyncSession, item_id: int):
        model = session.get_one(cls.model, item_id)
        await session.delete(model)
        await session.commit()


class UserCRUD(BaseCRUD):
    model = User


class CategoryCRUD(BaseCRUD):
    model = Category


class ItemCRUD(BaseCRUD):
    model = Item


class FeedbackCRUD(BaseCRUD):
    model = Feedback
