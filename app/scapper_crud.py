from models import Suspect, SuspectDescription


def save_suspect_to_db(suspect_data):
    description = SuspectDescription(
        sex=suspect_data.get("sex"),
        age_range=suspect_data.get("age"),
        height=suspect_data.get("height"),
        build=suspect_data.get("build"),
        hair_color=suspect_data.get("hair_color"),
        hair_type=suspect_data.get("hair_type"),
        hair_length=suspect_data.get("hair_length"),
        facial_hair=suspect_data.get("facial_hair"),
        ethnic_appearance=suspect_data.get("ethnic_appearance"),
    )

    suspect = Suspect(
        name=suspect_data.get("suspect_name"),
        crime_type=suspect_data.get("crime_type"),
        crime_location=suspect_data.get("crime_location"),
        summary=suspect_data.get("summary"),
        details=suspect_data.get("full_details"),
        photo_url=suspect_data.get("img_url"),
        cs_reference=suspect_data.get("cs_reference"),
        police_force=suspect_data.get("police_force"),
        description=description,
    )

    suspect.save()
