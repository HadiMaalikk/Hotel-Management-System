from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.payment import PaymentCreate
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("")
def add_payment(payload: PaymentCreate, db: Session = Depends(get_db)):
    return PaymentService.add_payment(
        db=db,
        room_stay_id=payload.room_stay_id,
        amount=payload.amount,
        payment_type=payload.payment_type,
        payment_mode=payload.payment_mode,
        paid_on=payload.paid_on,
        remarks=payload.remarks
    )
