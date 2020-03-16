






import mongoengine

class PlayList(mongoengine.Document):

  # Playlist fields
  _id = mongoengine.UUIDField(binary=False, primary_key=True)
  name = mongoengine.StringField()
  summary = mongoengine.StringField()
  videos = mongoengine.ListField(mongoengine.UUIDField(binary=False))
  channel = mongoengine.UUIDField(binary=False)
  tags = mongoengine.ListField(mongoengine.StringField(max_length=50))

  def save(self,  *args, **kwargs):
    
    # Update id value with unique id
    self._id = uuid.uuid4()

    # Provide default role
    self.role = 'user'

    # Encode current password
    current_password = str.encode(self.password)

    # Hash password
    hashed = bcrypt.hashpw(current_password, bcrypt.gensalt(10))

    # Update password
    self.password = hashed.decode("utf-8") 

    # Proceed save
    super(PlayList, self).save(*args, **kwargs)
