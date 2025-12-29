from pydantic import BaseModel
from typing import Optional

class AuthorBase(BaseModel):
    full_name: str
    biography: str | None = None
    
class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    full_name: Optional[str] = None
    biography: Optional[str] = None

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        from_attributes = True