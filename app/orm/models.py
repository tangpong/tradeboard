import enum
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "user_account"

    name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    items: Mapped[list["Item"]] = relationship(back_populates="user")
    feedbacks: Mapped[list["Feedback"]] = relationship(back_populates="user")


class TradeStatus(enum.Enum):
    HIDDEN = "hidden"
    ACTIVE = "active"
    RESERVED = "reserved"
    SOLD = "sold"


class Item(Base):
    __tablename__ = "trade_item"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    sold_at: Mapped[datetime | None]

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="items")

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="items")

    status: Mapped[TradeStatus] = mapped_column(default=TradeStatus.HIDDEN)


class Category(Base):
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(unique=True)

    items: Mapped[list[Item]] = relationship(back_populates="category")

    def __repr__(self):
        return f'{self.__class__.name}(id={self.id}, name={self.name})'


class Feedback(Base):
    __tablename__ = "feedback"
    __table_args__ = (UniqueConstraint("user_id", "item_id"),)

    created_at: Mapped[datetime]
    rating: Mapped[int]
    text: Mapped[str] = mapped_column(default="")

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="feedbacks")

    item_id: Mapped[int] = mapped_column(ForeignKey("trade_item.id"))
