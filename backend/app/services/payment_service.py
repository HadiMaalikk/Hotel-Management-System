from datetime import date
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.room_stay import RoomStay
from app.models.payment import Payment


class PaymentService:

    @staticmethod
    def add_payment(
        db: Session,
        room_stay_id: int,
        amount,
        payment_type: str,
        payment_mode: str,
        paid_on: date | None = None,
        remarks: str | None = None
    ) -> Payment:

        # 1. Validate ACTIVE stay (NO status column)
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
                status_code=400,
                detail="Invalid or inactive room stay"
            )

        # 2. Create payment (append-only)
        payment = Payment(
            room_stay_id=room_stay_id,
            amount=amount,
            payment_type=payment_type,
            payment_mode=payment_mode,
            paid_on=paid_on or date.today(),
            remarks=remarks
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment
