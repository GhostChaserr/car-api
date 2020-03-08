



# Load modles
from models.user import User
from fastapi import status
import json

class Query:

  def __init__(self):
    pass

  # Query user by email
  def query_by_email(self, email):

    if email == False:
      raise ValueError('Provide email')

    try:
      user = User.objects.get(email=email)
      return user
    except:
      return None


  # Query user by username
  def query_by_id(self, Model, id, fields):

    if id == False:
      raise ValueError("Provide id")

    try:
      record = Model.objects.only(*fields).get(_id=id)

      # Convert
      json_data = record.to_json()

      # Dictify
      return json.loads(json_data)

    except:
      return None
  
  # By default returns first 10 record
  def query_many(self, Model, fields, filters={'start': None, 'end': 10}):

    try:
      
      # Query records
      records = Model.objects.only(*fields)[filters['start']:filters['end']]
      
      # Convert to json
      json_data = records.to_json()

      # Converts to list of dictionaries
      return json.loads(json_data)

    except:
      
      # Throw 500 error
      return None
  
  # Query related data
  def query_related(self, Model, key, recordId):
    try:
      records = Model.objects(car=recordId)
      json_data = records.to_json()
      return json.loads(json_data)
    except:
      return None

