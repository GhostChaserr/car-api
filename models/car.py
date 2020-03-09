import mongoengine
import uuid
import datetime

# Load types
from typing import List, Dict

# Load user model
from models.user import User
from pydantic import BaseModel
from models.shared.photo import PhotoType, Photo

class CarFeatureType(BaseModel):
  feature: str
  is_available: bool

class CarType(BaseModel):
    title: str
    summary: str
    model: str
    features: List[CarFeatureType]
    photos: List[PhotoType]
    tags: List[str]


class CarFeature(mongoengine.EmbeddedDocument):
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  feature = mongoengine.StringField()
  is_available = mongoengine.BooleanField(default=True)


class Car(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  title = mongoengine.StringField()
  summary = mongoengine.StringField()
  features = mongoengine.ListField(mongoengine.EmbeddedDocumentField(CarFeature))
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

  # Return car data
  def get_details(self):

    data =  { 
        "_id": self.model,
        "title": self.title, 
        "model": self.model, 
        "tags": self.tags, 
        "photos": self.photos,
        "created_at": self.created_at 
    }

    return data

  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Car, self).save(*args, **kwargs)

