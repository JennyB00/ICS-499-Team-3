from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.privileges import *
from Database.database import *
from Database import privileges_repo as pr

router = APIRouter(
    prefix="/privileges",
    tags=["privileges"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=Privileges)
def read_privileges(id: int, db: Session = Depends(get_db)):
    db_privileges = pr.get_privileges(db, id)
    if db_privileges is None:
        raise HTTPException(status_code=404, detail="Privileges Not Found")
    return db_privileges

@router.patch("/{id}", response_model=Privileges)
async def update_privileges(id: int, privilege: Privileges, db: Session = Depends(get_db)):
    db_privileges = pr.update_privileges(db, id, privilege.dict(exclude_unset=True))
    if db_privileges is None:
        raise HTTPException(status_code=404, detail="Privileges not found")
    else:
        return db_privileges

@router.delete("/{id}")
def delete_privileges(id: int, db: Session = Depends(get_db)):
    if pr.delete_privileges(db, id):
        return {"message":"Privileges successfully deleted"}
    else:
        raise HTTPException(status_code=404,detail="Privileges Not Found")