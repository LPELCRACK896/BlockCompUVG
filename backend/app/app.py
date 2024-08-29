import argparse
import uvicorn
import os
from fastapi import FastAPI
from config.config import Settings

# Identify env
parser = argparse.ArgumentParser(description="Run FastAPI application")
parser.add_argument(
    "--env", 
    choices=["dev", "prod"], 
    default="dev", 
    help="Set the environment (dev or prod)"
)
args = parser.parse_args()

# Set environment variable
os.environ['APP_ENV'] = args.env

settings = Settings(args.env)
settings.setup_config()

app = FastAPI()

# Import and include the router
from routes.user import user
app.include_router(router=user, prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
