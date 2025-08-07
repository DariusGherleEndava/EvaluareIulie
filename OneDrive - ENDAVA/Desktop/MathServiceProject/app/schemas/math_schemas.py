from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PowRequest(BaseModel):
    base: float
    exponent: float

class PowResponse(BaseModel):
    result: float

class FibonacciRequest(BaseModel):
    n: int

class FibonacciResponse(BaseModel):
    result: int

class FactorialRequest(BaseModel):
    n: int

class FactorialResponse(BaseModel):
    result: int

class RequestLogSchema(BaseModel):
    id: int
    operation: str
    input_data: str
    result: str
    timestamp: datetime

    class Config:
        orm_mode = True
