from app.models import Suspect
from app.schemas import SuspectModel
from mongoengine import DoesNotExist, ValidationError


def get_all_suspects():
    return Suspect.objects()


def get_suspect_by_id(suspect_id: str):
    try:
        return Suspect.objects.get(id=suspect_id)
    except (DoesNotExist, ValidationError):
        return None

def format_suspect(suspect):
    description = suspect.description
    return SuspectModel(
        id=str(suspect.id),
        name=suspect.name,
        crime_type=suspect.crime_type,
        crime_location=suspect.crime_location,
        summary=suspect.summary,
        details=suspect.details,
        photo_url=suspect.photo_url,
        cs_reference=suspect.cs_reference,
        police_force=suspect.police_force,
        description={
            "sex": description.sex,
            "age_range": description.age_range,
            "height": description.height,
            "build": description.build,
            "hair_color": description.hair_color,
            "hair_type": description.hair_type,
            "hair_length": description.hair_length,
            "facial_hair": description.facial_hair,
            "ethnic_appearance": description.ethnic_appearance,
        },
    )
