import os
from dotenv.main import load_dotenv
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(".env")

DB_ACCESS_TOKEN = os.environ.get("DB_ACCESS_TOKEN")
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HTTP_PATH = os.environ.get("DB_HTTP_PATH")

engine = create_engine(
    f"databricks+pyhive://token:{DB_ACCESS_TOKEN}@westeurope.azuredatabricks.net:443/{DB_DATABASE}",
    connect_args={"http_path": DB_HTTP_PATH},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
