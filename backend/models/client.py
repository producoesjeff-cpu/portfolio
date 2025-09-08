from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Client(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    logo: str = ""
    website: str = ""
    order: int = 0
    active: bool = True
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class ClientCreate(BaseModel):
    name: str
    logo: str = ""
    website: str = ""
    order: int = 0
    active: bool = True

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    order: Optional[int] = None
    active: Optional[bool] = None