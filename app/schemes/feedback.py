from pydantic import BaseModel, ConfigDict


class FeedbackBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    rating: int
    text: str


class FeedbackCreate(FeedbackBase):
    ...


class FeedbackPartialUpdate(FeedbackBase):
    name: str | None
    rating: int | None
    text: str | None


class Feedback(FeedbackBase):
    id: int
    user: int


