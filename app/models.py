import mongoengine as me


class SuspectDescription(me.EmbeddedDocument):
    sex = me.StringField(max_length=10, required=False)
    age_range = me.StringField(max_length=50, required=False)
    height = me.StringField(max_length=50, required=False)
    build = me.StringField(max_length=50, required=False)
    hair_color = me.StringField(max_length=50, required=False)
    hair_type = me.StringField(max_length=50, required=False)
    hair_length = me.StringField(max_length=50, required=False)
    facial_hair = me.StringField(max_length=50, required=False)
    ethnic_appearance = me.StringField(max_length=50, required=False)


class Suspect(me.Document):
    name = me.StringField(max_length=255, required=True)
    crime_type = me.StringField(max_length=255, required=True)
    crime_location = me.StringField(max_length=255, required=False)
    summary = me.StringField(required=False)
    details = me.StringField(required=False)
    photo_url = me.URLField(required=False)
    cs_reference = me.StringField(max_length=255, required=False)
    police_force = me.StringField(max_length=255, required=False)

    description = me.EmbeddedDocumentField(SuspectDescription)

    meta = {
        "collection": "suspects",
        "indexes": [
            {
                "fields": ["name", "cs_reference"],
                "unique": True,
            }
        ],
    }
