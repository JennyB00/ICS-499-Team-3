from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.privileges import Privileges, PrivilegesPy
from Database.Database import *
from Database.privilegesRepo import *


app = APIRouter(
    prefix="/privileges",
    tags=["privileges"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@app.get("/", response_model=list[Privileges])
def read_all_privileges(limit: int = 100, db: Session = Depends(get_db)):
    return get_all_privileges(db, limit=limit)

@app.get("/{id}", response_model=Privileges)
def read_privileges(id: int, db: Session = Depends(get_db)):
    return get_privileges(db, id)