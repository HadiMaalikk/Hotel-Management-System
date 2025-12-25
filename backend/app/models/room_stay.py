from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from app.database.base import Base

class RoomStay(Base):
    __tablename__ = "room_stays"
    id = Column(Integer, primary_key = True, index = True)
    room_id = Column(Integer, ForeignKey("rooms.id" , ondelete="RESTRICT"), nullable = False, index=True)
    check_in_date = Column(Date, nullable = False)
    check_out_date = Column(Date, nullable = True)
    
    rent_type = Column(String, nullable = False)
    rent_amount = Column(Numeric(10,2), nullable = False)
    
    advance_amount = Column(Numeric(10,2), nullable = True)
    caution_deposit = Column(Numeric(10,2), nullable = True)
    
    electricity_bill_amount = Column(Numeric(10,2), nullable = True)
    water_bill_amount = Column(Numeric(10,2), nullable = True) 
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    