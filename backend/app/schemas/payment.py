from pydantic import BaseModel
from decimal import Decimal
from datetime import date
from typing import Optional

class PaymentCreate(BaseModel):
    room_stay_id: int
    amount: Decimal
    payment_type: str
    payment_mode: str
    paid_on: Optional[date]
    remarks: Optional[str]
