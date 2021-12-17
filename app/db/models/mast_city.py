from sqlalchemy import Table 

from app.db.database import Base, metadata 

class Mast_City(Base):
    """Map the existing Mast_City table"""
    __table__ = Table("Mast_City", metadata, autoload=True)