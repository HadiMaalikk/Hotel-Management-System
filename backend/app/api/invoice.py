from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.invoice_service import InvoiceService

router = APIRouter(prefix="/rooms", tags=["Invoices"])

@router.get("/{room_id}/invoice")
def view_invoice(room_id: int, db: Session = Depends(get_db)):
    return InvoiceService.generate_invoice(db, room_id)
