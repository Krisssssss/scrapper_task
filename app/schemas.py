from pydantic import BaseModel
from typing import Optional


class SuspectDescriptionModel(BaseModel):
    sex: Optional[str] = None
    age_range: Optional[str] = None
    height: Optional[str] = None
    build: Optional[str] = None
    hair_color: Optional[str] = None
    hair_type: Optional[str] = None
    hair_length: Optional[str] = None
    facial_hair: Optional[str] = None
    ethnic_appearance: Optional[str] = None


class SuspectModel(BaseModel):
    id: str
    name: str
    crime_type: str
    crime_location: Optional[str] = None
    summary: Optional[str] = None
    details: Optional[str] = None
    photo_url: Optional[str] = None
    cs_reference: Optional[str] = None
    police_force: Optional[str] = None
    description: SuspectDescriptionModel
