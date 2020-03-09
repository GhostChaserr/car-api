


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