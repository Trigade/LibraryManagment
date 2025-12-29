from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MemberBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    

class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    membership_status: Optional[str] = None

class MemberResponse(MemberBase):
    id: int
    join_date:datetime
    membership_status: str
    class Config:
        from_attributes = True