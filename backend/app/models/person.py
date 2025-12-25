from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime, Date, UniqueConstraint
from sqlalchemy.sql import func
from app.database.base import Base

class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String, nullable = False)
    phone = Column(String, nullable = False, unique = True, index = True)
    alternate_phone = Column(String, nullable = True)
    
    id_proof_type = Column(String, nullable = False)
    id_proof_number = Column(String, nullable = False)
    
    address = Column(String, nullable = True)
    
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    
    __table_args__ = (
        UniqueConstraint(
            "id_proof_type",
            "id_proof_number",
            name="uq_person_id_proof"
        ),
    )