

# Lod saclars and  Object topes
from graphene import ObjectType, String, Int, Boolean, ID


# Load avatar
from graph.types.AvatarObject import AvatarObject

  # _id = mongoengine.UUIDField(binary=False, primary_key=True)
  # name = mongoengine.StringField()
  # surname = mongoengine.StringField()
  # age = mongoengine.IntField()
  # email = mongoengine.EmailField()
  # password = mongoengine.StringField()
  # username = mongoengine.StringField()
  # avatar = mongoengine.EmbeddedDocumentField(Avatar)
  # role = mongoengine.StringField()
  # created_at = mongoengine.DateTimeField(default=datetime.datetime.now)

class UserObject (ObjectType):
  _id = ID
  name = String()
  surname = String()
  age = Int()
  email = String()
  password = String()
  username = String()
  avatar = AvatarObject
  role = String()
  created_at = String()

