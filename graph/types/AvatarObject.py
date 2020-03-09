

from graphene import ObjectType, String, ID

class AvatarObject(ObjectType):
  _id = ID
  path = String
  filename = String