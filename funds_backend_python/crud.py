from sqlalchemy.orm import Session
from . import models, schemas

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(
        customer_id=account.customer_id,
        account_type=account.account_type, 
        balance=account.balance
        )
    db.add(db_account )
    db.commit()
    db.refresh(db_account)
    return db_account
