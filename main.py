from fastapi import FastAPI
from mongoengine import connect
import uuid
import json

# Connect to db
connect('car-api2')

app = FastAPI()

# Load models
from models.car import Car
from models.user import User
from models.shared.photo import Photo


@app.get("/")
def read_root():

    # Construct new car model
    car = Car()
    car.title = "audi"
    car.model = "x5"
    car.tags = ['cool', 'sexy']


    # Construct embedded photo
    photo = Photo()
    photo._id = uuid.uuid4()
    photo.path = "photo-path"
    photo.filename = "photo-filename"

    # Embedd photos
    car.photos = [photo]

    # Save to database
    car.save()

    return {"Hello": "World"}


@app.get("/api/cars")
def list_cars():

    # Fetch cars
    cars = Car.objects()

    # Convert to json
    json_data = cars.to_json()

    # Return cars
    return json.loads(json_data)