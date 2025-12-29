from pydantic import BaseModel
from typing import Optional
from dtos.publisher_response import PublisherResponse
from dtos.category_response import CategoryResponse
from dtos.author_response import AuthorResponse

class BookBase(BaseModel):
    title: str
    isbn: str
    publish_year: int
    stock_quantity: int
    

class BookCreate(BookBase):
    publisher_id: int
    category_id: int
    author_id: int


class BookUpdate(BookBase):
    title: Optional[str] = None
    isbn: Optional[str] = None
    publish_year: Optional[int] = None
    stock_quantity: Optional[int] = None
    publisher_id: Optional[int] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None

class BookResponse(BookBase):
    id: int

    publisher_name: Optional[str] = None
    category_name: Optional[str] = None
    author_name: Optional[str] = None

    class Config:
        from_attributes = True