from pydantic import BaseModel
from typing import List, Dict


class PhotoTypes(BaseModel):
  path: str
  filename: str

class CarTypes(BaseModel):
    title: str
    model: str
    photos: List[PhotoTypes]
    tags: List[str]
