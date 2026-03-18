import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
try:
    with engine.connect() as conn:
        print("Connected to database!")
except Exception as e:
    print("Error:", e)