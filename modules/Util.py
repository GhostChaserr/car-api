


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