


# Load app
from main import app
from fastapi import FastAPI, Response, Request, status
import json
import uuid


# Load models
from models.shared.photo import Photo, PhotoType
from models.car import Car, CarType, CarFeature
from models.comment import Comment, CommentAuthor, CommentType
from models.activity import Activty, ActivitySubject
from models.order import OrderAuthor, OrderSubject, Order, OrderType

# Load helper modules
from modules.Query import Query
from modules.Auth import Auth
from modules.Util import Util
from models.user import User


# Construct modules
query_module = Query()
auth_module = Auth()
util_module = Util()




# Car routes
@app.get("/api/cars")
def get_cars():

  # Reverse query
  cars = Car.objects()
  json_data = cars.to_json()
  return { 'cars' : json.loads(json_data) }

@app.post("/api/cars")
def create_car(car_payload: CarType, response: Response, request: Request):

  #   {
  #     "title": "bwm",
  #     "summary": "manqana",
  #     "model": "bm24",
  #     "features": [
  #         {
  #             "feature": "music player",
  #             "is_available": true
  #         }
  #     ],
  #     "photos": [
  #         {
  #             "path": "string",
  #             "filename": "string"
  #         }
  #     ],
  #     "tags": [
  #         "bwm"
  #     ]
  # }
  
  # Check if admin is Logged in
  token = auth_module.get_token(request=request)
  user = auth_module.validate_token(token=token)

  if user is None:
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return util_module.generate_response_context(status=401, error='access denied!', data=None)


  # Initialize car
  car = Car()
  car.title = car_payload.title
  car.model = car_payload.model
  car.tags = car_payload.tags
  car.summary = car_payload.summary
  car.photos = []
  car.user = user["_id"]

  # Photos
  photos = []
  for uploaded_photo in car_payload.photos:
    photo = Photo()
    photo._id = uuid.uuid4()
    photo.filename = uploaded_photo.filename
    photo.path = uploaded_photo.path 
    photos.append(photo)
  
  # Features
  features = []
  for provided_feature in car_payload.features:
    feature = CarFeature()
    feature._id = uuid.uuid4()
    feature.feature = provided_feature.feature
    feature.is_available = provided_feature.is_available
    features.append(feature)

  # Append photos to car and save
  car.photos = photos
  car.features = features
  car.save()

  # Convert to json
  json_data = car.to_json()
  data = json.loads(json_data)


  # Query and update user
  # http://docs.mongoengine.org/guide/querying.html#atomic-updates
  # User.objects(_id="4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c").update_one(add_to_set__cars=[car._id])

  response.status_code = status.HTTP_200_OK
  return util_module.generate_response_context(status=201, error=None, data=data)


@app.get("/api/cars/{car_id}/comments")
def query_car_comments(car_id: str):

  # Query all comments for given car
  q_set = Comment.objects(car=car_id)
  json_data = q_set.to_json()

  # Return all comments
  return { 'comments': json.loads(json_data) }

@app.post("/api/cars/{car_id}/comments")
async def comment_car(comment_payload: CommentType, car_id: str, request: Request, response: Response):
  # {
	#   "comment":"ramdenad qiravdeba ?"
  # }
  
  # Get logged in user
  user = auth_module.get_me(request=request)

  if user is None:
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return util_module.generate_response_context(status=401, error='access denied!', data=None)

  # Query car fields
  car = Car.objects.get(_id=car_id)

  # Create new comment
  comment = Comment()
  comment.comment = comment_payload.comment
  comment.car = car_id

  # # Create author
  author = CommentAuthor()
  author.surname = user["name"]
  author.name = user["surname"]
  author.user = user["_id"]

  # Append author
  comment.author = author
  comment.save()

  # Register new activity
  activity = Activty()
  activity.action = "CommentedCar"
  activity.user = user["_id"]

  # Activity subject
  subject = ActivitySubject()
  subject.car = car_id
  subject.title = car.title
  subject.model = car.model
  activity.car = subject
  activity.save()

  # Generate JSON
  json_data = comment.to_json()
  data = json.loads(json_data)

  # Return comment back
  response.status_code = status.HTTP_200_OK
  return util_module.generate_response_context(status=201, error=None, data=data)



@app.post("/api/car/car_id/orders")
def create_order(order: OrderType, car_id: str, response: Response, request: Request):

  # Get logged in user
  user = auth_module.get_me(request=request)

  if user is None:
    response.status_code = status.HTTP_200_OK
    return util_module.generate_response_context(status=401, data=None, error="Access denied!")
      
  # Get logged in user
  car = Car.objects.only("title", "model").get(_id=car_id)
  
  # Initialize new order
  order = Order()
  order.total = 200
  order.start = "2020"
  order.end = "2020"

  # Append buyer
  order_user = OrderAuthor()
  order_user.name = user.name
  order_user.author = user._id
  order_user.surname = user.surname
  order.user = order_user

  # Append car
  order_subject = OrderSubject()
  order_subject.car = car._id
  order_subject.model = car.model
  order_subject.title = car.title
  order.subject = order_subject

  order.save()


  return { 'mgs' : "order registerd!" }


