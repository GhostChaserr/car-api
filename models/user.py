import mongoengine
import uuid
import bcrypt
import hashlib
import base64




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

  # Fields needed for JWT
  def get_auth_fields(self):
    return { 'role': self.role, '_id': str(self._id) }


  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Provide default role
    self.role = 'user'

    # Encode current password
    current_password = str.encode(self.password)

    # Hash password
    hashed = bcrypt.hashpw(current_password, bcrypt.gensalt(10))

    # Update password
    self.password = hashed.decode("utf-8") 

    # Proceed save
    super(User, self).save(*args, **kwargs)
