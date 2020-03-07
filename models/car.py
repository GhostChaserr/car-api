import mongoengine
import uuid

# Load embedded model
from models.shared.photo import Photo

class Car(mongoengine.Document):

  # Fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  title = mongoengine.StringField()
  model = mongoengine.StringField()
  tags = mongoengine.ListField(mongoengine.StringField())
  photos = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Photo))

  # Override save method
  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Proceed save
    super(Car, self).save(*args, **kwargs)

