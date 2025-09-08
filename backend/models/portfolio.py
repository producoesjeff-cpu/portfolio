from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SocialLinks(BaseModel):
    instagram: str = ""
    linkedin: str = ""
    youtube: str = ""
    whatsapp: str = ""

class PersonalInfo(BaseModel):
    name: str
    role: str
    location: str
    email: str
    phone: str
    bio: str
    heroImage: str = ""
    aboutImage: str = ""
    social: SocialLinks = SocialLinks()

class DemoReel(BaseModel):
    title: str
    description: str
    videoUrl: str = ""
    thumbnail: str = ""

class Service(BaseModel):
    title: str
    description: str
    icon: str

class Portfolio(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(datetime.utcnow().timestamp()))
    personal: PersonalInfo
    demoReel: DemoReel
    services: List[Service] = []
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

class PortfolioUpdate(BaseModel):
    personal: Optional[PersonalInfo] = None
    demoReel: Optional[DemoReel] = None
    services: Optional[List[Service]] = None