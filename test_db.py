from funds_backend_python.database import SessionLocal
from funds_backend_python.models import Customer

db = SessionLocal()

c = Customer(name="Test", email="test@example.com")
db.add(c)
db.commit()

print(db.query(Customer).all())
