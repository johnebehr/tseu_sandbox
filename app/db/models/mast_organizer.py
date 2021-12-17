from sqlalchemy import Table 

from app.db.database import Base, metadata

class Mast_Organizer(Base):
    """Map the existing Mast_Organizer table"""
    __table__ = Table("Mast_Organizer", metadata, autoload=True)