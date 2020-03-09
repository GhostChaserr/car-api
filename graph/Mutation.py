

from graphene import ObjectType, Field
from graph.types import User

class Mutation(ObjectType):

  # Mutations
  create_user = Field(User)

  def resolve_create_user(root, info):
    return {
      "name": "gerge"
    }