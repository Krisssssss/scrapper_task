import mongoengine


def init_db():
    mongoengine.connect(
        "crime_db", host="mongodb://admin:password@localhost:27017/admin"
    )
