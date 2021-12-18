from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from app.schemas.member_info import MemberInfo, MemberNamePairs
from app.db.crud.crud_members import (get_member_base_info, get_name_pairs, 
    search_names) 
# from sqlalchemy.orm import Session 

from app.db.database import get_session

# Instantiate a router
router = APIRouter()

# Get member by SSNo
@router.get("/get/{id}", response_model=MemberInfo)
async def get_member_by_id(id:str, session:Session = Depends(get_session)) -> Dict:
    results = get_member_base_info(ssno=id, session=session)

    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Member with SSNo {id} could not be found")

    return results

# Get Last_Name, First_Name for Searchbar
@router.get("/name-pairs", response_model= List[MemberNamePairs])
def get_member_name_pairs(session:Session = Depends(get_session)) -> List:
    results = get_name_pairs(session=session)

    return results

@router.get("/search/{ltrs}")
def search_members(ltrs:str, session:Session = Depends(get_session)) -> List:
    results = search_names(ltrs=ltrs, session=session)

    return results