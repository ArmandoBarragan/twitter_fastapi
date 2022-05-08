# FastAPI imports
from fastapi import FastAPI

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# Project imports
import settings
from twitter.routes.users import router as user_router


DATABASE_URL = settings.DATABASE_URL

app = FastAPI()
app.include_router(user_router, prefix='/users')
