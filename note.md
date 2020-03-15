


# App Timeline
[X] server setup
  [] Routes
    [X] User routes
      [x] GET  - Paginated list of users
      [x] GET  - Single user
      [x] POST - Register user
      [x] POST - Login user
      [x] GET  - Query logged in user
    [] Order routes
      [] GET - Paginated list of user orders
      [] GET - Single order
      [] POST - Register new order
  [X] Authentication
    [x] Sign up
      [x] Password hashing
      [x] Token generation
    [x] Sign in
    [x] Query loggged in user
  [] Helpers
    [x] Query module
    [x] Auth module
    [] Error module
    
# Start server
uvicorn main:app --reload


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
> PUT /api/channels/channel_id/action=update
{

}

# Unfollow channel
> PUT /api/channels/channel_id/action=update
{

}