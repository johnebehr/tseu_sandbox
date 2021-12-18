import itertools

from typing import Tuple

from sqlalchemy import select
# from sqlalchemy.engine import result
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import concat

from app.db.database import SessionLocal

# from app.db.model_loader import m 
from app.db.models.members import Members

def get_member_base_info(ssno:str, session:Session = SessionLocal()) -> Tuple: 
    qry = select(Members.First_Name, Members.Last_Name, 
        Members.Address1, Members.City, Members.State, Members.Zip).\
        where(Members.Soc_Sec_No == ssno)

    results = session.execute(qry).first()

    return results

def get_name_pairs(session:Session = SessionLocal()):
    qry = select(Members.Last_Name, Members.First_Name).\
        group_by(Members.Last_Name, Members.First_Name).\
        order_by(Members.Last_Name, Members.First_Name)

    results = session.execute(qry).all()

    return results

def search_names(ltrs:str, session:Session = SessionLocal()):
    qry = select(Members.Last_Name, Members.First_Name, Members.tseuId, 
        Members.Soc_Sec_No).\
        where(concat(Members.Last_Name, ', ', Members.First_Name).startswith(f"{ltrs}")).\
        group_by(Members.Last_Name, Members.First_Name).\
        order_by(Members.Last_Name, Members.First_Name)

    results = session.execute(qry).all()[:20]

    return results