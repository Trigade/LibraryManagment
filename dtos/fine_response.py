from pydantic import BaseModel
from typing import Optional

class FineModel(BaseModel):
    amount: int
    payment_status: int = 0
    loan_id: int

class FineCreate(FineModel):
    pass

class FineUpdate(FineModel):
    amount: Optional[int] = None
    payment_status: Optional[int] = None
    loan_id: Optional[int] = None

class FineResponse(FineModel):
    id: int
    member_name: Optional[str] = None

    class Config:
        from_attributes = True