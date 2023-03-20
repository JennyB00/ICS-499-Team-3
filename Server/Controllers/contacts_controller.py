from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.contacts import *
from Database.database import *
from Database import contacts_repo as cr

router = APIRouter(
    prefix="/contacts",
    tags=["contacts"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=str)
def read_contact(id: int, db: Session = Depends(get_db)):
    db_contact = cr.get_contact(db, id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact Not Found")
    return db_contact.contact

@router.delete("/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):
    if cr.delete_contact(db, id):
        return {"message":"Contact successfully deleted"}
    else:
        raise HTTPException(status_code=404,detail="Contact Not Found")