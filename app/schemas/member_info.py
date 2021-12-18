# from app.db.database import Base
from typing import Optional 

from pydantic import BaseModel

class MemberBase(BaseModel):
    First_Name:Optional[str] = None 
    Last_Name:Optional[str] = None 

class MemberInfo(MemberBase):
    Address1:Optional[str]
    City:Optional[str]
    State:Optional[str]
    Zip:Optional[str]

    class Config:
        orm_mode = True

class MemberNamePairs(BaseModel):
    Last_Name:str
    First_Name:str