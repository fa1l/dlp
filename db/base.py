from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class BaseDbModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
