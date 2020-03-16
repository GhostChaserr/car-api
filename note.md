


# App Timeline
[X] server setup
  [] Routes
    [X] User routes
      [x] GET  - Paginated list of users
      [x] GET  - Single user
      [x] POST - Register user
      [x] POST - Login user
      [x] GET  - Query logged in user
      [x] POST - Create new channel
      [x] PUT - update channel
        ?action=action_type
      [x] PUT - update video
        ?action=action_type
      
  [X] Authentication
    [x] Sign up
      [x] Password hashing
      [x] Token generation
    [x] Sign in
    [x] Me query
  [] Helpers
    [x] Query module
    [x] Auth module
    [] Error module
  [] Actions
    [X] Video 
      [x] Upload video
      [x] Update video
      [x] Comment video
      [x] Upvote video
      [x] Downvote video
    [X] Channel
      [x] Create channel
      [x] Update channel
      [x] Delete channel
      [x] Follow channel
      [x] Unfollow channel
    
# Start server
uvicorn main:app --reload


```
    ------------------
        CHANNEL ENDPOINTS
    ------------------
```

# Create channel
> POST /api/channels
{
  "name": "channel name",
  "summary": "channel summary",
  "tags": [
    "channel tag"
  ]
}

# Update channel
> PUT /api/channels/channel_id/action=update
{
  "name": "updated",
  "summary": "updated",
  "tags": [
    "updated"
  ]
}

# Follow channel
> PUT /api/channels/channel_id/action=follow
{

}

# Unfollow channel
> PUT /api/channels/channel_id/action=unfollow
{

}

```
    ------------------
        CHANNEL ENDPOINTS
    ------------------
```

# Publish new video
> POST - /api/channels/chanel_id/videos 
{
	"name": "videoname",
	"summary": "videosummary",
	"path": "bucket.mp5",
	"filename": "bucjet.m5.me.child",
	"tags": ["development"],
	"thumbnail":{
		"path":"path",
		"filename":"filename"
	}
}

# Comment video
api/videos/video_id?action=comment
{
	"comment": "what a nice comment"
}

# Upvote video
api/videos/video_id?action=upvote
{

}

# Downvote video
api/videos/video_id?action=downvote
{

}

# Trash video
api/videos/vide_id?action=trash
{

}