from app.util.settings import Settings
from sqlalchemy.engine.url import URL 
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Instantiate a settings object 
db_settings = Settings()

# Create a database URL for SQLAlchemy 
SQL_ALCHEMY_DATABASE_URL = URL.create(**db_settings.get_alchemy_dict())

# Create the SQLAlchemy engine
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# Instantiate the base parent class
Base = declarative_base()

# Enable table metadata retrival
metadata = MetaData(bind=engine)

# Create a SessionLocal class 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=False)