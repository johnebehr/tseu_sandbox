from sqlalchemy import Table 

from app.db.database import Base, metadata

class COPE_Contributions(Base):
    """Map the existing COPE_Contributions table"""
    __table__ = Table("COPE_Contributions", metadata, autoload=True)