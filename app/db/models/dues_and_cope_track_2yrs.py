from sqlalchemy import Table 

from app.db.database import Base, metadata

class Dues_And_Cope_Track_2yrs(Base):
    """Map the existing dues_and_cope_track_2yrs table"""
    __table__ = Table("dues_and_cope_track_2yrs", metadata, autoload=True)