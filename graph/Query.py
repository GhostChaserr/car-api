import graphene
from graphene import ObjectType, String, Boolean, List
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import json



# Load types
from graph.types.UserObject import UserObject 

# Load models
from models.user import User


class Query(ObjectType):


    # Query fields
    hello = String()
    users = List(UserObject)

    # Query resolvers
    def resolve_hello(self,info):
        return "Hello" 
    
    # Query users
    def resolve_users(self,info):
        return []
    