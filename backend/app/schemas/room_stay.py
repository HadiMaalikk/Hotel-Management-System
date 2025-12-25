from datetime import date
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel



# REQUEST SCHEMA (CHECK-IN)

class RoomStayCreate(BaseModel):
    room_id: int
    check_in_date: date

    rent_type: Literal["DAILY", "MONTHLY"]
    rent_amount: Decimal

    advance_amount: Optional[Decimal] = None
    caution_deposit: Optional[Decimal] = None

    electricity_bill_amount: Optional[Decimal] = None
    water_bill_amount: Optional[Decimal] = None



# RESPONSE SCHEMA

class RoomStayResponse(BaseModel):
    id: int
    room_id: int

    check_in_date: date
    check_out_date: Optional[date]

    rent_type: str
    rent_amount: Decimal

    advance_amount: Optional[Decimal]
    caution_deposit: Optional[Decimal]

    electricity_bill_amount: Optional[Decimal]
    water_bill_amount: Optional[Decimal]

    status: str  # ✅ DERIVED FIELD (NOT DB)

    class Config:
        from_attributes = True


# REQUEST SCHEMA (CHECKOUT)

class RoomStayCheckout(BaseModel):
    room_stay_id: int
    check_out_date: date
