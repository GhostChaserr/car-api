import mongoengine
import uuid

class Photo(mongoengine.EmbeddedDocument):

    # Aavatar fields
    _id = mongoengine.UUIDField(binary=False)
    path = mongoengine.StringField()
    filename = mongoengine.StringField()