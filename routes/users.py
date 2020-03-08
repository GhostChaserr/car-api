


# Load app
from main import app
import json
from models.user import User, UserType, LoginType
from models.shared.avatar import Avatar, AvatarType
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

  # Query user
  user = query_module.query_by_id(Model=User, id=id, fields=('name', 'surname', 'avatar'))

  # Throw err if user was not found
  if user is None:
    response.status_code = status.HTTP_404_NOT_FOUND
    return util_module.generate_response_context(status=400, data=None, error='user was not found!')

  # Return user
  response.status_code = status.HTTP_200_OK
  return util_module.generate_response_context(status=200, data=user, error=None)



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


# Login route
@app.post('/api/users/login')
def login_user(loginPayload: LoginType, response: Response):

  # Check if email exists
  user = query_module.query_by_email(email=loginPayload.email)

  # Return error if user with given email was not found
  if user is None:
     response.status_code = status.HTTP_404_NOT_FOUND
     return util_module.generate_response_context(status=404, error='user with given email was not found', data=None)


  # Check password
  pass_is_valid = auth_module.validate_password(loginPayload.password, user.password)

  # Return error if password is invalid
  if pass_is_valid == False:
     response.status_code = status.HTTP_400_BAD_REQUEST
     return util_module.generate_response_context(status=400, error='invalid password', data=None)

  # Create token payload
  token_payload = { 'role': user.role, '_id': str(user.id) }

  # Generate token
  token = auth_module.generate_auth_token(payload=token_payload)

  # Return token
  response.status_code = status.HTTP_200_OK
  return util_module.generate_response_context(status=200, error=None, data=token)

@app.put('/api/users/{id}')
def update_user():
  return { 'msg': 'updating user!' }

@app.delete('/api/users/{id}')
def delete_user():
  return { 'msg': 'deleting user' }


@app.get('/api/me')
def query_me(request: Request, response: Response):
  
  # Query logged in user
  user = auth_module.get_me(request=request)

  if user is None:
    response.status_code = status.HTTP_404_NOT_FOUND
    return util_module.generate_response_context(status=404, error='user was not found', data=None)

  # Return logged in user data
  response.status_code = status.HTTP_200_OK
  return util_module.generate_response_context(status=200, error=None, data=user)
