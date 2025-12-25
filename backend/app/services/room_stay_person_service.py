from datetime import date
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.room import Room
from app.models.person import Person
from app.models.room_stay import RoomStay
from app.models.room_stay_person import RoomStayPerson


class RoomStayPersonService:

    @staticmethod
    def assign_person(
        db: Session,
        room_stay_id: int,
        person_id: int,
        joined_on: date | None = None
    ) -> RoomStayPerson:

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

        # 2. Validate person exists
        person = db.query(Person).filter(Person.id == person_id).first()
        if not person:
            raise HTTPException(
                status_code=404,
                detail="Person not found"
            )

        # 3. Ensure person is not in another ACTIVE stay
        active_assignment = (
            db.query(RoomStayPerson)
            .join(RoomStay, RoomStay.id == RoomStayPerson.room_stay_id)
            .filter(
                RoomStayPerson.person_id == person_id,
                RoomStayPerson.left_on.is_(None),
                RoomStay.check_out_date.is_(None)
            )
            .first()
        )

        if active_assignment:
            raise HTTPException(
                status_code=400,
                detail="Person already assigned to another room"
            )

        # 4. Check room occupancy
        room = db.query(Room).filter(Room.id == stay.room_id).first()
        if not room:
            raise HTTPException(
                status_code=404,
                detail="Room not found"
            )

        current_occupancy = (
            db.query(RoomStayPerson)
            .filter(
                RoomStayPerson.room_stay_id == room_stay_id,
                RoomStayPerson.left_on.is_(None)
            )
            .count()
        )

        if current_occupancy >= room.max_occupancy:
            raise HTTPException(
                status_code=400,
                detail="Room occupancy limit reached"
            )

        # 5. Assign person to stay
        assignment = RoomStayPerson(
            room_stay_id=room_stay_id,
            person_id=person_id,
            joined_on=joined_on or date.today()
        )

        db.add(assignment)
        db.commit()
        db.refresh(assignment)

        return assignment
