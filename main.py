

# Enable reading env variables
from fastapi import FastAPI
# from dotenv import load_dotenv
from mongoengine import connect
from starlette.graphql import GraphQLApp
import graphene



# Connect to db
connect('youtube-clone')

# Enable reading env variables
# load_dotenv()

# Load Graphql Operations
from graph.Query import Query



# Initialize app
app = FastAPI()


# Register schema
schema = graphene.Schema(
  query=Query
  
)

# Registering graphql Endpoint
app.add_route("/graphql", GraphQLApp(schema=schema))

# Register routes
import routes.cars
import routes.users
import routes.channels
import routes.videos