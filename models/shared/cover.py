import mongoengine
from pydantic import BaseModel




class Cover(mongoengine.EmbeddedDocument):

    # Aavatar fields
    _id = mongoengine.UUIDField(binary=False)
    path = mongoengine.StringField()
    filename = mongoengine.StringField()