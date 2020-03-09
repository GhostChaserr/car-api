


# Load app
from main import app
from fastapi import FastAPI, Response, Request, status

# Load models
from models.shared.photo import Photo, PhotoType
from models.car import Car, CarType
from models.comment import Comment, CommentAuthor
from models.activity import Activty, ActivitySubject
from models.order import OrderAuthor, OrderSubject, Order, OrderType

import json
from modules.Query import Query
from models.user import User

query_module = Query()



# Car routes
@app.get("/api/cars")
def get_cars():

  # Reverse query
  cars = Car.objects(user='4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c')
  json_data = cars.to_json()
  return { 'cars' : json.loads(json_data) }

@app.post("/api/cars")
def create_car(carPayload: CarType, response: Response, request: Request):
  
  # Initialize car
  car = Car()
  car.title = "bmx"
  car.model = "m6"
  car.tags = []
  car.photos = []
  car.user = "4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c"

  # Save car
  car.save()

  # Query and update user
  # http://docs.mongoengine.org/guide/querying.html#atomic-updates
  # User.objects(_id="4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c").update_one(add_to_set__cars=[car._id])

  return { 'msg': "fethcing cars" }


@app.get("/api/cars/{car_id}/comments")
def query_car_comments(car_id: str):

  # Query all comments for given car
  q_set = Comment.objects(car=car_id)
  json_data = q_set.to_json()

  # # Return all comments
  return { 'comments': json.loads(json_data) }

@app.post("/api/cars/{car_id}/comments")
async def comment_car(car_id: str):  

  # Required payload - carId, loggedInUserId
  # car_id = "bf20d0e1-f996-479c-a719-37ad1977ce72"

  car = Car.objects.only("title", "model").get(_id=car_id)
  user = User.objects.only("name", "surname", "_id").get(_id="4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c")

  # Create new comment
  comment = Comment()
  comment.comment = "magari manqanaa"
  comment.car = car_id

  # Create author
  author = CommentAuthor()
  author.surname = user.surname
  author.name = user.name
  author.user = user._id

  # Append author
  comment.author = author

  # Create new comment
  comment.save()


  # Register new activity
  activity = Activty()
  activity.action = "CommentedCar"
  activity.user = user._id

  # Activity subject
  subject = ActivitySubject()
  subject.car = car_id
  subject.title = car.title
  subject.model = car.model
  activity.car = subject

  # Save activity
  activity.save()

  return { 'msg' : "commented!" }


@app.post("/api/car/car_id/orders")
def create_order(order: OrderType, car_id: str, response: Response, request: Request):

  # Get logged in user
  car = Car.objects.only("title", "model").get(_id=car_id)
  user = User.objects.only("name", "surname", "_id").get(_id="4bce3fd8-7c5a-4758-ad0e-a73ea0e4664c")

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


