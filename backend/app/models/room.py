from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from app.database.base import Base

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key = True, index = True)
    room_number = Column(String, nullable = False, unique= True, index = True)
    max_occupancy = Column(Integer, nullable = False)
    
    electricity_included = Column(Boolean, nullable = False, default = False)
    water_included = Column(Boolean, nullable = False, default = False)
    
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    
    