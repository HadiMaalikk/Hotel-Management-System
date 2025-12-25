from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.room import Room
from app.models.room_stay import RoomStay
from app.models.room_stay_person import RoomStayPerson
from app.models.person import Person
from app.models.payment import Payment


class InvoiceService:

    @staticmethod
    def generate_invoice(db: Session, room_id: int):
        # 1. Get latest stay for room
        stay = (
            db.query(RoomStay)
            .filter(RoomStay.room_id == room_id)
            .order_by(RoomStay.check_in_date.desc())
            .first()
        )

        if not stay:
            raise HTTPException(404, "No stay found for this room")

        room = db.query(Room).filter(Room.id == room_id).first()

        # 2. Guests
        guests = (
            db.query(Person)
            .join(RoomStayPerson)
            .filter(RoomStayPerson.room_stay_id == stay.id)
            .all()
        )

        # 3. Payments
        payments = (
            db.query(Payment)
            .filter(Payment.room_stay_id == stay.id)
            .all()
        )

        # 4. Date calculations
        end_date = stay.check_out_date or date.today()
        total_days = (end_date - stay.check_in_date).days or 1

        # 5. Rent calculation
        rent_total = (
            stay.rent_amount * total_days
            if stay.rent_type == "DAILY"
            else stay.rent_amount
        )

        # 6. Totals
        electricity = stay.electricity_bill_amount or Decimal("0")
        water = stay.water_bill_amount or Decimal("0")

        total_amount = rent_total + electricity + water
        total_paid = sum(p.amount for p in payments)

        balance = total_amount - total_paid

        return {
            "invoice_number": f"INV-{stay.id}",
            "invoice_date": date.today(),
            "room_number": room.room_number,
            "check_in_date": stay.check_in_date,
            "check_out_date": stay.check_out_date,
            "total_days": total_days,
            "rent_type": stay.rent_type,
            "rent_amount": stay.rent_amount,
            "rent_total": rent_total,
            "electricity_bill_amount": electricity,
            "water_bill_amount": water,
            "total_amount": total_amount,
            "total_paid": total_paid,
            "balance_amount": balance,
            "guests": guests,
            "payments": payments
        }
