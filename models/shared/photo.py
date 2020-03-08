import mongoengine
import uuid
from pydantic import BaseModel
from typing import List, Dict


class PhotoType(BaseModel):
  path: str
  filename: str

class Photo(mongoengine.EmbeddedDocument):

    # Aavatar fields
    _id = mongoengine.UUIDField(binary=False)
    path = mongoengine.StringField()
    filename = mongoengine.StringField()