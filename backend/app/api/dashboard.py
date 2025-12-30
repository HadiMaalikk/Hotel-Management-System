from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from datetime import date

from app.database.session import get_db
from app.models.room import Room
from app.models.room_stay import RoomStay
from app.models.room_stay_person import RoomStayPerson
from app.models.payment import Payment
from app.models.person import Person

from dateutil.relativedelta import relativedelta


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/rooms")
def get_dashboard_rooms(db: Session = Depends(get_db)):
    rooms = db.query(Room).all()
    today = date.today()

    dashboard_rooms = []

    for room in rooms:
        # Get active stay (if any)
        active_stay = (
            db.query(RoomStay)
            .filter(
                RoomStay.room_id == room.id,
                RoomStay.check_out_date.is_(None)
            )
            .one_or_none()
        )

        # 🟩 EMPTY ROOM
        if not active_stay:
            dashboard_rooms.append({
                "room_id": room.id,
                "status": "empty"
            })
            continue

        # Get active tenant
        tenant = (
    db.query(Person)
    .join(
        RoomStayPerson,
        RoomStayPerson.person_id == Person.id
    )
    .filter(
        RoomStayPerson.room_stay_id == active_stay.id,
        RoomStayPerson.left_on.is_(None)
    )
    .first()
)

        # 🧠 RENT STATUS LOGIC (simple version)
        status = "occupied"
        rent_type = active_stay.rent_type.lower()
        if rent_type == "monthly":
            if active_stay.check_in_date:
                due_date = active_stay.check_in_date + relativedelta(months=1)
                
                if due_date < today:
                    status = "due"
        
        elif rent_type == "daily":
            last_payment_date = (
                db.query(func.max(Payment.paid_on))
                .filter(Payment.room_stay_id == active_stay.id,
                        Payment.payment_type == "daily_rent")
                .scalar()
            )
            if not last_payment_date or last_payment_date < today:
                status = "due" 
            
        dashboard_rooms.append({
            "room_id": room.id,
            "status": status,
            "tenant": {
                "name": tenant.full_name if tenant else None,
                "phone": tenant.phone if tenant else None
            }
        })

    return dashboard_rooms
    