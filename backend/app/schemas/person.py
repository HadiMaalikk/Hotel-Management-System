from pydantic import BaseModel
from typing import Optional

class PersonCreate(BaseModel):
    full_name: str
    phone: str
    alternate_phone: Optional[str]
    id_proof_type: str
    id_proof_number: str
    address: Optional[str]

class PersonResponse(PersonCreate):
    id: int

    class Config:
        from_attributes = True
