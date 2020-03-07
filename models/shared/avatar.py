import mongoengine

class Avatar(mongoengine.EmbeddedDocument):

    # Aavatar fields
    path = mongoengine.StringField()
    filename = mongoengine.StringField()