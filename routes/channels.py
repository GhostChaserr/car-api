from fastapi import Response, Request, status, Query
from main import app
import uuid



# Load models
from models.channel import Channel, ChannelType
from models.shared.photo import Photo, PhotoType
from models.video import Video, VideoType

# Load helper modules
from modules.Auth import Auth
from modules.Query import Query
from modules.Util import Util


auth_module = Auth()
util_module = Util()

@app.post('/api/channels')
def create_channel(channel_payload: ChannelType, request: Request, response: Response):

  # Get logged in user
  user = auth_module.get_me(request=request)

  if user is None:
    return { "msg": "access denied!" }

  # Channel fields
  channel = Channel()
  channel.name = channel_payload.name
  channel.summary = channel_payload.summary
  channel.tags = channel_payload.tags
  channel.admins = [user.get("_id")]
  
  # Channel cover 
  cover = Photo()
  cover._id = uuid.uuid4()
  cover.filename = "path-filename"
  cover.path = "path-photo"
  channel.cover = cover

  channel.save() 

  return { "msg" : "create channel route!" }


@app.put("/api/channels/{channel_id}")
def update_channel(
  channel_payload: ChannelType,
  channel_id: str,
  request: Request,
  response: Response,
  action: str
):

  # Get logged in user
  user = auth_module.get_me(request=request)

  if user is None:
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return util_module.generate_response_context(status=403, error='access denied!', data=None)

  if action == 'update':
    
    # Check ownership
    if not Channel.objects(pk=channel_id, admins__contains= user.get("_id")):
      response.status_code = status.HTTP_403_FORBIDDEN
      return util_module.generate_response_context(status=403, error='access denied! now owner', data=None)

    # Update
    Channel.objects(_id=channel_id).update(
      set__name= channel_payload.name,
      set__summary=channel_payload.summary,
      set__tags= channel_payload.tags
    )

    # Retrun success response
    return { "msg": 'updated' }
  
  if action == 'follow':
    
    # Add new follower
    Channel.objects(pk=channel_id).update(add_to_set__followers = [user.get("_id")]);
    
    return { "msg" : "follow channel" }
  
  if action == 'unfollow':

    # Add new follower
    Channel.objects(pk=channel_id).update(pull__followers = user.get("_id"));

    return { "msg": "unfollow channel" }
  
  if action =='delete':

    # Clean delete channel
    Channel.objects(_id=channel_id).update(set__status= 'deleted')

    # Return response
    return { "msg": "deleted!" }
  
  if action == 'add-admin':

    return { "case": "assign admin to channel" }


  
  # No action was provided
  return { "msg": "provide action query parameter!" }


@app.delete("/api/channels/{channel_id}")
def delete_channel(channel_id: str,request: Request, response: Response):

  # Clean delete channel
  Channel.objects(_id=channel_id).update(set__status= 'deleted')

  # Return response
  return { "msg": "deleted!" }


@app.post('/api/channels/{channel_id}/videos')
def publish_video(video_payload: VideoType, channel_id: str,request: Request, response: Response):

  video = Video()
  video.name = video_payload.name
  video.summary = video_payload.summary
  video.tags = video_payload.tags
  video.path = video_payload.path
  video.filename = video_payload.filename
  video.channel = channel_id

  # Thumbnail
  thumbnail = Photo()
  thumbnail._id = uuid.uuid4()
  thumbnail.path = video_payload.thumbnail.path
  thumbnail.filename = video_payload.thumbnail.filename
  video.thumbnail = thumbnail

  # Save vide
  video.save()


  return { "msg": "publishing videos!" }

@app.put('/api/channels/{channel_id}/videos/{vide_id}')
def update_video(request: Request, response: Response):
  return { "msg" : "updating video!"}


@app.delete('/api/channels/{channel_id}/videos/{vide_id}')
def delete_video(request: Request, response: Response):
  return { "msg": "delete video" }

  




