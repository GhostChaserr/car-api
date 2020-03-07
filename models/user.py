import mongoengine



# Load shared models
from models.shared.avatar import Avatar

class User(mongoengine.Document):

  # Fields
  id = mongoengine.ObjectIdField(primary_key=True)
  name = mongoengine.StringField()
  surname = mongoengine.StringField()
  age = mongoengine.IntField()
  email = mongoengine.EmailField()
  username = mongoengine.StringField()
  avatar = mongoengine.EmbeddedDocumentField(Avatar)