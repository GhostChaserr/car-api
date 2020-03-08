




import jwt
import os
import bcrypt


# Load models
from models.user import User

# Load query module
from modules.Query import Query

class Auth:

  def __init__(self):
    
    # Get reference to auth token
    self.app_secret = os.environ.get('SECRET_KEY')

    # Get refernce to modules
    self.query_module = Query()


    self.validate_password(pass_to_validate='batsibatso', hashed_password="$2b$10$6uxiwQmv1B88Dfox0.mPZ.IjORPMNnUyZiuVGA8/QHRKPA2VLkKuW")

  # Generate token
  def generate_auth_token(self, payload):
    return jwt.encode(payload, self.app_secret, algorithm='HS256')


  # Validate password
  def validate_password(self, pass_to_validate, hashed_password):

    # Encode password and hash
    encodeded_hash = str.encode(hashed_password)
    encoded_pass = str.encode(pass_to_validate)

    # Check if valid
    return bcrypt.checkpw(encoded_pass, encodeded_hash)
  
  # Verify role
  def verify_permission(self, request, role):

    # Get token fromr Header
    token = self.get_token(request)
    
    # Make sure token is valid
    decoded_data = self.validate_token

    # Throw err if token is invalid
    if decoded_data is None:
      raise Exception("Access denied - wrong token ")
      
    # Check role
    if decoded_data.role == role:
      return True
    else:
      return False
  
  # Get token from request
  def get_token(self, request):
    return request.headers.get('token')
 

  # Get logged in user
  def get_me(self, request):

    # Extract token from header
    token = self.get_token(request=request)

    # Check if token was provided
    if token == False or token == None:
      return None

    # Validate token
    decoded_user = self.validate_token(token=token)

    # Query user with given id
    return self.query_module.query_by_id(Model=User, id=decoded_user['_id'], fields=('name', 'surname', 'avatar', 'username'))
    

  # Verify token
  def validate_token(self, token):
    try:
        decoded = jwt.decode(token, self.app_secret, algorithms=['HS256'], verify=True)
        return decoded
    except jwt.InvalidTokenError:
      return None
    except jwt.ExpiredSignatureError:
      return None