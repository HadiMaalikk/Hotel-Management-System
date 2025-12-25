from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import not_

from app.database.session import get_db
from app.models.room import Room
from app.models.room_stay import RoomStay

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.get("/available")
def available_rooms(db: Session = Depends(get_db)):
    active_room_ids = (
        db.query(RoomStay.room_id)
        .filter(RoomStay.check_out_date.is_(None))
        .subquery()
    )

    rooms = db.query(Room).filter(Room.id.notin_(active_room_ids)).all()
    return rooms
