from sqlalchemy import create_engine, inspect, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from .config import DATABASE_URL

print(f"Connecting to database at {DATABASE_URL}")

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    """Establish and return a database connection."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()

def read_tweets():
    session = get_connection()
    tweets = session.query(Tweet).all()
    for tweet in tweets:
        print(f"{tweet.id}: @{tweet.username} - {tweet.content}")
    session.close()


def check_schema():
    """Check and print the schema of the 'tweets' table."""
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    columns = inspector.get_columns('tweets')
    for column in columns:
        print(f"Column: {column['name']}, Type: {column['type']}")

def write_tweet(username, content):
    """Write a tweet to the database."""
    session = get_connection()
    tweet = Tweet(username=username, content=content)
    session.add(tweet)
    session.commit()
    session.close()
