from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from funds_backend_python import crud, schemas, models
from funds_backend_python.database import get_db

router = APIRouter()

@router.post("", response_model=schemas.CustomerRead)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Customer).filter(models.Customer.email == customer.email).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    return crud.create_customer(db, customer)
