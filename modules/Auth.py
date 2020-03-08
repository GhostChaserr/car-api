




import jwt
import os


# Load models
from models.user import User

class Auth:

  def __init__(self):
    
    # Get reference to auth token
    self.app_secret = os.environ.get('SECRET_KEY')

  # Generate token
  def generate_auth_token(self, payload):
    return jwt.encode(payload, self.app_secret, algorithm='HS256')
 
  # Verify token
  def verify_token(self, token):
    try:
        decoded = jwt.decode(token, self.app_secret,  algorithm='HS256')
        return decoded
    except jwt.InvalidTokenError:
      return False
    except jwt.ExpiredSignatureError:
      return False