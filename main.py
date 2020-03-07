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



# Get single car
@app.get("/api/cars/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


# Using query paramenters
@app.get("/api/v1/cars")
async def read_item(skip: int = 0, limit: int = 10):
    return { 'values': { f'{skip}': skip, f'{limit}': limit } }

# Add new car
@app.post("/api/cars")
def create_car():
    return {'message': 'posting new car'}