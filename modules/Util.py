
from libgravatar import Gravatar

class Util:

  def __init__(self):
    pass

  

  # Generate response context
  def generate_response_context(self, status, data, error):
    return {
      'status': status,
      'data': data,
      'error': error
    }

  # Generate random avatar
  def get_avatar(self, email):
    g = Gravatar(email)
    image_url = g.get_image(size=90)
    print(image_url)