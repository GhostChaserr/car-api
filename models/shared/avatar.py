import mongoengine
from pydantic import BaseModel


class AvatarType(BaseModel):

  # Fields   
  path: str = None
  filename: str = None

class Avatar(mongoengine.EmbeddedDocument):

    # Aavatar fields
    _id = mongoengine.UUIDField(binary=False)
    path = mongoengine.StringField()
    filename = mongoengine.StringField()