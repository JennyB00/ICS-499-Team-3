from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.message import *
from Database.database import *
from Database import message_repo as mr

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=Message)
def read_message(id: int, db: Session = Depends(get_db)):
    db_message = mr.get_message(db, id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message Not Found")
    return db_message

@router.delete("/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):
    if mr.delete_message(db, id):
        return {"message":"Message successfully deleted"}
    else:
        raise HTTPException(status_code=404,detail="Message Not Found")