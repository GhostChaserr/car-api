from fastapi import Response, Request, status
from main import app



# Load models
from models.video import Video, VideoType
from models.shared.photo import Photo, PhotoType
from models.comment import Comment, CommentAuthor, CommentType


# Load helper modules
from modules.Auth import Auth
from modules.Util import Util

auth_module = Auth()
util_module = Util()




@app.get("/api/videos")
def query_videos(request: Request, response: Response):
  return { "msg" : "query videos" }

def query_video(request: Request, response: Response):
  return { "msg": "query video!" }



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

@app.put('/api/videos/{video_id}')
def update_video(
  comment_payload: CommentType,
  video_id: str,
  request: Request, 
  response: Response,
  action: str
):

  user = auth_module.get_me(request=request)

  if user is None:
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return util_module.generate_response_context(status=403, error='access denied!', data=None)

  # Update video
  if action == 'update':
    return { "msg": "update video!" }

  # Trash video
  if action == 'trash':

    # Perform clean delete
    Video.objects(pk=video_id).update(set__status="deleted")
    
    return { "msg": "trashed" }


  if action == 'upvote':

    # Push user to upvotes arrat
    Video.objects(pk=video_id).update(
      add_to_set__upvotes=[user.get("_id")],
      pull__downvotes=user.get("_id")
    )

    return { "msg": "upvoting video" }
  
  if action == 'downvote':

    # Push user to downvotes array
    Video.objects(pk=video_id).update(
      add_to_set__downvotes=[user.get("_id")],
      pull__upvotes=user.get("_id"),
    );

    return  { "msg": "downvote video" }
  
  if action == 'comment':

    # Initialize comment
    comment = Comment()
    comment.video = video_id
    comment.comment = comment_payload.comment

    # Initialize author
    author = CommentAuthor()
    author.name = user.get("name")
    author.surname = user.get("surname")
    author.user = user.get("_id")

    # Append author and save
    comment.author = author
    comment.save()

    return { "msg" : "comment added!" }



  # Provide action
  return { "msg" : "updating video!"}


@app.delete('/api/videos/{video_id}')
def delete_video(request: Request, response: Response):
  return { "msg": "delete video" }

  







  
