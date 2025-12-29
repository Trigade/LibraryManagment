from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    category_name: str
    description: str | None = None
    

class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    category_name: Optional[str] = None
    description: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True