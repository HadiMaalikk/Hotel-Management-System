from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.database.session import get_db
from app.services.room_stay_person_service import RoomStayPersonService

router = APIRouter(prefix="/room-stays", tags=["Room Stay Persons"])

@router.post("/{room_stay_id}/assign-person")
def assign_person(
    room_stay_id: int,
    person_id: int,
    db: Session = Depends(get_db)
):
    return RoomStayPersonService.assign_person(
        db=db,
        room_stay_id=room_stay_id,
        person_id=person_id,
        joined_on=date.today()
    )
