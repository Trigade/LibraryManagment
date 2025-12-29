from pydantic import BaseModel
from typing import TypeVar, Optional, Generic

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    success: bool
    message: str | None = None
    data: Optional[T] = None