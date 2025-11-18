from pydantic import BaseModel
from typing import Optional
from datatime import datetime

app = FastAPI()

class CustomerCreate(BaseModel):
    name: str
    email: str

class AccountCreate(BaseModel):
    customer_id: int
    account_type: Literal["SAVINGS", "CHECKING", "INVESTMENT"]
    balance: float | None = None

class TransactionCreate(BaseModel):
    account_id: int
    transcation_type: Literal["DEPOSIT", "WITHDRAWAL", "TRANSFER"]
    amount: float

class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}

class AccountRead(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    timestamp: datetime

    model_config = {"from_attributes": True}

class TransactionRead(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    timestamp: datetime

    model_config = {"from_attributes": True}

