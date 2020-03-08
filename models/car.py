import mongoengine
import uuid
import datetime

# Load types
from typing import List, Dict

# Load user model
from models.user import User
from pydantic import BaseModel
from models.shared.photo import PhotoType, Photo

class CarType(BaseModel):
    title: str
    model: str
    photos: List[PhotoType]
    tags: List[str]

class Car(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  title = mongoengine.StringField()
  model = mongoengine.StringField()
  tags = mongoengine.ListField(mongoengine.StringField())
  photos = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Photo))
  user = mongoengine.UUIDField(binary=False)
  created_at = mongoengine.DateTimeField(default=datetime.datetime.now)
  meta = {
    'indexes': [
        { 'fields': ['user'] }
    ]
  }

  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Car, self).save(*args, **kwargs)

