import mongoengine
import uuid


# Load shared models
from models.shared.avatar import Avatar, AvatarType

# Load types
from pydantic import BaseModel
from typing import List, Dict

# User payload type
class UserType(BaseModel):
  name: str
  surname: str
  age: int
  email: str
  password: str
  username: str
  avatar: AvatarType

class User(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  name = mongoengine.StringField()
  surname = mongoengine.StringField()
  age = mongoengine.IntField()
  email = mongoengine.EmailField()
  password = mongoengine.StringField()
  username = mongoengine.StringField()
  avatar = mongoengine.EmbeddedDocumentField(Avatar)
  role = mongoengine.StringField()

  meta = {
    'indexes': [
        {'fields': ['email'], 'unique': True}
      ]
  }


  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Provide default role
    self.role = 'user'

    # Proceed save
    super(User, self).save(*args, **kwargs)
