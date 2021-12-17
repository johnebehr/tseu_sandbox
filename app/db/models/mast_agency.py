from sqlalchemy import Table 

from app.db.database import Base, metadata 

class Mast_Agency(Base):
    """Map the existing Mast_Agency table"""
    __table__ = Table("Mast_Agency", metadata, autoload=True)