from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.contacts import *
from Database.database import *
from Database import past_chats_repo as pr

router = APIRouter(
    prefix="/past_chats",
    tags=["past_chats"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=int)
def read_past_chat(id: int, db: Session = Depends(get_db)):
    db_contact = pr.get_past_chat(db, id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact Not Found")
    return db_contact.past_chat_id

@router.delete("/{id}")
def delete_past_chat(id: int, db: Session = Depends(get_db)):
    if pr.delete_past_chat(db, id):
        return {"message":"Contact Deleted"}
    else:
        raise HTTPException(status_code=404,detail="Contact Not Found")