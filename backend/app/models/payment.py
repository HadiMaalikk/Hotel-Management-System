from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from app.database.base import Base

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key = True, index = True)
    
    room_stay_id = Column(Integer, ForeignKey("room_stays.id" , ondelete="CASCADE"), nullable = False, index=True)
    amount = Column(Numeric(10,2), nullable = False)
    payment_type = Column(String, nullable = False)
    payment_mode = Column(String, nullable = False)
    paid_on = Column(Date, nullable = False)
    remarks =  Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default = func.now())
