


# Load app
from main import app
import json
from models.user import User, UserType
from models.shared.avatar import Avatar, AvatarType
from fastapi import Response, status
import uuid

import mongoengine

# Load helper modules
from modules.Util import Util
from modules.Auth import Auth
from modules.Query import Query

query_module = Query()
util_module = Util()
auth_module = Auth()

@app.get("/api/users")
def query_users(response: Response):

  response_context = {
    'status': None,
    'data': None,
    'error': None
  }

  # Query users
  users = query_module.query_many(Model=User, fields=('name','surname','avatar'))

  # Handle query fail case
  if users is None:
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return util_module.generate_response_context(status=500, data=None, error='failed to query users')

  # Return list of users back
  return util_module.generate_response_context(status=200, data=users, error=None)


@app.get('/api/users/{id}')
def query_user(id: str, response: Response):

  try:

    user = User.objects.get(_id=id)
    response.status_code = status.HTTP_200_OK
    return { 'user': user }

  except:

    response.status_code = status.HTTP_404_NOT_FOUND
    return { 'msg': 'user was not found' }


@app.post('/api/users')
def create_user(userPayload: UserType, response: Response):

  # Response context
  response_context = {}

  # Query user by email
  email_taken = query_module.query_by_email(email=userPayload.email)

  # Throw err if email taken
  if email_taken:
    
    response_context = {
      'status': 400,
      'error': 'email taken',
      'data': None
    }
    return response_context

  # User
  user = User()
  user.name = userPayload.name
  user.surname = userPayload.surname
  user.age = userPayload.age
  user.email = userPayload.email
  user.password = userPayload.password
  user.username = userPayload.username

  # Avatar
  avatar = Avatar()

  # Generate sample avatar
  avatar._id = uuid.uuid4()
  avatar.path = "sample-avatar"
  avatar.filename = "sample-filename"
  user.avatar = avatar 

  # Save user into database
  user.save()

  # Auth fields
  user_auth_fields = user.get_auth_fields()
  
  # Generate auth token
  token = auth_module.generate_auth_token(payload={**user_auth_fields})

  # Set response and return token
  response.status_code = status.HTTP_201_CREATED
  return util_module.generate_response_context(status=201, data=token, error=None)

@app.put('/api/users/{id}')
def update_user():
  return { 'msg': 'updating user!' }

@app.delete('/api/users/{id}')
def delete_user():
  return { 'msg': 'deleting user' }

@app.put('/api/users/login')
def login_user():
  return { 'mg': "login user" }

@app.get('/api/users/me')
def query_me():
  return { 'mg' :"querying logged in user" }
