from pydantic import BaseModel
from typing import Optional

class PublisherBase(BaseModel):
    name: str
    address: str
    phone: str
    

class PublisherCreate(PublisherBase):
    pass


class PublisherUpdate(PublisherBase):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class PublisherResponse(PublisherBase):
    id: int
    class Config:
        from_attributes = True