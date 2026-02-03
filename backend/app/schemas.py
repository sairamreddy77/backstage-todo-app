
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(TodoBase):
    pass

class TodoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime
