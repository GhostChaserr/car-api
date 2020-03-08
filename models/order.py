



import mongoengine
import uuid
import bcrypt
import hashlib
import base64
import datetime




# Load shared models
from models.shared.avatar import Avatar, AvatarType

# Load types
from pydantic import BaseModel
from typing import List, Dict


# Load photo modl
from models.shared.photo import Photo
from models.shared.avatar import Avatar
from pydantic import BaseModel



class OrderAuthor(mongoengine.EmbeddedDocument):
    author = mongoengine.UUIDField(binary=False)
    name = mongoengine.StringField()
    surname = mongoengine.StringField()


class OrderSubject(mongoengine.EmbeddedDocument):
    car = mongoengine.UUIDField(binary=False)
    title = mongoengine.StringField()
    model = mongoengine.StringField()

class Order(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  user = mongoengine.EmbeddedDocumentField(OrderAuthor)
  subject = mongoengine.EmbeddedDocumentField(OrderSubject)
  total = mongoengine.IntField()
  start =  mongoengine.DateTimeField()
  end =  mongoengine.DateTimeField()
  created_at = mongoengine.DateTimeField(default=datetime.datetime.now)

  meta = {
    'indexes': [
        {'fields': ['user']}
      ]
  }

  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Order, self).save(*args, **kwargs)
