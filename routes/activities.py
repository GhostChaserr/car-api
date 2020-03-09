


# Load app
from main import app
import json

# Load models
from models.user import User, UserType, LoginType
from models.shared.avatar import Avatar, AvatarType
from models.activity import Activty

from fastapi import Response, Request, status
import uuid

import mongoengine

# Load helper modules
from modules.Util import Util
from modules.Auth import Auth
from modules.Query import Query

query_module = Query()
util_module = Util()
auth_module = Auth()


# Load user activities
@app.get("/api/user/{id}/activities")
def query_user_activities():
  return { "msg" : "getting user actvities" }
