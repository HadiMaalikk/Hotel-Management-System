from sqlalchemy import Column, Numeric, String, Integer, Boolean, DateTime, Date, UniqueConstraint, ForeignKey
from sqlalchemy.sql import func
from app.database.base import Base

class RoomStayPerson(Base):
    __tablename__ = "room_stay_persons"
    
    id = Column(Integer, primary_key = True, index = True)
    room_stay_id = Column(Integer, ForeignKey("room_stays.id" , ondelete="CASCADE"), nullable = False, index=True)
    person_id = Column(Integer, ForeignKey("persons.id" , ondelete="RESTRICT"), nullable = False, index=True)
    joined_on = Column(Date, nullable = False)
    left_on = Column(Date, nullable = True)
    
    created_at = Column(DateTime(timezone=True), server_default = func.now())
