from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.person import PersonCreate, PersonResponse
from app.services.person_service import PersonService

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.post("", response_model=PersonResponse)
def create_person(payload: PersonCreate, db: Session = Depends(get_db)):
    return PersonService.create_person(db, payload)

@router.get("/{person_id}", response_model=PersonResponse)
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = PersonService.get_person(db, person_id)
    return person
