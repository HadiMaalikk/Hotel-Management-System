from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.person import Person


class PersonService:

    @staticmethod
    def create_person(
        db: Session,
        full_name: str,
        phone: str,
        id_proof_type: str,
        id_proof_number: str,
        alternate_phone: str | None = None,
        address: str | None = None
    ) -> Person:

        person = Person(
            full_name=full_name,
            phone=phone,
            alternate_phone=alternate_phone,
            id_proof_type=id_proof_type,
            id_proof_number=id_proof_number,
            address=address
        )

        db.add(person)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise ValueError(
                "Person with same phone number or ID proof already exists"
            )

        db.refresh(person)
        return person
