# from pydantic import BaseModel

# class BaseResponse(BaseModel):
#     code: int
#     message: str
#     data: list = []

from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    return_code: int
    message: str
    data: Optional[T] = None

    class Config:
        extra = "forbid"
