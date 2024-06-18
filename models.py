from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    

class TaskInn(BaseModel):
    title: str
    description: Optional[str]
    completed: bool
    

