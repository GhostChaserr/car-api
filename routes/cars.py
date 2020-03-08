


# Load app
from main import app
from fastapi import FastAPI, Response, Request, status

# Load models
from models.shared.photo import Photo, PhotoType
from models.car import Car, CarType



# Car routes
@app.get("/api/cars")
def get_cars():
  return { 'msg' : "getting cars" }