

# Enable reading env variables
from dotenv import load_dotenv
from fastapi import FastAPI, Response, Request, status
from mongoengine import connect


# Connect to db
connect('car-api2')

# Enable reading env variables
load_dotenv()

# Initialize app
app = FastAPI()

# Register routes
import routes.cars
import routes.users

# @app.get("/")
# def read_root():

#     # Construct new car model
#     car = Car()
#     car.title = "audi"
#     car.model = "x5"
#     car.tags = ['cool', 'sexy']


#     # Construct embedded photo
#     photo = Photo()
#     photo._id = uuid.uuid4()
#     photo.path = "photo-path"
#     photo.filename = "photo-filename"

#     # Embedd photos
#     car.photos = [photo]

#     # Save to database
#     car.save()

#     return {"Hello": "World"}


# @app.get("/api/cars")
# def list_cars():

#     # Fetch cars
#     cars = Car.objects()

#     # Convert to json
#     json_data = cars.to_json()

#     # Return cars
#     return json.loads(json_data)



# # Get single car
# @app.get("/api/cars/{item_id}")
# async def read_item(item_id: str):
#     return {"item_id": item_id}


# # Using query paramenters
# @app.get("/api/v1/cars")
# async def read_item(skip: int = 0, limit: int = 10):
#     return { 'values': { f'{skip}': skip, f'{limit}': limit } }


# @app.post("/api/cars")
# async def create_item(payload: CarTypes,  request: Request, response: Response):

#     # Get token
#     token = request.headers.get('token')
    
#     # Check if user is valid
#     if token is None:
#          response.status_code = status.HTTP_401_UNAUTHORIZED
#          return { 'msg': "Access denied!" }

#     # Create car record
#     car = Car()
#     car.title = payload.title
#     car.model = payload.model
#     car.tags = payload.tags

#     # save photos
#     photos = []
#     for uploadedPhoto in payload.photos:

#         # Initialize Photo model instance
#         photo = Photo()

#         # Generate new photo embedded object
#         photo._id = uuid.uuid4()
#         photo.filename = uploadedPhoto.filename
#         photo.path = uploadedPhoto.path

#     # Save embedded photos
#     car.photos = []

#     # Save car to database
#     car.save()
    
#     # Response context
#     response = {
#        'status': 200,
#        'error': '',
#     }

#     # Return car back
#     return response