from sqlalchemy import Table 

from app.db.database import Base, metadata 

class Mast_Location(Base):
    """Map the Mast_Location table"""
    __table__ = Table("Mast_Location", metadata, autoload=True)