from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}

class AccountCreate(BaseModel):
    customer_id: int
    account_type: Literal["SAVINGS", "CHECKING", "INVESTMENT"]
    balance: float | None = None

class AccountRead(BaseModel):
    id: int
    customer_id: int
    account_type: str
    balance: float
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}

class TransactionCreate(BaseModel):
    account_id: int
    transcation_type: Literal["DEPOSIT", "WITHDRAWAL", "TRANSFER"]
    amount: float

class TransactionRead(BaseModel):
    id: int
    account_id: int
    transaction_type: str
    amount: float
    time_stamp: datetime

    model_config = {"from_attributes": True}

