
import mongoengine
import datetime
import uuid
from pydantic import BaseModel
from typing import List, Dict

# Load photo model
from models.shared.photo import PhotoType, Photo


class VideoType(BaseModel):
  name: str
  summary: str
  path: str
  filename: str
  tags: List[str]
  thumbnail: PhotoType
  
class Video(mongoengine.Document):

  # Video filds
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  name = mongoengine.StringField(max_length=60)
  path = mongoengine.StringField()
  filename = mongoengine.StringField()
  summary = mongoengine.StringField(max_length=190)
  tags = mongoengine.ListField(mongoengine.StringField(max_length=50))
  views = mongoengine.IntField(default=0)
  thumbnail = mongoengine.EmbeddedDocumentField(Photo)
  channel = mongoengine.UUIDField(binary=False)
  upvotes = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  downvotes = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  created_at = mongoengine.DateTimeField(default=datetime.datetime.now)


  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Video, self).save(*args, **kwargs)

