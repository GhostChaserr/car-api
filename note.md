


# App Timeline
[X] server setup
  [] Routes
    [x] GET - Fetching list of cars
    [x] GET - Fetch single car
    [x] POST - Register new car
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