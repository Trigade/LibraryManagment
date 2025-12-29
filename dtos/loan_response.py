from pydantic import BaseModel
from typing import Optional
from datetime import date

class LoanBase(BaseModel):
    loan_date: date
    due_date: date
    return_date: Optional[date] = None

class LoanCreate(LoanBase):
    member_id: int
    book_id: int

class LoanUpdate(BaseModel):
    loan_date: Optional[date] = None
    due_date: Optional[date] = None
    return_date: Optional[date] = None
    member_id: Optional[int] = None
    book_id: Optional[int] = None

class LoanResponse(LoanBase):
    id: int
    book_title:str
    member_name:str
    member_last_name:str
    author_name:str
    class Config:
        from_attributes = True