from datetime import datetime

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import ForeignKey


# Models
class BaseModel:
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    last_edit = Column(TIMESTAMP, default=datetime.utcnow)


class Tweet(BaseModel):
    __tablename__ = "tweets"
    content = Column(String(255), nullable=False)
    user = Column(ForeignKey('users.id'), nullable=False)


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(String(255), nullable=False)
    username = Column()
