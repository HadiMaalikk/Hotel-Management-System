from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.room_stay import RoomStayCreate, RoomStayResponse
from app.services.room_stay_service import RoomStayService
from app.schemas.room_stay import RoomStayCheckout
from app.models.room_stay import RoomStay

router = APIRouter(
    prefix="/room-stays",
    tags=["Room Stays"]
)

@router.post("/check-in", response_model=RoomStayResponse)
def check_in(payload: RoomStayCreate, db: Session = Depends(get_db)):
    stay = RoomStayService.check_in(db, payload)

    return RoomStayResponse(
        id=stay.id,
        room_id=stay.room_id,
        check_in_date=stay.check_in_date,
        check_out_date=stay.check_out_date,
        rent_type=stay.rent_type,
        rent_amount=stay.rent_amount,
        advance_amount=stay.advance_amount,
        caution_deposit=stay.caution_deposit,
        electricity_bill_amount=stay.electricity_bill_amount,
        water_bill_amount=stay.water_bill_amount,
        status="ACTIVE"
    )


@router.post("/checkout", response_model=RoomStayResponse)
def checkout(payload: RoomStayCheckout, db: Session = Depends(get_db)):
    stay = RoomStayService.checkout(
        db=db,
        room_stay_id=payload.room_stay_id,
        check_out_date=payload.check_out_date
    )

    return RoomStayResponse(
        id=stay.id,
        room_id=stay.room_id,
        check_in_date=stay.check_in_date,
        check_out_date=stay.check_out_date,
        rent_type=stay.rent_type,
        rent_amount=stay.rent_amount,
        advance_amount=stay.advance_amount,
        caution_deposit=stay.caution_deposit,
        electricity_bill_amount=stay.electricity_bill_amount,
        water_bill_amount=stay.water_bill_amount,
        status="COMPLETED"
    )
    
@router.get("/active", response_model=list[RoomStayResponse])
def get_active_stays(db: Session = Depends(get_db)):
    stays = (
        db.query(RoomStay)
        .filter(RoomStay.check_out_date.is_(None))
        .all()
    )

    return [
        RoomStayResponse(
            id=s.id,
            room_id=s.room_id,
            check_in_date=s.check_in_date,
            check_out_date=s.check_out_date,
            rent_type=s.rent_type,
            rent_amount=s.rent_amount,
            advance_amount=s.advance_amount,
            caution_deposit=s.caution_deposit,
            electricity_bill_amount=s.electricity_bill_amount,
            water_bill_amount=s.water_bill_amount,
            status="ACTIVE"
        )
        for s in stays
    ]


@router.get("/{room_stay_id}", response_model=RoomStayResponse)
def get_room_stay(room_stay_id: int, db: Session = Depends(get_db)):
    stay = db.query(RoomStay).filter(RoomStay.id == room_stay_id).first()
    if not stay:
        raise HTTPException(status_code=404, detail="Room stay not found")

    status = "ACTIVE" if stay.check_out_date is None else "COMPLETED"

    return RoomStayResponse(
        id=stay.id,
        room_id=stay.room_id,
        check_in_date=stay.check_in_date,
        check_out_date=stay.check_out_date,
        rent_type=stay.rent_type,
        rent_amount=stay.rent_amount,
        advance_amount=stay.advance_amount,
        caution_deposit=stay.caution_deposit,
        electricity_bill_amount=stay.electricity_bill_amount,
        water_bill_amount=stay.water_bill_amount,
        status=status
    )

