from sqlalchemy import Table 

from app.db.database import Base, metadata 

class Dues(Base):
    """Map the exitsing Dues table"""
    __table__ = Table("Dues", metadata, autoload=True)