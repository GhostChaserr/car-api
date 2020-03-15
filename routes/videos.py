from fastapi import Response, Request, status
from main import app




@app.get("/api/videos")
def query_videos(request: Request, response: Response):
  return { "msg" : "query videos" }

def query_video(request: Request, response: Response):
  return { "msg": "query video!" }

