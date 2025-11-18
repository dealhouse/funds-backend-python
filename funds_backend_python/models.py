from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from .database import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=None)

    accounts = relationship("Account", back_populates="customers")

    

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    account_type = Column(String, nullable=False)
    balance = Column(Float)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=None)
    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="accounts")
    
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    transaction_type = Column(String, nullable=False)
    amount = Column(Float)
    time_stamp = Column(DateTime, default=None)
    account = relationship("Account", back_populates="transactions")
