import mongoengine
import datetime
import uuid
from pydantic import BaseModel
from typing import List, Dict

# Load photo model
from models.shared.photo import PhotoType, Photo


class ChannelType(BaseModel):
  name: str
  summary: str
  tags: List[str]

class Channel(mongoengine.Document):

  # Channel fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  cover = mongoengine.EmbeddedDocumentField(Photo)
  name = mongoengine.StringField(max_length=60)
  status = mongoengine.StringField(max_length=60, default="active")
  summary = mongoengine.StringField(max_length=180)
  tags = mongoengine.ListField(mongoengine.StringField(max_length=50))
  followers = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  admins = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  created_at = mongoengine.DateTimeField(default=datetime.datetime.now)

  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Channel, self).save(*args, **kwargs)

