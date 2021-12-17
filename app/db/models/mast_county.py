from sqlalchemy import Table 

from app.db.database import Base, metadata

class Mast_County(Base):
    """Map the existing Mast_County table"""
    __table__ = Table("Mast_County", metadata, autoload=True)