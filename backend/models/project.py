from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Project(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    client: str
    year: str
    category: str
    description: str
    image: str = ""
    featured: bool = False
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    videoUrl: Optional[str] = ""
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class ProjectCreate(BaseModel):
    title: str
    client: str
    year: str
    category: str
    description: str
    image: str = ""
    featured: bool = False
    videoUrl: Optional[str] = ""

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    client: Optional[str] = None
    year: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    featured: Optional[bool] = None
    videoUrl: Optional[str] = None