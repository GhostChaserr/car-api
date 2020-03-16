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
from models.user import User


class CommentType(BaseModel):
  comment: str


class CommentAuthor(mongoengine.EmbeddedDocument):

    # Authot fields
    user = mongoengine.UUIDField(binary=False)
    surname = mongoengine.StringField()
    name = mongoengine.StringField()

class Comment(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  comment = mongoengine.StringField()
  car =  mongoengine.UUIDField(binary=False)
  video =  mongoengine.UUIDField(binary=False)
  author = mongoengine.EmbeddedDocumentField(CommentAuthor)
  upvotes = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  downvotes = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  created_at = mongoengine.DateTimeField(default=datetime.datetime.now)
  
  meta = {
    'indexes': [
        {'fields': ['video']}
      ]
  }

  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Comment, self).save(*args, **kwargs)
