from sqlalchemy.orm import Session
from datetime import date
from fastapi import HTTPException
from app.models.room import Room
from app.models.room_stay import RoomStay
from app.schemas.room_stay import RoomStayCreate

from app.models.room_stay_person import RoomStayPerson


class RoomStayService:

    @staticmethod
    def check_in(db: Session, payload):
        # 1. Validate room exists
        room = db.query(Room).filter(Room.id == payload.room_id).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")

        # 2. Prevent double check-in
        existing_stay = (
            db.query(RoomStay)
            .filter(
                RoomStay.room_id == payload.room_id,
                RoomStay.check_out_date.is_(None)
            )
            .first()
        )

        if existing_stay:
            raise HTTPException(
                status_code=400,
                detail="Room already has an active stay"
            )

        # 3. Create stay
        stay = RoomStay(
            room_id=payload.room_id,
            check_in_date=payload.check_in_date,
            rent_type=payload.rent_type,
            rent_amount=payload.rent_amount,
            advance_amount=payload.advance_amount,
            caution_deposit=payload.caution_deposit,
            electricity_bill_amount=payload.electricity_bill_amount,
            water_bill_amount=payload.water_bill_amount,
        )

        db.add(stay)
        db.commit()
        db.refresh(stay)
        
        return stay
    
    @staticmethod
    def checkout(db: Session, room_stay_id: int, check_out_date: date):
        # 1. Fetch ACTIVE stay
        stay = (
            db.query(RoomStay)
            .filter(
                RoomStay.id == room_stay_id,
                RoomStay.check_out_date.is_(None)
            )
            .first()
        )

        if not stay:
            raise HTTPException(
                status_code=404,
                detail="Active room stay not found"
            )

        # 2. Set checkout date
        stay.check_out_date = check_out_date

        # 3. Close all active occupants
        (
            db.query(RoomStayPerson)
            .filter(
                RoomStayPerson.room_stay_id == stay.id,
                RoomStayPerson.left_on.is_(None)
            )
            .update({"left_on": check_out_date})
        )

        db.commit()
        db.refresh(stay)
        return stay
    
    
